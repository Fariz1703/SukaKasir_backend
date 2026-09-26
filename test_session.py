from sqlalchemy import text

from database.database import SessionLocal


db = SessionLocal()

try:
    result = db.execute(text("SELECT 1"))
    print(result.scalar())
finally:
    db.close()