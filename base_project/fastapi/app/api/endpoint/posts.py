from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.models import Post, Board, User
from app.schemas.models import PostCreate, PostResponse, PostUpdate, Pagination
from app.utils.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=PostResponse)
def create_post(post: PostCreate, board_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_board = db.query(Board).filter(Board.id == board_id).first()
    if not db_board or (not db_board.public and db_board.owner_id != current_user.id):
        raise HTTPException(status_code=403, detail="Not authorized to create post in this board")
    db_post = Post(title=post.title, content=post.content, board_id=board_id, owner_id=current_user.id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@router.put("/{post_id}", response_model=PostResponse)
def update_post(post_id: int, post: PostUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    if db_post.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this post")
    db_post.title = post.title or db_post.title
    db_post.content = post.content or db_post.content
    db.commit()
    db.refresh(db_post)
    return db_post

@router.delete("/{post_id}")
def delete_post(post_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    if db_post.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this post")
    db.delete(db_post)
    db.commit()
    return {"message": "Post deleted successfully"}

@router.get("/{post_id}", response_model=PostResponse)
def get_post(post_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    db_board = db.query(Board).filter(Board.id == db_post.board_id).first()
    if not db_board.public and db_post.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to view this post")
    return db_post

@router.get("/", response_model=Pagination)
def list_posts(board_id: int, page: int = 1, size: int = 10, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_board = db.query(Board).filter(Board.id == board_id).first()
    if not db_board or (not db_board.public and db_board.owner_id != current_user.id):
        raise HTTPException(status_code=403, detail="Not authorized to view posts in this board")
    skip = (page - 1) * size
    query = db.query(Post).filter(Post.board_id == board_id)
    total = query.count()
    posts = query.offset(skip).limit(size).all()
    return Pagination(total=total, page=page, size=size, items=posts)
