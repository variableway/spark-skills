import { Card, CardContent, CardHeader, CardTitle } from "@myapp/ui/components/ui/card";

export default function Settings() {
  return (
    <div className="p-6 space-y-6">
      <h1 className="text-2xl font-bold">Settings</h1>
      <Card>
        <CardHeader>
          <CardTitle>General</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-muted-foreground">Configure your application preferences here.</p>
        </CardContent>
      </Card>
    </div>
  );
}
