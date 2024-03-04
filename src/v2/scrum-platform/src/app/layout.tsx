import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'
import { ConfigProvider } from 'antd'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Scrum Platform',
  description: 'Scrum Platform',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <ConfigProvider
    theme={{
      token: {
        // Seed Token
        colorBgBase: '#00b96b',
        borderRadius: 2,

        // Alias Token
        colorBgContainer: '#f6ffed',
      },
    }}
    >
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
    </ConfigProvider>
  )
}
