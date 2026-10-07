const http = require('http');
const { exec } = require('child_process');

const targetUrl = 'http://localhost:3000';
let opened = false;

function openBrowser() {
  if (opened) return;
  opened = true;
  const platform = process.platform;
  
  if (platform === 'win32') {
    exec(`start ${targetUrl}`);
  } else if (platform === 'darwin') {
    exec(`open ${targetUrl}`);
  } else {
    exec(`xdg-open ${targetUrl}`);
  }
  console.log(`\n✨ AegisMed Unified Portal opened at ${targetUrl}\n`);
}

function checkFrontend() {
  http.get(targetUrl, (res) => {
    if (res.statusCode >= 200 && res.statusCode < 400) {
      openBrowser();
      process.exit(0);
    } else {
      setTimeout(checkFrontend, 800);
    }
  }).on('error', () => {
    setTimeout(checkFrontend, 800);
  });
}

// Start checking after 1 second, with a fallback timeout of 10s
setTimeout(checkFrontend, 1200);
setTimeout(() => {
  if (!opened) {
    openBrowser();
    process.exit(0);
  }
}, 8000);
