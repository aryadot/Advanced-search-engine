import requests
import re
import psycopg2
from datetime import datetime

# Step 1: Fetch Markdown
url = "https://raw.githubusercontent.com/public-apis/public-apis/master/README.md"
md = requests.get(url).text
sections = re.split(r"### ", md)[1:]

# Step 2: Parse
apis = []
for section in sections:
    category = section.split('\n')[0].strip()
    rows = re.findall(
        r"\| \[([^\]]+)\]\(([^)]+)\) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|", section
    )
    for row in rows:
        apis.append((
            row[0].strip(),          # name
            row[1].strip(),          # link
            row[2].strip(),          # description
            row[3].strip(),          # auth
            row[4].strip().lower() == "yes",  # https (boolean)
            row[5].strip(),          # cors
            category.strip(),        # category
            datetime.now()           # added
        ))

# Step 3: Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="api_search_engine",
    user="postgres",
    password="your_password",  # 🔐 replace with your password
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Step 4: Insert data
cur.execute("DELETE FROM apis")  # Clear previous data

cur.executemany("""
    INSERT INTO apis (name, link, description, auth, https, cors, category, added)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""", apis)

conn.commit()
cur.close()
conn.close()

print(f"✅ Inserted {len(apis)} APIs into PostgreSQL")
