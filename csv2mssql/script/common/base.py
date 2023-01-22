from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
##from sqlalchemy.orm.declarative import declarative_base

server = 'rick'
port = 1433
db = 'master'

cs = f'mssql+pymssql://{server}:{port}/{db}'
print(cs)

engine = create_engine(cs)

Base = declarative_base()
