const http = require('http');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

// Determine project root directory
const ROOT_DIR = fs.existsSync(path.join(__dirname, 'index.html'))
  ? __dirname
  : (fs.existsSync(path.join(__dirname, 'Dynamic-Portfolio-Website-', 'index.html'))
      ? path.join(__dirname, 'Dynamic-Portfolio-Website-')
      : process.cwd());

const DEFAULT_PORT = parseInt(process.env.PORT, 10) || 3000;
const shouldOpenBrowser = !process.argv.includes('--no-open');

// MIME types
const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.htm': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.mjs': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.webp': 'image/webp',
  '.avif': 'image/avif',
  '.ico': 'image/x-icon',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.ttf': 'font/ttf',
  '.otf': 'font/otf',
  '.mp4': 'video/mp4',
  '.webm': 'video/webm',
  '.mp3': 'audio/mpeg',
  '.wav': 'audio/wav',
  '.pdf': 'application/pdf',
  '.txt': 'text/plain; charset=utf-8',
};

// Live reload SSE clients
const clients = new Set();

const LIVE_RELOAD_SCRIPT = `
<!-- Dynamic Live Reload -->
<script>
(() => {
  const source = new EventSource('/__livereload');
  source.onmessage = (event) => {
    if (event.data === 'reload') {
      console.log('[live-reload] File changed, reloading...');
      window.location.reload();
    }
  };
  source.onerror = () => {
    source.close();
    setTimeout(() => {
      // Reconnect after delay if server restarted
      try { new EventSource('/__livereload'); } catch (e) {}
    }, 2000);
  };
})();
</script>
`;

function notifyReload() {
  for (const client of clients) {
    try {
      client.write('data: reload\n\n');
    } catch (e) {
      clients.delete(client);
    }
  }
}

// Watch directory for changes (with debounce)
let reloadTimeout = null;
try {
  fs.watch(ROOT_DIR, { recursive: true }, (eventType, filename) => {
    if (!filename) return;
    const norm = filename.replace(/\\/g, '/');
    if (norm.includes('.git') || norm.includes('node_modules') || norm.endsWith('.tmp')) {
      return;
    }
    const ext = path.extname(filename).toLowerCase();
    if (['.html', '.css', '.js', '.svg', '.json', '.png', '.jpg', '.avif'].includes(ext)) {
      clearTimeout(reloadTimeout);
      reloadTimeout = setTimeout(() => {
        console.log(`[live-reload] Change detected in ${filename}. Refreshing browser...`);
        notifyReload();
      }, 100);
    }
  });
} catch (err) {
  console.warn('[live-reload] File watching disabled:', err.message);
}

// Server request handler
const server = http.createServer((req, res) => {
  // SSE endpoint for live reload
  if (req.url === '/__livereload') {
    res.writeHead(200, {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
      'Access-Control-Allow-Origin': '*',
    });
    res.write('data: connected\n\n');
    clients.add(res);

    req.on('close', () => {
      clients.delete(res);
    });
    return;
  }

  // Parse path
  let decodedPath = '';
  try {
    const rawPath = req.url.split('?')[0].split('#')[0];
    decodedPath = decodeURIComponent(rawPath);
  } catch (e) {
    decodedPath = req.url;
  }

  // Normalize path & route mappings
  let cleanPath = decodedPath.replace(/^\/+/, '');
  if (!cleanPath || cleanPath === '') {
    cleanPath = 'index.html';
  } else if (cleanPath === 'original') {
    cleanPath = 'original.html';
  } else if (cleanPath === 'resume') {
    cleanPath = 'resume.html';
  }

  const filePath = path.join(ROOT_DIR, cleanPath);

  // Security check: ensure path is within ROOT_DIR
  if (!filePath.startsWith(ROOT_DIR)) {
    res.writeHead(403, { 'Content-Type': 'text/plain; charset=utf-8' });
    res.end('403 Forbidden');
    return;
  }

  fs.stat(filePath, (err, stats) => {
    if (err) {
      // If file not found, try appending .html
      if (err.code === 'ENOENT' && !path.extname(cleanPath)) {
        const fallbackHtml = filePath + '.html';
        if (fs.existsSync(fallbackHtml)) {
          return serveFile(req, res, fallbackHtml, fs.statSync(fallbackHtml));
        }
      }
      res.writeHead(404, { 'Content-Type': 'text/html; charset=utf-8' });
      res.end(`<!DOCTYPE html><html><head><title>404 Not Found</title></head><body style="font-family:sans-serif;padding:40px;text-align:center;"><h1>404 Not Found</h1><p>Cannot find: <code>${decodedPath}</code></p><a href="/">Return to Home</a></body></html>`);
      return;
    }

    if (stats.isDirectory()) {
      const indexInDir = path.join(filePath, 'index.html');
      if (fs.existsSync(indexInDir)) {
        return serveFile(req, res, indexInDir, fs.statSync(indexInDir));
      }
      res.writeHead(403, { 'Content-Type': 'text/plain; charset=utf-8' });
      res.end('403 Directory Listing Denied');
      return;
    }

    serveFile(req, res, filePath, stats);
  });
});

function serveFile(req, res, filePath, stats) {
  const ext = path.extname(filePath).toLowerCase();
  const contentType = MIME_TYPES[ext] || 'application/octet-stream';
  const fileSize = stats.size;

  // Handle Range requests (for smooth video playback)
  const range = req.headers.range;
  if (range && contentType.startsWith('video/')) {
    const parts = range.replace(/bytes=/, '').split('-');
    const start = parseInt(parts[0], 10);
    const end = parts[1] ? parseInt(parts[1], 10) : fileSize - 1;

    if (start >= fileSize || end >= fileSize) {
      res.writeHead(416, {
        'Content-Range': `bytes */${fileSize}`,
        'Content-Type': contentType,
      });
      return res.end();
    }

    const chunkSize = (end - start) + 1;
    const fileStream = fs.createReadStream(filePath, { start, end });
    res.writeHead(206, {
      'Content-Range': `bytes ${start}-${end}/${fileSize}`,
      'Accept-Ranges': 'bytes',
      'Content-Length': chunkSize,
      'Content-Type': contentType,
    });
    fileStream.pipe(res);
    return;
  }

  // For HTML files, inject live reload script
  if (contentType.startsWith('text/html')) {
    fs.readFile(filePath, 'utf8', (err, htmlContent) => {
      if (err) {
        res.writeHead(500, { 'Content-Type': 'text/plain; charset=utf-8' });
        res.end('500 Internal Server Error');
        return;
      }
      let finalHtml = htmlContent;
      if (finalHtml.includes('</body>')) {
        finalHtml = finalHtml.replace('</body>', `${LIVE_RELOAD_SCRIPT}</body>`);
      } else {
        finalHtml += LIVE_RELOAD_SCRIPT;
      }
      const buffer = Buffer.from(finalHtml, 'utf8');
      res.writeHead(200, {
        'Content-Type': contentType,
        'Content-Length': buffer.length,
        'Cache-Control': 'no-cache, no-store, must-revalidate',
      });
      res.end(buffer);
    });
    return;
  }

  // For all other static files
  res.writeHead(200, {
    'Content-Type': contentType,
    'Content-Length': fileSize,
    'Accept-Ranges': 'bytes',
    'Cache-Control': 'public, max-age=3600',
  });
  fs.createReadStream(filePath).pipe(res);
}

// Start server with automatic port retry
function startServer(port, maxTries = 10) {
  server.listen(port, () => {
    const localUrl = `http://localhost:${port}/`;
    console.log('\n======================================================');
    console.log('  🚀 Dynamic Portfolio Development Server Active');
    console.log('======================================================');
    console.log(`  ➜ Local:      ${localUrl}`);
    console.log(`  ➜ Portfolio:  http://localhost:${port}/index.html`);
    console.log(`  ➜ Original:   http://localhost:${port}/original.html`);
    console.log(`  ➜ Resume:     http://localhost:${port}/resume.html`);
    console.log('------------------------------------------------------');
    console.log('  🔥 Live Reload: Enabled (editing files auto-refreshes)');
    console.log('  Press Ctrl+C to stop the server\n');

    if (shouldOpenBrowser) {
      openBrowser(localUrl);
    }
  });

  server.on('error', (err) => {
    if (err.code === 'EADDRINUSE' && maxTries > 0) {
      console.log(`Port ${port} is in use, trying port ${port + 1}...`);
      startServer(port + 1, maxTries - 1);
    } else {
      console.error('Server error:', err);
    }
  });
}

function openBrowser(url) {
  const platform = process.platform;
  let cmd = '';
  if (platform === 'win32') {
    cmd = `start "" "${url}"`;
  } else if (platform === 'darwin') {
    cmd = `open "${url}"`;
  } else {
    cmd = `xdg-open "${url}"`;
  }
  exec(cmd, (err) => {
    // Ignore errors opening browser
  });
}

startServer(DEFAULT_PORT);

