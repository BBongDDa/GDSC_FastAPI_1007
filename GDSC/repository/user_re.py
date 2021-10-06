# 실제로 로직이 돌아가는걸 만드는 곳입니다.
from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from GDSC import models


def signin(id: str, password: str, db: Session):
    # ID가 맞는 사람 찾기
    find_user = db.query(models.User).filter(models.User.id == id).first()
    
    if not find_user:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="그런 아이디 없는데?"
        ) "아이디 오류"
    
    # Password도 맞는지 봐야지?
    if find_user.password != password:
        return HTTPException(
            status_code=400,
            detail="비밀번호 틀렸던데?"
        )
    
    return find_user


def signup(id: str, password: str, name: str, db: Session):
    new_user = models.User(
        id=id,
        password=password,
        name=name
    )
    db.add(new_user) # 추가만
    db.commit() # 저장버튼
    return "GDSC 회원가입을 축하합니다."