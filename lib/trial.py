from datetime import datetime
from sqlalchemy import( Column,Integer,String,create_engine,DateTime,CheckConstraint,PrimaryKeyConstraint,UniqueConstraint)
from sqlalchemy.orm import declarative_base,sessionmaker



base=declarative_base()

class Animal(base):
    # we create the table names and colums
    __tablename__="animals"
    # we create the contrains

# we crete the class aTTRIBUTES
    id=Column(Integer,primary_key=True)
    name=Column(String(50))
    breed=Column(String(50))
    age=Column(Integer())
  

    def __repr__(self):
        return f"animal {self.id}: " \
            + f"{self.name}, " \
            + f"breed  {self.breed}"

 



if __name__=="__main__":
    # we create a connetion to the memory to store the table data 
    engine=create_engine("sqlite:///:memory:")
    try:
        base.metadata.create_all(engine)
    except Exception as e:
        print("encounted this error", str(e))
# we create a session for the transactions 
    Session=sessionmaker(bind=engine)
    session=Session()

    dog=Animal(name="jamie",age=23,breed="rotwailer")
    hyene=Animal(name="hyene",age=1,breed="scavanger")
    cat=Animal(name="tweety",age=2,breed="black")

    session.add_all([dog,hyene,cat])
    session.commit()

    for animal in session.query(Animal):
        print(Animal)
    try:
        for filtered in session.query(Animal).filter(Animal.name=="jamie"):
            print(filtered)

    except Exception as e:
        print("we got this error", str(e))   