import databases
from fastapi import FastAPI, Request
import sqlalchemy
from decouple import config

DATABASE_URL = (f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@localhost:{config('DB_PORT')}/{config('DB_NAME')}")


database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# engine = sqlalchemy.create_engine(DATABASE_URL)
# metadata.create_all(engine)

# M O D E L S
books = sqlalchemy.Table(
    "books",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("author", sqlalchemy.String),
    sqlalchemy.Column("pages", sqlalchemy.Integer),
    # ForeingKey(NameOfTable) O2O
    #sqlalchemy.Column("reader_id", sqlalchemy.ForeignKey("readers.id"), nullable=False, index=True),

)

readers = sqlalchemy.Table(
    "readers",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
)

#M2M
readers_books = sqlalchemy.Table(
    "readers_books",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("book_id",sqlalchemy.ForeignKey("books.id"), nullable=False, index=True),
    sqlalchemy.Column("reader_id",sqlalchemy.ForeignKey("readers.id"), nullable=False, index=True),
)

app = FastAPI()

#Middleware
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# V I E W 

#BOOKS

@app.post("/books/")
async def create_books(request: Request):
    data = await request.json()
    #...(title = data.get("title"), author=data.get("author"))
    query = books.insert().values(**data)
    last_record_id = await database.execute(query)
    
    return {"id": last_record_id}

@app.get("/books/")
async def read_books():
    query = books.select()
    return await database.fetch_all(query)

#READERS 
@app.post("/readers/")
async def create_readers(request: Request):
    data = await request.json()
    #...(title = data.get("title"), author=data.get("author"))
    query = readers.insert().values(**data)
    last_record_id = await database.execute(query)
    
    return {"id": last_record_id}

@app.post("/read/")
async def read_book(request: Request):
    data = await request.json()
    query = readers_books.insert().values(**data)
    last_record_id = await database.execute(query)
    return {"id": last_record_id}