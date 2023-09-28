import { Outlet, useLocation } from "react-router-dom";
import Navbar from "./components/Navbar";

interface LayoutProps {
  hasAccount: boolean;
}

const Layout: React.FC<LayoutProps> = ({ hasAccount }) => {
  const pathname = useLocation().pathname;

  return (
    <>
      <div className="dark:bg-gray-900 dark:text-white text-black bg-slate-100 overscroll-auto h-full min-h-screen break-all">
        {!pathname.includes("/profile") && <Navbar hasAccount={hasAccount} />}
        <Outlet />
      </div>
    </>
  );
};

export default Layout;
