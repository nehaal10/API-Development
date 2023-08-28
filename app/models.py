'''All the tables information is stored here'''
from .database import Base
from sqlalchemy import Boolean,Integer, Column, String
from sqlalchemy.sql.expression import text 
from sqlalchemy.sql.sqltypes import TIMESTAMP


class PostTable(Base):
    __tablename__= 'posts'

    id = Column(Integer,primary_key = True,nullable = False,server_default = text("nextval('posts_id_seq'::regclass)"))
    title = Column(String,nullable = False)
    content = Column(String,nullable = False)
    published = Column(Boolean,server_default = 'True',nullable = False)
    created_at = Column(TIMESTAMP(timezone = True),server_default = text('now()'),nullable = False)


class UserTable(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key = True,nullable = False,server_default = text("nextval('posts_id_seq'::regclass)")) 
    email = Column(String,nullable = False,primary_key = True)
    password = Column(String,nullable = False)
    created_at = Column(TIMESTAMP(timezone = True),server_default = text('now()'),nullable = False)



