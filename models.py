from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    fullname = Column(String(256))
    password = Column(String(256))
    gender = Column(String(256))
    
    def __init__(self, fullname):
        self.fullname = fullname


if __name__ == "__main__":
    engine = create_engine("mysql+pymysql://root:@localhost/test")

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    user1 = User(fullname="Amir")

    session.add(user1)
    session.commit()
    print("User was added")


