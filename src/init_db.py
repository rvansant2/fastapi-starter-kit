# Initialize database for local development

from app.database.session import engine
from app.database.connection import Base

def init_db():
    """Create all database tables."""
    print(f"Initializing the database and creating all tables...")
    Base.metadata.create_all(bind=engine)
    print(f"Database initialization complete.")

if __name__ == "__main__":
    init_db()