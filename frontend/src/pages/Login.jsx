import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import api from "../api/api";

export default function Login() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleLogin(e) {
    e.preventDefault();

    try {
      setLoading(true);

      const response = await api.post("/auth/login", {
        email,
        password,
      });

      console.log("Login Response:", response.data);

      const token =
        response.data.access_token ||
        response.data.token ||
        response.data.jwt;

      if (!token) {
        alert("Login succeeded but no token was returned.");
        console.log("Response:", response.data);
        return;
      }

      localStorage.setItem("token", token);

      console.log("Stored Token:", localStorage.getItem("token"));

      navigate("/dashboard");
    } catch (error) {
      console.error(error);

      alert(
        error.response?.data?.detail ||
          "Invalid email or password"
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-blue-950 flex items-center justify-center relative overflow-hidden">

      <div className="absolute w-96 h-96 bg-cyan-500 rounded-full blur-[140px] opacity-20 -top-24 -left-24"></div>

      <div className="absolute w-96 h-96 bg-blue-600 rounded-full blur-[140px] opacity-20 bottom-0 right-0"></div>

      <div className="relative w-full max-w-md">

        <div className="backdrop-blur-xl bg-white/10 border border-white/10 rounded-3xl shadow-2xl p-10">

          <div className="text-center mb-8">

            <div className="w-20 h-20 rounded-full bg-gradient-to-r from-cyan-400 to-blue-600 flex items-center justify-center mx-auto shadow-lg text-3xl">
              🤖
            </div>

            <h1 className="text-4xl font-bold text-white mt-5">
              Welcome Back
            </h1>

            <p className="text-slate-300 mt-2">
              Enterprise AI KnowledgeOps Platform
            </p>

          </div>

          <form onSubmit={handleLogin}>

            <div className="mb-5">

              <label className="text-slate-300 text-sm">
                Email Address
              </label>

              <input
                type="email"
                placeholder="john@example.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                className="w-full mt-2 bg-slate-900/70 text-white border border-slate-700 rounded-xl p-4 outline-none focus:ring-2 focus:ring-cyan-400 transition"
              />

            </div>

            <div className="mb-7">

              <label className="text-slate-300 text-sm">
                Password
              </label>

              <input
                type="password"
                placeholder="••••••••"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                className="w-full mt-2 bg-slate-900/70 text-white border border-slate-700 rounded-xl p-4 outline-none focus:ring-2 focus:ring-cyan-400 transition"
              />

            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full py-4 rounded-xl bg-gradient-to-r from-cyan-500 via-blue-600 to-indigo-600 text-white font-semibold text-lg hover:scale-[1.02] transition duration-300 shadow-xl"
            >
              {loading ? "Signing In..." : "Sign In"}
            </button>

          </form>

          <div className="flex items-center my-8">

            <div className="flex-1 h-px bg-slate-700"></div>

            <span className="px-4 text-slate-400 text-sm">
              Secure Authentication
            </span>

            <div className="flex-1 h-px bg-slate-700"></div>

          </div>

          <div className="text-center">

            <span className="text-slate-300">
              Don't have an account?
            </span>

            <Link
              to="/register"
              className="text-cyan-400 font-semibold ml-2 hover:text-cyan-300 transition"
            >
              Create Account
            </Link>

          </div>

        </div>

      </div>

    </div>
  );
}