import { Card, CardContent, CardHeader, CardTitle } from "@myapp/ui/components/ui/card";

export default function Home() {
  return (
    <div className="p-6 space-y-6">
      <h1 className="text-2xl font-bold">Welcome</h1>
      <Card>
        <CardHeader>
          <CardTitle>Getting Started</CardTitle>
        </CardHeader>
        <CardContent>
          <p>Edit this page to start building your desktop app.</p>
        </CardContent>
      </Card>
    </div>
  );
}
