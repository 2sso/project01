from sqlalchemy import create_engine

DB_URL = "mysql+pymysql://root:rootpass@db:3306/mydb"


engine = create_engine(DB_URL)

def get_connection():
    return engine.connect()

