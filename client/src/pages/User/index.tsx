import { useState } from "react";
import { FaMoon, FaSun } from "react-icons/fa"; // Icons for dark/light mode

const UserMenu = () => {
  const [darkMode, setDarkMode] = useState(false);

  // Sample user data
  const user = {
    name: "John Doe",
    email: "johndoe@example.com",
    mostListenedSongs: [
      { name: "Song 1", artist: "Artist 1", year: 2022 },
      { name: "Song 2", artist: "Artist 2", year: 2022 },
      { name: "Song 3", artist: "Artist 3", year: 2021 },
      // Add more songs as needed
    ],
  };

  // Function to toggle dark/light mode
  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  return (
    <div className={`min-h-screen ${darkMode ? "dark" : ""}`}>
      {/* Dark/Light mode toggle */}
      <div className="flex justify-end p-4">
        <button
          className="text-2xl text-gray-400 hover:text-gray-600"
          onClick={toggleDarkMode}
        >
          {darkMode ? <FaSun /> : <FaMoon />}
        </button>
      </div>

      {/* User Information */}
      <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg">
        <h1 className="text-3xl font-semibold">{user.name}</h1>
        <p className="text-gray-500">{user.email}</p>
      </div>

      {/* Most Listened Songs */}
      <div className="mt-6">
        <h2 className="text-2xl font-semibold">Most Listened Songs</h2>
        <div className="mt-4 space-y-4">
          {user.mostListenedSongs.map((song, index) => (
            <div
              key={index}
              className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-md flex justify-between items-center"
            >
              <div>
                <p className="text-lg font-semibold">{song.name}</p>
                <p className="text-gray-500">{song.artist}</p>
              </div>
              <span className="text-gray-400">{song.year}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Statistics */}
      <div className="mt-6">
        <h2 className="text-2xl font-semibold">Statistics</h2>
        {/* Add your statistics here */}
      </div>
    </div>
  );
};

export default UserMenu;
