from sqlalchemy import Column, String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import relationship
from .database import Base, engine

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fullname = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)

class Board(Base):
    __tablename__ = "boards"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    public = Column(Boolean, default=True)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    posts = relationship("Post", back_populates="board")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    board_id = Column(Integer, ForeignKey('boards.id'), nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    board = relationship("Board", back_populates="posts")

Base.metadata.create_all(engine)
