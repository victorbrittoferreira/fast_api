import databases
import sqlalchemy

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/store"

data = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

books = sqlalchemy.Table(
    "books",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("author", sqlalchemy.String),
)