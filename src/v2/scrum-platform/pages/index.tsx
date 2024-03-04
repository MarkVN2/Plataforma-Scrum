import Image from 'next/image'
import '../src/app/globals.css'
import Navbar from '@/src/app/modules/navbar'
import Sidebar from '@/src/app/modules/sidebar'
import { Button, Layout } from 'antd'

export default function Home() {
  return (
    <main>
      <Navbar/>
      <Sidebar/>

    </main>
  )
}