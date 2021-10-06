from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from GDSC import database, schemas
from GDSC.repository import user_re

router = APIRouter(
    prefix='/user',
    tags=['User'],
)

get_db = database.get_db

# 로그인 정보를 보내고, 성공여부를 받는 라우터
@router.get('/', response_model=schemas.User)
def sign_in(id: str, password: str, db: Session=Depends(get_db)):
    return user_re.signin(id=id, password=password, db=db)

# 회원가입 정보를 보내고, 성공여부를 받는 라우터
@router.post('/')
def sign_up(id: str, password: str, name: str, db: Session=Depends(get_db)):
    return user_re.signup(id=id, password=password, name=name, db=db)