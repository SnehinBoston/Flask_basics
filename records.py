from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert, select
engine = create_engine('sqlite:///:memory:', echo=True)
metadata = MetaData()
users_table = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
)
metadata.create_all(engine)
with engine.connect() as connection:
    insert_stmt = users_table.insert().values(name="John Doe", age=30)
    connection.execute(insert_stmt)

with engine.connect() as connection:
    select_stmt = select(users_table).where(users_table.c.name == "John Doe")
    result = connection.execute(select_stmt)

with engine.connect() as connection:
    select_stmt = select(users_table).where(users_table.c.name == "John Doe")
    result = connection.execute(select_stmt)
    user = result.fetchone()
    print(f"User: {user.name}, Age: {user.age}")