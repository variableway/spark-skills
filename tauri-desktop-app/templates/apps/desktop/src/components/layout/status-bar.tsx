"use client";

import { useEffect, useState } from "react";

export function StatusBar() {
  const [platform, setPlatform] = useState<string>("detecting...");

  useEffect(() => {
    if ("__TAURI_INTERNALS__" in window) {
      import("@tauri-apps/api/core").then(({ invoke }) => {
        invoke<string>("get_platform")
          .then(setPlatform)
          .catch(() => setPlatform("unknown"));
      });
    } else {
      setPlatform("web");
    }
  }, []);

  const platformIcon =
    platform.includes("macos") ? "🍎" :
    platform.includes("windows") ? "🪟" :
    platform.includes("linux") ? "🐧" : "🌐";

  return (
    <div className="flex items-center justify-between border-t bg-muted/50 px-4 py-1.5 text-xs text-muted-foreground">
      <div className="flex items-center gap-3">
        <span>{platformIcon} {platform}</span>
      </div>
      <div>v0.1.0</div>
    </div>
  );
}
