"""
SQLAlchemy models for users and validations.
Designed for SQLite, easy to upgrade to PostgreSQL.
"""

from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

DATABASE_URL = "sqlite:///data/ai_assistant.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    """User model with role-based access control."""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    role = Column(String, default="sysadmin")
    validations = relationship("Validation", back_populates="user")

    def is_admin(self):
        """Check if the user has admin privileges."""
        return self.role.lower() == "admin"

class Validation(Base):
    """Track each validation a user performs."""
    __tablename__ = "validations"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    guide_title = Column(String)
    step = Column(Text)
    response = Column(Text)
    valid = Column(Boolean)
    score = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="validations")

def init_db():
    """Create all tables in the database."""
    Base.metadata.create_all(bind=engine)
