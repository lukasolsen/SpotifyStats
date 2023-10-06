import { useAuth } from "./context/AuthContext";

const App: React.FC = () => {
  const { isLoggedIn } = useAuth();

  const topTracks = [
    {
      name: "FLOWERS",
      artist: "Jaden",
    },
    {
      name: "XO Tour Llif3",
      artist: "Lil Uzi Vert",
    },
    {
      name: "SAD!",
      artist: "XXXTENTACION",
    },
    {
      name: "Hello",
      artist: "Adele",
    },
    {
      name: 'Lose Yourself - From "8 Mile" Soundtrack',
      artist: "Eminem",
      image:
        "https://e-cdn-images.dzcdn.net/images/cover/e2b36a9fda865cb2e9ed1476b6291a7d/500x500-000000-80-0-0.jpg",
      info: 'Album: "8 Mile" Soundtrack',
    },
  ];

  return (
    <div className="container mx-auto mt-16">
      <section className="flex flex-row justify-between items-center">
        <div className="w-7/12 pr-10">
          <h1 className="text-3xl font-bold mb-4">
            Visualize Your Spotify Listening Habits
          </h1>
          <p className="text-lg text-gray-600 mb-8">
            Spotify Stats is your gateway to exploring and understanding your
            music preferences. Discover your top artists, tracks, and more.
          </p>

          {!isLoggedIn && (
            <a
              href="/register"
              className="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-md text-lg inline-block"
            >
              Get Started
            </a>
          )}

          {isLoggedIn && (
            <div className="mt-8 flex flex-row justify-evenly items-center">
              <a
                href="/import"
                className="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-md text-lg"
              >
                Import Spotify Data
              </a>

              <a
                href={`/user/`}
                className="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-md text-lg"
              >
                Go to your dashboard
              </a>
            </div>
          )}
        </div>
      </section>

      <section className="mt-12">
        <h2 className="text-3xl font-semibold mb-4">Top Tracks</h2>
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
          {/* Replace this with data from your top tracks */}
          {topTracks.map((track, index) => (
            <div
              key={index}
              className="relative bg-white dark:bg-gray-800 shadow-md p-4 cursor-pointer overflow-hidden object-cover rounded-lg mb-4 h-52 w-full"
              style={{
                backgroundImage: `linear-gradient(rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.7)), url(${track.image})`,
                backgroundPosition: "top right",
                backgroundSize: "cover",
                backgroundRepeat: "no-repeat",
              }}
            >
              {/* Track Title and Author */}
              <h3 className="text-lg font-semibold text-white mb-2">
                {track.name}
              </h3>
              <p className="text-gray-300 dark:text-white">{track.artist}</p>

              {/* Hover Info */}
              <div className="opacity-0 absolute top-0 right-0 w-full h-full bg-black bg-opacity-80 text-white text-xs flex flex-col justify-center items-center transition-opacity duration-300 hover:opacity-100">
                <p className="text-sm mb-2">Track Info</p>
                {/* Add additional information about the track here */}
                <p>{track.info}</p>
              </div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
};

export default App;
