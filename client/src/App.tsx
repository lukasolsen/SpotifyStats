import { useState } from "react";
import { useAuth } from "./context/AuthContext";
import { FaFileImport, FaChartBar } from "react-icons/fa";

const App: React.FC = () => {
  const { isLoggedIn } = useAuth();
  const [file, setFile] = useState<File | null>(null);

  const handleClick = async () => {
    const handleSending = async () => {
      const formData = new FormData();
      formData.append("in_file", file!); // Use "in_file" as the key
      try {
        const response = await fetch("http://localhost:8000/upload/", {
          method: "POST",
          body: formData,
        });
        if (response.ok) {
          const data = await response.json();
          console.log(data);
        } else {
          console.error("Upload failed. Status code:", response.status);
        }
      } catch (error) {
        console.error("Error:", error);
      }
    };

    if (file) {
      handleSending();
    } else {
      console.error("Please select a file.");
    }
  };

  return (
    <>
      <div className="flex flex-row justify-between container mx-auto mt-16">
        <div className="w-6/12">
          <h1 className="text-2xl font-bold text-green-500">Spotify Stats</h1>
          <p className="text-base text-gray-400">
            Spotify Stats is a web application that allows you to see your
            Spotify statistics.
          </p>

          {!isLoggedIn && (
            <div className="flex flex-row space-x-4 items-center mt-8">
              <a
                href={"/register"}
                className="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-md w-6/12 text-center mx-auto"
              >
                Get Started
              </a>
            </div>
          )}

          {/* Display things such as 2 buttons for importing file, and going to dashboard */}
          {isLoggedIn && (
            <div className="flex flex-row space-x-4 items-center mt-8 justify-evenly">
              <a
                href={"/import"}
                className="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-md text-center flex flex-row items-center"
              >
                <FaFileImport className="mr-2" />
                Import File
              </a>

              <a
                href={"/dashboard"}
                className="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-md text-center flex flex-row items-center"
              >
                <FaChartBar className="mr-2" />
                Go to Dashboard
              </a>
            </div>
          )}
        </div>
        <div className="w-6/12 flex flex-row justify-end items-center space-x-4">
          {/* Animated SVG */}
          <div className="w-48 h-48 relative">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 100 100"
              className="w-full h-full absolute top-0 left-0"
            >
              {/* Gray harvester-like shape */}
              <rect
                x="20"
                y="20"
                width="60"
                height="60"
                fill="#ccc"
                rx="8"
                ry="8"
              />
              {/* Animated green lines */}
              <line
                x1="10"
                y1="40"
                x2="90"
                y2="40"
                stroke="green"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <animate
                  attributeName="x2"
                  from="10"
                  to="90"
                  dur="3s"
                  begin="2s"
                  repeatCount="indefinite"
                />
              </line>
              <line
                x1="10"
                y1="50"
                x2="90"
                y2="50"
                stroke="green"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <animate
                  attributeName="x2"
                  from="10"
                  to="90"
                  dur="1s"
                  begin="0s"
                  repeatCount="indefinite"
                />
              </line>
            </svg>
          </div>
        </div>
      </div>

      <div className="hidden">
        <h1>Send file to API</h1>
        <input
          type="file"
          onChange={(e) => {
            setFile(e.target.files![0]);
          }}
        />
        <button onClick={handleClick}>Send</button>
      </div>
    </>
  );
};

export default App;
