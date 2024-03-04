import { Menu } from "antd";
import { HomeOutlined } from "@ant-design/icons";
export default function MenuList(){
    return (
    <Menu theme="dark" mode="inline" className="menu-bar">
        <Menu.SubMenu title="Welcome"> 
            <Menu.Item key="1" icon={<HomeOutlined/>}>
                Home
            </Menu.Item>
        </Menu.SubMenu>
    </Menu>
    )
}