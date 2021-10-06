from GDSC.database import Base
from sqlalchemy import Column, String, Integer

class User(Base):
    __tablename__ = "user"
    
    no = Column(Integer, primary_key=True, index=True)
    id = Column(String(20), comment="아이디")
    password = Column(String, comment="비밀번호")
    name = Column(String, comment="이름", nullable=True)
    