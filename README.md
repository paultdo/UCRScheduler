# UCR Scheduler

Enter courses, get every conflict-free schedule combination, ranked by preference, on an interactive calendar.

## Quick Start

### Prerequisites
- Python 3.10+ and [`uv`](https://docs.astral.sh/uv/)
- Node.js 20.19+ (or 22.12+) and npm
- A [Supabase](https://supabase.com) project (or any Postgres database)

### Backend

```bash
cd backend
uv venv
uv add fastapi "uvicorn[standard]" sqlalchemy alembic pydantic pydantic-settings requests psycopg2-binary python-dotenv beautifulsoup4

# create backend/.env with:
# DATABASE_URL=<supabase transaction pooler connection string>
# DIRECT_URL=<supabase session pooler connection string, for migrations>

uv run alembic upgrade head
uv run uvicorn app.main:app --reload
```

Backend runs at `http://127.0.0.1:8000`. Docs at `http://127.0.0.1:8000/docs`.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at `http://localhost:5173`.

## Usage

1. Enter course codes (e.g. `CS010A`, `MATH009A`)
2. Select the term
3. Choose a primary ranking preference, and optionally secondary preferences
4. Click **Fetch Courses**
5. Use **Prev / Next** to browse alternate schedules, or **Copy CRNs** to paste into R'Web

## API

```
POST /schedule

{
  "courses": ["CS010A", "MATH009A"],
  "term_code": "202640",
  "primary": "earliest_end_time",
  "secondary": ["fewest_gaps"],
  "limit": 20
}
```

## License

MIT