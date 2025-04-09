# 🔍 API Search Engine

A full-stack web app for discovering public APIs by keyword, authentication type, and category. Built with FastAPI, PostgreSQL, and React, it also supports bookmarking favorites, dark mode, and full-text search ranking.

---

## 🚀 Features

- 🔎 Search 1400+ public APIs with full-text ranking
- 🔐 Filter by authentication type (No Auth, API Key, OAuth)
- 🗂️ Filter by API category (e.g. Animals, Email, Geocoding)
- ⭐ Bookmark favorite APIs (saved locally)
- 🌗 Toggle between light and dark mode
- 🏷️ Clean UI with category + auth badges

---

## 🧰 Tech Stack

- **Frontend**: React, Axios, CSS
- **Backend**: FastAPI
- **Database**: PostgreSQL with full-text search (`tsvector` + `ts_rank`)

---

## 📦 Project Structure

```
api-search-engine/
├── backend/               # FastAPI backend
│   ├── main.py            # Main API with /search endpoint
│   └── ...
├── data_parser/          # Script to load API data into DB
│   └── insert_apis_pg.py
├── frontend/             # React frontend
│   ├── src/
│   │   ├── App.js         # Main React component
│   │   └── App.css        # Styling including dark mode & badges
│   └── ...
```

---

## 🧪 Local Development

### 1. Backend Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn psycopg2-binary
uvicorn main:app --reload
```

Make sure PostgreSQL is running and `api_search_engine` database is set up.


### 2. Load API Data
```bash
python data_parser/insert_apis_pg.py
```


### 3. Frontend Setup
```bash
cd frontend
npm install
npm start
```

---

## 🌍 Deployment

The website is deployed using Netlify. You can access it at: https://advanced-search-engine.vercel.app
### Backend (Optional)
Use [Render](https://render.com), [Railway](https://railway.app), or [Fly.io](https://fly.io) to deploy FastAPI + PostgreSQL.

---

## 🙌 Credits
- Public API dataset: https://github.com/public-apis/public-apis
- Icons: Unicode / Emoji

---

## 📄 License
MIT License

