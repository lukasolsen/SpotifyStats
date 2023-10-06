import { Link, useLocation } from "react-router-dom";

type NavbarProps = {
  hasAccount: boolean;
};

const Navbar: React.FC<NavbarProps> = ({ hasAccount }) => {
  const location = useLocation();

  return (
    <>
      {location.pathname.includes("/login") ||
      location.pathname.includes("/register") ? null : (
        <div className="w-full p-4 pt-2 dark:text-white text-black border-b border-b-green-400 flex items-center justify-center">
          <div className="flex flex-row justify-between items-center w-2/4">
            <Link to={"/"}>
              <h1 className="text-2xl font-bold text-green-500">
                Spotify Stats
              </h1>
            </Link>

            <div className="flex flex-row space-x-4 items-center">
              <Link
                to="/"
                className={`${
                  location.pathname === "/" ? "text-green-400" : ""
                }`}
              >
                Hjem
              </Link>
              <Link
                to="/kontakt"
                className={`${
                  location.pathname === "/kontakt" ? "text-blue" : ""
                }`}
              >
                Kontakt
              </Link>
              <Link
                to="/produkter"
                className={`${
                  location.pathname === "/produkter" ? "text-blue" : ""
                }`}
              >
                Produkter
              </Link>
              <Link
                to="/pricing"
                className={`${
                  location.pathname === "/pricing" ? "text-blue" : ""
                }`}
              >
                Pricing
              </Link>
            </div>

            {!hasAccount && (
              <div className="flex flex-row space-x-4 items-center">
                <Link to="/login">Login</Link>
                <Link to="/register">Register</Link>
              </div>
            )}
          </div>
        </div>
      )}
    </>
  );
};

export default Navbar;
