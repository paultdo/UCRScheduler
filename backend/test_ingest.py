from app.database import get_db
from app.ingestion.ingest import ingest_subject

db = next(get_db())

ingest_subject(db, "BIOL", "202640")
ingest_subject(db, "WRIT", "202640")
ingest_subject(db, "EE", "202640")
ingest_subject(db, "HNPG", "202640")


