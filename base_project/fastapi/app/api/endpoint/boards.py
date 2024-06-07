from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.models import Board, User
from app.schemas.models import BoardCreate, BoardResponse, Pagination
from app.utils.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=BoardResponse)
def create_board(board: BoardCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_board = Board(name=board.name, public=board.public, owner_id=current_user.id)
    db.add(db_board)
    db.commit()
    db.refresh(db_board)
    return db_board

@router.put("/{board_id}", response_model=BoardResponse)
def update_board(board_id: int, board: BoardCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_board = db.query(Board).filter(Board.id == board_id).first()
    if not db_board:
        raise HTTPException(status_code=404, detail="Board not found")
    if db_board.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this board")
    db_board.name = board.name
    db_board.public = board.public
    db.commit()
    db.refresh(db_board)
    return db_board

@router.delete("/{board_id}")
def delete_board(board_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_board = db.query(Board).filter(Board.id == board_id).first()
    if not db_board:
        raise HTTPException(status_code=404, detail="Board not found")
    if db_board.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this board")
    db.delete(db_board)
    db.commit()
    return {"message": "Board deleted successfully"}

@router.get("/{board_id}", response_model=BoardResponse)
def get_board(board_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_board = db.query(Board).filter(Board.id == board_id).first()
    if not db_board:
        raise HTTPException(status_code=404, detail="Board not found")
    if not db_board.public and db_board.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to view this board")
    return db_board

@router.get("/", response_model=Pagination)
def list_boards(page: int = 1, size: int = 10, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    skip = (page - 1) * size
    query = db.query(Board).filter((Board.public == True) | (Board.owner_id == current_user.id))
    total = query.count()
    boards = query.offset(skip).limit(size).all()
    return Pagination(total=total, page=page, size=size, items=boards)
