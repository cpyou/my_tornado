from sqlalchemy import Column, String, Integer, VARCHAR,ForeignKey, Float
from sqlalchemy.orm import relationship,backref
from db import engine,Base


class Article(Base):
    __tablename__ = 'articles'
    user = Column(VARCHAR(20), primary_key=True)
    title = Column(VARCHAR(40))
    time = Column(VARCHAR(20))
    content = Column(VARCHAR(2000))
