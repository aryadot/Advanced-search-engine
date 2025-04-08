from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import psycopg2

app = FastAPI()

# ✅ Allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="api_search_engine",
    user="postgres",
    password="your_password",  # ← replace with your actual password
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# ✅ /search endpoint with full-text search + auth filter + ts_rank ordering
@app.get("/search")
def search_apis(
    q: str = Query(""),
    auth: str = Query(""),
    category: str = Query("")
):
    values = []

    if q.strip():
        base_query = """
            SELECT name, link, description, auth, https, cors, category,
                   ts_rank(tsv, plainto_tsquery(%s)) AS rank
            FROM apis
            WHERE tsv @@ plainto_tsquery(%s)
        """
        values = [q, q]
    else:
        base_query = """
            SELECT name, link, description, auth, https, cors, category,
                   0.0 AS rank
            FROM apis
            WHERE TRUE
        """

    if auth and auth.lower() != "all":
        base_query += " AND LOWER(auth) LIKE %s"
        values.append(f"%{auth.lower()}%")

    if category and category.lower() != "all":
        base_query += " AND LOWER(category) LIKE %s"
        values.append(f"%{category.lower()}%")

    base_query += " ORDER BY rank DESC LIMIT 50"

    cur.execute(base_query, tuple(values))
    rows = cur.fetchall()
    keys = ["name", "link", "description", "auth", "https", "cors", "category", "rank"]
    return [dict(zip(keys, row)) for row in rows]
