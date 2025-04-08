import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [authFilter, setAuthFilter] = useState("");
  const [results, setResults] = useState([]);
  const [favorites, setFavorites] = useState([]);
  const [showFavorites, setShowFavorites] = useState(false);
  const [darkMode, setDarkMode] = useState(false);
  useEffect(() => {
    if (darkMode) {
      document.body.classList.add("dark");
    } else {
      document.body.classList.remove("dark");
    }
  }, [darkMode]);
  

  // Load favorites from localStorage on load
  useEffect(() => {
    const saved = JSON.parse(localStorage.getItem("favorites")) || [];
    setFavorites(saved);
  }, []);

  // Save favorites when updated
  useEffect(() => {
    localStorage.setItem("favorites", JSON.stringify(favorites));
  }, [favorites]);

  const handleSearch = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/search", {
        params: {
          q: query,
          auth: authFilter,
        },
      });
      setResults(response.data);
    } catch (err) {
      console.error("Search failed:", err);
    }
  };

  const toggleFavorite = (api) => {
    const exists = favorites.find((f) => f.name === api.name);
    if (exists) {
      setFavorites(favorites.filter((f) => f.name !== api.name));
    } else {
      setFavorites([...favorites, api]);
    }
  };

  const isFavorited = (api) => favorites.some((f) => f.name === api.name);

  return (
    <div className={`App ${darkMode ? "dark" : ""}`}>
      <h1>🔍 API Search Engine</h1>

      {/* 🌗 Dark Mode Toggle */}
      <button onClick={() => setDarkMode(!darkMode)}>
        {darkMode ? "☀️ Light Mode" : "🌙 Dark Mode"}
      </button>

      {/* 🔎 Search Controls */}
      <input
        type="text"
        placeholder="Search for APIs..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && handleSearch()}
      />
      <button onClick={handleSearch}>Search</button>

      <select onChange={(e) => setAuthFilter(e.target.value)} value={authFilter}>
        <option value="">All Auth</option>
        <option value="No">No Auth</option>
        <option value="apiKey">API Key</option>
        <option value="OAuth">OAuth</option>
      </select>

      {/* 🔁 Tab Toggle */}
      <div className="toggle-buttons">
        <button
          className={!showFavorites ? "active" : ""}
          onClick={() => setShowFavorites(false)}
        >
          🔍 Search Results
        </button>
        <button
          className={showFavorites ? "active" : ""}
          onClick={() => setShowFavorites(true)}
        >
          ⭐ Favorites ({favorites.length})
        </button>
      </div>

      {/* 📢 Section Title */}
      <h2 className="section-title">
        {showFavorites ? "⭐ Your Favorites" : "🔍 Search Results"}
      </h2>

      {/* 📦 Results */}
      <div className="results">
        {(showFavorites ? favorites : results).map((api, index) => (
          <div key={index} className="card">
            <h2>{api.name}</h2>
            <p>{api.description}</p>
            <a href={api.link} target="_blank" rel="noreferrer">
              Docs
            </a>

            {/* 🏷️ Badges */}
            <div>
              <span className="badge auth-badge">{api.auth}</span>
              <span className="badge category-badge">{api.category}</span>
            </div>

            {/* ⭐ Favorite Button */}
            <button onClick={() => toggleFavorite(api)}>
              {isFavorited(api) ? "⭐ Remove" : "☆ Favorite"}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
