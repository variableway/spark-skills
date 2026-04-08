"use client";

import { useEffect, useRef } from "react";
import { Terminal } from "@xterm/xterm";
import { FitAddon } from "@xterm/addon-fit";
import "@xterm/xterm/css/xterm.css";

export default function TerminalPage() {
  const termRef = useRef<HTMLDivElement>(null);
  const xtermRef = useRef<Terminal | null>(null);

  useEffect(() => {
    if (!termRef.current || xtermRef.current) return;

    const term = new Terminal({
      theme: {
        background: "#0f172a",
        foreground: "#f8fafc",
        cursor: "#3b82f6",
      },
      fontFamily: "JetBrains Mono, Menlo, monospace",
      fontSize: 14,
      cursorBlink: true,
    });
    const fitAddon = new FitAddon();

    term.loadAddon(fitAddon);
    term.open(termRef.current);
    fitAddon.fit();

    xtermRef.current = term;

    // Simple command handler
    let line = "";
    const prompt = () => {
      term.write("\r\n$ ");
    };

    term.write("Welcome to Terminal\r\n");
    term.write("Type 'help' for available commands.\r\n");
    prompt();

    term.onData((data) => {
      const code = data.charCodeAt(0);

      if (code === 13) {
        // Enter
        const cmd = line.trim();
        line = "";

        if (cmd === "help") {
          term.write("\r\nAvailable commands:");
          term.write("\r\n  help     - Show this help");
          term.write("\r\n  clear    - Clear terminal");
          term.write("\r\n  echo     - Echo text back");
          term.write("\r\n  date     - Show current date");
          term.write("\r\n  platform - Show platform info");
          term.write("\r\n  whoami   - Show current user");
          prompt();
        } else if (cmd === "clear") {
          term.clear();
          term.write("$ ");
        } else if (cmd.startsWith("echo ")) {
          term.write("\r\n" + cmd.slice(5));
          prompt();
        } else if (cmd === "date") {
          term.write("\r\n" + new Date().toString());
          prompt();
        } else if (cmd === "platform") {
          term.write("\r\n" + navigator.platform);
          prompt();
        } else if (cmd === "whoami") {
          term.write("\r\nuser");
          prompt();
        } else if (cmd) {
          term.write(`\r\ncommand not found: ${cmd}`);
          prompt();
        } else {
          prompt();
        }
      } else if (code === 127) {
        // Backspace
        if (line.length > 0) {
          line = line.slice(0, -1);
          term.write("\b \b");
        }
      } else if (code >= 32) {
        // Printable characters
        line += data;
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
      <div className="flex items-center gap-2 border-b px-4 py-2">
        <h2 className="text-sm font-medium">Terminal</h2>
      </div>
      <div ref={termRef} className="flex-1 p-2" style={{ minHeight: "400px" }} />
    </div>
  );
}
