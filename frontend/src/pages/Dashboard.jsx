import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/api";

export default function Dashboard() {
  const navigate = useNavigate();

  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem("token");

    if (!token) {
      navigate("/login");
    }
  }, [navigate]);

  function logout() {
    localStorage.removeItem("token");
    navigate("/");
  }

  async function uploadPDF() {
    if (!file) {
      alert("Choose a PDF");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const response = await api.post("/upload/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      alert(response.data.message);
    } catch (error) {
      alert("Upload Failed");
      console.log(error);
    } finally {
      setLoading(false);
    }
  }

  async function askAI() {
    if (!question) return;

    try {
      setLoading(true);

      const response = await api.post("/chat/", {
        question,
      });

      setAnswer(response.data.answer);
    } catch (error) {
      alert("Chat Failed");
      console.log(error);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-blue-950 text-white">

      {/* Header */}

      <header className="sticky top-0 z-50 border-b border-white/10 backdrop-blur-xl bg-slate-950/70">

        <div className="max-w-7xl mx-auto flex justify-between items-center px-8 py-5">

          <div>
            <h1 className="text-3xl font-bold">
              Enterprise AI KnowledgeOps
            </h1>

            <p className="text-slate-400 mt-1">
              AI Powered Enterprise Knowledge Management Platform
            </p>
          </div>

          <div className="flex gap-4">

            <div className="bg-cyan-500 px-5 py-2 rounded-full font-semibold">
              AI Assistant
            </div>

            <button
              onClick={logout}
              className="bg-red-500 hover:bg-red-600 px-5 py-2 rounded-full font-semibold transition"
            >
              Logout
            </button>

          </div>

        </div>

      </header>

      <div className="max-w-7xl mx-auto grid lg:grid-cols-3 gap-8 p-10">

        {/* Upload */}

        <div className="bg-white/10 backdrop-blur-xl border border-white/10 rounded-3xl p-8 shadow-2xl">

          <h2 className="text-2xl font-bold mb-6">
            Upload Knowledge Base
          </h2>

          <input
            type="file"
            accept=".pdf"
            onChange={(e) => setFile(e.target.files[0])}
            className="w-full bg-slate-900 border border-slate-700 rounded-xl p-4"
          />

          {file && (
            <div className="mt-5 bg-slate-900 rounded-xl p-4 border border-slate-700">

              <p className="text-green-400 font-medium">
                Selected File
              </p>

              <p className="mt-2 text-slate-300">
                {file.name}
              </p>

            </div>
          )}

          <button
            onClick={uploadPDF}
            className="mt-8 w-full bg-gradient-to-r from-blue-600 to-cyan-500 hover:scale-105 transition rounded-xl py-4 font-semibold"
          >
            {loading ? "Uploading..." : "Upload PDF"}
          </button>

        </div>

        {/* Chat */}

        <div className="lg:col-span-2 bg-white/10 backdrop-blur-xl border border-white/10 rounded-3xl p-8 shadow-2xl">

          <h2 className="text-2xl font-bold mb-6">
            Ask Your Documents
          </h2>

          <textarea
            rows={6}
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ask anything from your uploaded documents..."
            className="w-full bg-slate-900 border border-slate-700 rounded-2xl p-5 outline-none resize-none focus:border-cyan-500"
          />

          <button
            onClick={askAI}
            className="mt-6 bg-gradient-to-r from-emerald-500 to-cyan-500 hover:scale-105 transition px-8 py-4 rounded-xl font-semibold"
          >
            {loading ? "Thinking..." : "Ask AI"}
          </button>

          {answer && (

            <div className="mt-10 bg-slate-900 rounded-2xl border border-slate-700 p-8">

              <h3 className="text-2xl font-bold text-cyan-400 mb-5">
                AI Response
              </h3>

              <p className="leading-8 text-slate-200 whitespace-pre-wrap">
                {answer}
              </p>

            </div>

          )}

        </div>

      </div>

    </div>
  );
}