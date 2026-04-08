"use client";

import { SidebarProvider, SidebarTrigger } from "@myapp/ui/components/ui/sidebar";
import { AppSidebar } from "./app-sidebar";
import { StatusBar } from "./status-bar";

export function AppShell({ children }: { children: React.ReactNode }) {
  return (
    <SidebarProvider>
      <AppSidebar />
      <main className="flex flex-col flex-1 overflow-hidden">
        <SidebarTrigger />
        <div className="flex-1 overflow-auto">{children}</div>
        <StatusBar />
      </main>
    </SidebarProvider>
  );
}
