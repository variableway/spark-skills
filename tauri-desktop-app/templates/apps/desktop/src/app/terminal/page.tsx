"use client";

import { useEffect, useRef, useState } from "react";
import { Terminal } from "@xterm/xterm";
import { FitAddon } from "@xterm/addon-fit";
import "@xterm/xterm/css/xterm.css";

type Mode = "tutorial" | "free";

interface TutorialStep {
  prompt: string;
  description: string;
}

const TUTORIAL_STEPS: TutorialStep[] = [
  { prompt: "echo 'Hello, Tauri!'", description: "Try your first command" },
  { prompt: "pwd", description: "Show current directory" },
  { prompt: "ls", description: "List files" },
  { prompt: "date", description: "Show current time" },
  { prompt: "whoami", description: "Who are you?" },
];

async function execCommand(cmd: string, onData: (d: string) => void): Promise<number> {
  // Tauri shell mode — execute and collect output
  if ("__TAURI_INTERNALS__" in window) {
    try {
      const { Command } = await import("@tauri-apps/plugin-shell");
      const command = Command.create("sh", ["-c", cmd]);
      const output = await command.execute();
      if (output.stdout) onData(output.stdout);
      if (output.stderr) onData(output.stderr);
      return output.code ?? 1;
    } catch (e: unknown) {
      onData(`error: ${e instanceof Error ? e.message : String(e)}`);
      return 1;
    }
  }

  // Browser fallback
  const builtins: Record<string, () => string> = {
    pwd: () => "/home/user",
    ls: () => "Documents  Downloads  Pictures  Desktop",
    whoami: () => "user",
    date: () => new Date().toString(),
    uname: () => "Browser (WebAssembly)",
    hostname: () => "localhost",
    clear: () => "",
    help: () =>
      [
        "Available commands:",
        "  echo  pwd  ls  whoami  date  uname  hostname  clear",
        "  Type anything else to echo it back.",
        "",
        "Run in Tauri desktop for real shell access!",
      ].join("\r\n"),
  };

  const parts = cmd.trim().split(/\s+/);
  const base = parts[0];

  if (base === "clear") {
    onData("__CLEAR__");
    return 0;
  }
  if (base === "echo") {
    onData(parts.slice(1).join(" "));
    return 0;
  }
  if (builtins[base]) {
    onData(builtins[base]());
    return 0;
  }
  onData(`(browser) ${cmd}`);
  return 0;
}

export default function TerminalPage() {
  const termRef = useRef<HTMLDivElement>(null);
  const xtermRef = useRef<Terminal | null>(null);
  const [mode, setMode] = useState<Mode>("tutorial");
  const [stepIdx, setStepIdx] = useState(0);
  const lineRef = useRef("");
  const historyRef = useRef<string[]>([]);
  const histIdxRef = useRef(-1);
  const isTauriRef = useRef(false);
  const cwdRef = useRef("~");

  useEffect(() => {
    if (!termRef.current || xtermRef.current) return;

    const term = new Terminal({
      theme: {
        background: "#0f172a",
        foreground: "#f8fafc",
        cursor: "#3b82f6",
        green: "#22c55e",
        yellow: "#f59e0b",
        cyan: "#06b6d4",
      },
      fontFamily: "JetBrains Mono, Menlo, monospace",
      fontSize: 14,
      cursorBlink: true,
      convertEol: true,
    });
    const fitAddon = new FitAddon();

    term.loadAddon(fitAddon);
    term.open(termRef.current);
    fitAddon.fit();
    xtermRef.current = term;

    isTauriRef.current = "__TAURI_INTERNALS__" in window;

    // --- Prompt ---
    const writePrompt = () => {
      term.write(`\r\n\x1b[32m${cwdRef.current}\x1b[0m \x1b[34m$\x1b[0m `);
    };

    // --- Welcome ---
    const showWelcome = () => {
      term.writeln("\x1b[36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[0m");
      term.writeln("\x1b[1;33m  Innate Terminal v0.1.0\x1b[0m");
      term.writeln(`  Mode: \x1b[32m${isTauriRef.current ? "Tauri Shell" : "Browser Emulation"}\x1b[0m`);
      term.writeln("\x1b[36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[0m");
      term.writeln("");
      term.writeln("  Type \x1b[33mhelp\x1b[0m for commands.");
      term.writeln("  Press \x1b[33mTab\x1b[0m to accept tutorial suggestion.");
      term.writeln("  Or type any command freely.");
      term.writeln("");
    };

    const showTutorialHint = () => {
      const step = TUTORIAL_STEPS[stepIdx];
      if (step) {
        term.writeln(`\x1b[33m[Tutorial ${stepIdx + 1}/${TUTORIAL_STEPS.length}] ${step.description}\x1b[0m`);
        term.writeln(`  Hint: \x1b[32m${step.prompt}\x1b[0m (press Tab to fill)`);
        term.writeln("");
      }
    };

    showWelcome();
    showTutorialHint();
    writePrompt();

    // --- Execute ---
    const execute = async (cmd: string) => {
      if (!cmd) {
        writePrompt();
        return;
      }

      historyRef.current.push(cmd);
      histIdxRef.current = historyRef.current.length;

      // Check tutorial progress
      const step = TUTORIAL_STEPS[stepIdx];
      if (step && cmd.trim() === step.prompt) {
        setStepIdx((i) => i + 1);
      }

      const code = await execCommand(cmd, (data) => {
        if (data === "__CLEAR__") {
          term.clear();
        } else {
          term.write(data);
        }
      });

      // Update cwd after cd
      if (cmd.trim().startsWith("cd ")) {
        const target = cmd.trim().slice(3) || "~";
        cwdRef.current = target === ".." ? "~" : target;
      }

      if (code !== 0) {
        term.writeln(`\x1b[31mexit code: ${code}\x1b[0m`);
      }
      writePrompt();
    };

    // --- Input ---
    term.onData((data) => {
      const code = data.charCodeAt(0);

      if (code === 13) {
        // Enter
        const cmd = lineRef.current;
        lineRef.current = "";
        term.writeln("");
        execute(cmd);
      } else if (code === 127) {
        // Backspace
        if (lineRef.current.length > 0) {
          lineRef.current = lineRef.current.slice(0, -1);
          term.write("\b \b");
        }
      } else if (code === 9) {
        // Tab - autocomplete with tutorial suggestion
        const step = TUTORIAL_STEPS[stepIdx];
        if (step && !lineRef.current) {
          lineRef.current = step.prompt;
          term.write(step.prompt);
        }
      } else if (data === "\x1b[A") {
        // Up arrow - history
        if (histIdxRef.current > 0) {
          histIdxRef.current--;
          const old = lineRef.current;
          if (old) term.write("\b \b".repeat(old.length));
          const cmd = historyRef.current[histIdxRef.current];
          lineRef.current = cmd;
          term.write(cmd);
        }
      } else if (data === "\x1b[B") {
        // Down arrow - history
        if (histIdxRef.current < historyRef.current.length - 1) {
          histIdxRef.current++;
          const old = lineRef.current;
          if (old) term.write("\b \b".repeat(old.length));
          const cmd = historyRef.current[histIdxRef.current];
          lineRef.current = cmd;
          term.write(cmd);
        } else {
          histIdxRef.current = historyRef.current.length;
          const old = lineRef.current;
          if (old) term.write("\b \b".repeat(old.length));
          lineRef.current = "";
        }
      } else if (code === 3) {
        // Ctrl+C
        term.write("^C");
        lineRef.current = "";
        writePrompt();
      } else if (code >= 32) {
        lineRef.current += data;
        term.write(data);
      }
    });

    const handleResize = () => fitAddon.fit();
    window.addEventListener("resize", handleResize);

    return () => {
      window.removeEventListener("resize", handleResize);
      term.dispose();
      xtermRef.current = null;
    };
  }, []);

  return (
    <div className="flex flex-col h-full">
      <div className="flex items-center justify-between border-b px-4 py-2">
        <h2 className="text-sm font-medium">Terminal</h2>
        <span className="text-xs text-muted-foreground">
          {typeof window !== "undefined" && "__TAURI_INTERNALS__" in window ? "Tauri Shell" : "Browser Mode"} | Tab = tutorial hint | Ctrl+C = cancel
        </span>
      </div>
      <div ref={termRef} className="flex-1 p-2" style={{ minHeight: "400px" }} />
    </div>
  );
}
