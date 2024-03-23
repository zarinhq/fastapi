from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

##Mandatory fields while creating the posts
class PostCreate(PostBase):
    pass

##data that user gets- response model
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True

## data that user gets after creating the posts
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int 
    owner: UserOut

    class Config:
        orm_mode = True

## After joining the response model of the post
class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True

##Mandatory fields while creating users
class UserCreate(BaseModel):
    email: EmailStr
    password: str

## User login detail validation
class UserLogin(BaseModel):
    email: EmailStr
    password: str

##schema for access_token
class Token(BaseModel):
    access_token: str
    token_type: str

##Schema for the data embedded into our access token
class TokenData(BaseModel):
    id: Optional[int] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1) 



     