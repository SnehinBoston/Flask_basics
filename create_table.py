from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///:memory:', echo = True)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name = "John Doe", age = 30)
session.add(new_user)
session.commit()

user = session.query(User).filter_by(name="John Doe").first()
print(f'User: {user.name}, Age: {user.age}')
