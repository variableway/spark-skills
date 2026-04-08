import type { Metadata } from "next";
import { AppShell } from "@/components/layout/app-shell";
import "@myapp/ui/globals.css";

export const metadata: Metadata = {
  title: "My Desktop App",
  description: "Built with Tauri + Next.js",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <AppShell>{children}</AppShell>
      </body>
    </html>
  );
}
