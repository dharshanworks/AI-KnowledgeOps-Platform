import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-blue-950 text-white overflow-hidden">

      {/* Navbar */}
      <nav className="max-w-7xl mx-auto flex justify-between items-center px-8 py-6">

        <h1 className="text-2xl font-bold">
          Enterprise AI
        </h1>

        <div className="flex gap-4">

          <Link
            to="/login"
            className="px-5 py-2 rounded-lg hover:bg-white/10 transition"
          >
            Login
          </Link>

          <Link
            to="/register"
            className="px-5 py-2 bg-cyan-500 rounded-lg hover:bg-cyan-600 transition"
          >
            Register
          </Link>

        </div>

      </nav>

      {/* Hero */}

      <section className="max-w-7xl mx-auto px-8 py-24 grid lg:grid-cols-2 gap-16 items-center">

        <div>

          <p className="text-cyan-400 font-semibold mb-4">
            AI Powered Enterprise Knowledge Platform
          </p>

          <h1 className="text-6xl font-extrabold leading-tight">

            Chat With

            <span className="block text-cyan-400">
              Your Documents
            </span>

          </h1>

          <p className="mt-8 text-slate-300 text-lg">

            Upload PDFs, build an AI knowledge base,
            and instantly get accurate answers using
            Retrieval-Augmented Generation.

          </p>

          <div className="flex gap-5 mt-10">

            <Link
              to="/register"
              className="px-8 py-4 rounded-xl bg-cyan-500 hover:bg-cyan-600 font-semibold"
            >
              Get Started
            </Link>

            <Link
              to="/login"
              className="px-8 py-4 rounded-xl border border-white/20 hover:bg-white/10"
            >
              Login
            </Link>

          </div>

        </div>

        <div>

          <div className="bg-white/10 backdrop-blur-xl rounded-3xl border border-white/10 p-8 shadow-2xl">

            <h2 className="text-2xl font-bold mb-6">
              Platform Highlights
            </h2>

            <div className="grid grid-cols-2 gap-4">

              <div className="bg-slate-900 rounded-xl p-5">
                🤖
                <h3 className="font-bold mt-2">Groq AI</h3>
              </div>

              <div className="bg-slate-900 rounded-xl p-5">
                📄
                <h3 className="font-bold mt-2">RAG Pipeline</h3>
              </div>

              <div className="bg-slate-900 rounded-xl p-5">
                ⚡
                <h3 className="font-bold mt-2">Kafka</h3>
              </div>

              <div className="bg-slate-900 rounded-xl p-5">
                ☁️
                <h3 className="font-bold mt-2">Kubernetes</h3>
              </div>

            </div>

          </div>

        </div>

      </section>

    </div>
  );
}