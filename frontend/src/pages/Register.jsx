import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import api from "../api/api";

export default function Register() {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    name: "",
    email: "",
    password: "",
  });

  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  async function handleRegister(e) {
    e.preventDefault();

    try {
      setLoading(true);

      await api.post("/auth/register", form);

      alert("Registration Successful!");

      navigate("/");
    } catch (error) {
      alert(error.response?.data?.detail || "Registration Failed");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-blue-950 flex items-center justify-center relative overflow-hidden">

      {/* Background Blur */}
      <div className="absolute w-96 h-96 bg-cyan-500 rounded-full blur-[140px] opacity-20 -top-24 -left-24"></div>
      <div className="absolute w-96 h-96 bg-blue-600 rounded-full blur-[140px] opacity-20 bottom-0 right-0"></div>

      <div className="relative w-full max-w-md">

        <div className="backdrop-blur-xl bg-white/10 border border-white/10 rounded-3xl shadow-2xl p-10">

          <div className="text-center mb-8">

            <div className="w-20 h-20 mx-auto rounded-full bg-gradient-to-r from-cyan-400 to-blue-600 flex items-center justify-center text-3xl shadow-lg">
              🤖
            </div>

            <h1 className="text-4xl font-bold text-white mt-5">
              Create Account
            </h1>

            <p className="text-slate-300 mt-2">
              Enterprise AI KnowledgeOps Platform
            </p>

          </div>

          <form onSubmit={handleRegister}>

            <div className="mb-5">

              <label className="text-slate-300 text-sm">
                Full Name
              </label>

              <input
                type="text"
                name="name"
                required
                placeholder="John Doe"
                value={form.name}
                onChange={handleChange}
                className="w-full mt-2 bg-slate-900/70 text-white border border-slate-700 rounded-xl p-4 outline-none focus:ring-2 focus:ring-cyan-400"
              />

            </div>

            <div className="mb-5">

              <label className="text-slate-300 text-sm">
                Email Address
              </label>

              <input
                type="email"
                name="email"
                required
                placeholder="john@example.com"
                value={form.email}
                onChange={handleChange}
                className="w-full mt-2 bg-slate-900/70 text-white border border-slate-700 rounded-xl p-4 outline-none focus:ring-2 focus:ring-cyan-400"
              />

            </div>

            <div className="mb-7">

              <label className="text-slate-300 text-sm">
                Password
              </label>

              <input
                type="password"
                name="password"
                required
                placeholder="••••••••"
                value={form.password}
                onChange={handleChange}
                className="w-full mt-2 bg-slate-900/70 text-white border border-slate-700 rounded-xl p-4 outline-none focus:ring-2 focus:ring-cyan-400"
              />

            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full py-4 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 text-white font-semibold text-lg hover:scale-[1.02] transition duration-300 shadow-lg"
            >
              {loading ? "Creating Account..." : "Create Account"}
            </button>

          </form>

          <div className="mt-8 text-center">

            <span className="text-slate-300">
              Already have an account?
            </span>

            <Link
              to="/"
              className="text-cyan-400 font-semibold ml-2 hover:text-cyan-300"
            >
              Login
            </Link>

          </div>

        </div>

      </div>

    </div>
  );
}