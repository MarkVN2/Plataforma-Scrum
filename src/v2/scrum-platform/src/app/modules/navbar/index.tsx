import Image from 'next/image';
import '../../globals.css'

const Navbar = () => {
    return(
        <nav className="navbar navbar--fixed-top">
            <div className='navbar__inner'>
                <div className='navbar__items'>
                    <a className='navbar__brand'> 
                        <Image
                        className='navbar__logo'
                        src={'/amogus'}
                        width={100}
                        height={100}
                        alt='scrum_platform_logo'
                        />
                        <strong className='navbar__title font-NotoSans '>by Byte-Boost</strong>
                    </a>
                </div>
                <div className='navbar__items navbar__items--right '>
                    <a href="https://github.com/Byte-Boost/Plataforma-Scrum" target="_blank" rel="noopener noreferrer" className="navbar__item navbar__link">GitHub</a>
                    <a href="https://github.com/Byte-Boost" target="_blank" rel="noopener noreferrer" className="navbar__item navbar__link">Team</a>
                </div>
            </div>
        </nav>
    )
}
export default Navbar;
