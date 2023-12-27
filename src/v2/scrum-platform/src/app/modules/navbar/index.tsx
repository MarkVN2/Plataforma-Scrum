 import Image from 'next/image';
import '../../globals.css'

const Navbar = () => {
    return(
        <nav className="fixed bg-transparent  backdrop-blur-sm w-screen h-20 border-solid border-b-[0.25px] border-slate-300">
            <div className=' grid grid-flow-col'>
                <div className='flex'>
                    <img className='h-10 w-10' src='/logo.png' alt='logo'/>
                    <h1 className='text-2xl font-bold text-white'>Scrum Platform</h1>
                </div>
                <div className=" fixed end-0">
                        <a
                        className=" text-white font-bold pointer-events-none flex place-items-center gap-2 p-8 lg:pointer-events-auto lg:p-0"
                        href="https://github.com/Byte-Boost"
                        target="_blank"
                        rel="noopener noreferrer"
                        >
                        by{' Byte Boost'}
                    </a>
                </div>
            </div>
        </nav>
    )
}
export default Navbar;
