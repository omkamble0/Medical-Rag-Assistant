const { spawn, exec } = require("child_process");
const http = require("http");
const path = require("path");

const rootDir = path.resolve(__dirname, "..");
const apiDir = path.join(rootDir, "api");
const webDir = path.join(rootDir, "web");

console.log("\x1b[36m%s\x1b[0m", "=========================================================");
console.log("\x1b[32m%s\x1b[0m", " 🏥 Starting AegisMed Unified Clinical Platform");
console.log("\x1b[33m%s\x1b[0m", " 🌐 Unified Application URL: http://localhost:3000");
console.log("\x1b[36m%s\x1b[0m", "=========================================================");

const isWin = process.platform === "win32";

// 1. Start Python Backend
const pythonCmd = isWin ? "python" : "python3";
const backendProcess = spawn(pythonCmd, ["-m", "uvicorn", "app.main:app", "--port", "8000"], {
  cwd: apiDir,
  shell: true,
  stdio: "inherit",
});

// 2. Start Next.js Frontend
const npmCmd = isWin ? "npm.cmd" : "npm";
const frontendProcess = spawn(npmCmd, ["run", "dev"], {
  cwd: webDir,
  shell: true,
  stdio: "inherit",
});

// 3. Automated Single Browser Launcher
let browserOpened = false;
const targetUrl = "http://localhost:3000";

function openBrowser() {
  if (browserOpened) return;
  browserOpened = true;
  console.log("\x1b[32m%s\x1b[0m", `\n✨ AegisMed is live! Opening ${targetUrl} in your browser...\n`);
  if (isWin) {
    exec(`start ${targetUrl}`);
  } else if (process.platform === "darwin") {
    exec(`open ${targetUrl}`);
  } else {
    exec(`xdg-open ${targetUrl}`);
  }
}

function pollFrontend(retries = 30) {
  if (retries <= 0) {
    openBrowser();
    return;
  }
  http
    .get(targetUrl, (res) => {
      if (res.statusCode && res.statusCode >= 200 && res.statusCode < 500) {
        openBrowser();
      } else {
        setTimeout(() => pollFrontend(retries - 1), 800);
      }
    })
    .on("error", () => {
      setTimeout(() => pollFrontend(retries - 1), 800);
    });
}

setTimeout(() => pollFrontend(), 1500);

// 4. Graceful Unified Termination
function cleanExit() {
  console.log("\nStopping AegisMed services...");
  try {
    if (isWin) {
      if (backendProcess.pid) exec(`taskkill /pid ${backendProcess.pid} /T /F`);
      if (frontendProcess.pid) exec(`taskkill /pid ${frontendProcess.pid} /T /F`);
    } else {
      backendProcess.kill("SIGINT");
      frontendProcess.kill("SIGINT");
    }
  } catch (e) {
    // Ignore cleanup errors
  }
  process.exit(0);
}

process.on("SIGINT", cleanExit);
process.on("SIGTERM", cleanExit);
process.on("exit", cleanExit);
