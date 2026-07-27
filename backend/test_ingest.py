from app.database import get_db
from app.ingestion.ingest import ingest_subject

db = next(get_db())

ingest_subject(db, "CS", "202640")


