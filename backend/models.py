from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text
from backend.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    title = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, default="")
    github = Column(String, default="")
    linkedin = Column(String, default="")
    bio = Column(Text, default="")


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    order_index = Column(Integer, default=0)


class Experience(Base):
    __tablename__ = "experiences"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    location = Column(String, default="")
    start_date = Column(String, nullable=False)
    end_date = Column(String, default="Present")
    description = Column(Text, default="")
    highlights = Column(Text, default="")
    order_index = Column(Integer, default=0)


class Education(Base):
    __tablename__ = "education"

    id = Column(Integer, primary_key=True, index=True)
    degree = Column(String, nullable=False)
    institution = Column(String, nullable=False)
    location = Column(String, default="")
    start_date = Column(String, nullable=False)
    end_date = Column(String, nullable=False)
    details = Column(Text, default="")
    order_index = Column(Integer, default=0)


class Achievement(Base):
    __tablename__ = "achievements"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    organization = Column(String, nullable=False)
    year = Column(String, nullable=False)
    description = Column(Text, default="")
    order_index = Column(Integer, default=0)
