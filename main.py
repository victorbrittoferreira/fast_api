import databases
from fastapi import FastAPI, Request
import sqlalchemy

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/store"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

books = sqlalchemy.Table(
    "books",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("author", sqlalchemy.String),
    sqlalchemy.Column("pages", sqlalchemy.Integer),
    # ForeingKey(NameOfTable) O2O
    sqlalchemy.Column("reader_id", sqlalchemy.ForeignKey("readers.id"), nullable=False, index=True),

)

# engine = sqlalchemy.create_engine(DATABASE_URL)
# metadata.create_all(engine)

readers = sqlalchemy.Table(
    "readers",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
)




app = FastAPI()

#Middleware
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/books/")
async def read_books():
    query = books.select()
    return await database.fetch_all(query)

@app.post("/books/")
async def create_books(request: Request):
    data = await request.json()
    #...(title = data.get("title"), author=data.get("author"))
    query = books.insert().values(**data)
    last_record_id = await database.execute(query)
    
    return {"id": last_record_id}
    