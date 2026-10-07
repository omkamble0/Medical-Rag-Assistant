import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "AegisMed | Trusted Evidence-Based Health Guide",
  description: "Welcoming, compassionate health companion for patients and rigorous evidence-backed medical engine for healthcare professionals.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600;700&display=swap"
          rel="stylesheet"
        />
      </head>
      <body className="font-sans antialiased text-slate-800 bg-[#F6F8FB] selection:bg-indigo-100 selection:text-indigo-900">
        {children}
      </body>
    </html>
  );
}
