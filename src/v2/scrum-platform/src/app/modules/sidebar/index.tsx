import { Layout } from "antd";
import Sider from "antd/es/layout/Sider";
import Logo from "../logo";
import MenuList from "../menulist";

const Sidebar = () => {
    return(
          <Sider  className="sidebar " >
            <Logo/>
            <MenuList/>
          </Sider>
    )
}

export default Sidebar;