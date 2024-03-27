from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
import app.models, app.schemas, app.utils, app.database

router = APIRouter(
    prefix="/users",
    tags = ['Users'])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=app.schemas.UserOut)
def create_user(user: app.schemas.UserCreate, db: Session = Depends(app.database.get_db)):

    #hash the password - user.password
    hashed_password = app.utils.hash(user.password)
    user.password = hashed_password

    new_user = app.models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get('/{id}', response_model = app.schemas.UserOut)
def get_user(id: int, db: Session = Depends(app.database.get_db)):
    user = db.query(app.models.User).filter(app.models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"User with id {id} does not exist")
    return user