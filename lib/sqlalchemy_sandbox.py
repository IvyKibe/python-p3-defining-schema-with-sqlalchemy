#!/usr/bin/env python3

from  datetime import  datetime
from sqlalchemy import (Column, Integer, String, create_engine,
         desc,PrimaryKeyConstraint,DateTime,UniqueConstraint,CheckConstraint,Index)

from sqlalchemy.orm import sessionmaker,declarative_base

Base = declarative_base()




class Student(Base):
    __tablename__= 'students'

    __tableargs__=(
        PrimaryKeyConstraint("id",name="id_pk"),
        UniqueConstraint("emal", name="unique_email"),
        CheckConstraint("grade BETWEEN 1 AND 12",name="grade_between_1_and_12"))


    Index('index_name','name')

    id=Column(Integer(),primary_key=True)
    name=Column(String())
    email=Column(String(55))
    grade=Column(String())
    birthday=Column(DateTime())
    enrolled_date=Column(DateTime(),default=datetime.now())

    def __repr__(self):
       return f"Student {self.id}: " \
            + f"{self.name}, " \
            + f"Grade {self.grade}"

    
    
    # this is a model class 

if __name__ == '__main__':
    # data  models

    engine=create_engine("sqlite:///:memory:")
    try:
        Base.metadata.create_all(engine)
        print("Table was created Successfully",Student.__tablename__)
    except Exception as e:
        print("an error occured:",str(e))  

    Session=sessionmaker(bind=engine)  
    session=Session()  
     
    albert =Student(name="Albert Einstein",
        email="albert.einstein@zurich.edu",
        grade=6,
        birthday=datetime(
            year=1879,
            month=3,
            day=14)) 
    alan_turing = Student(
        name="Alan Turing",
        email="alan.turing@sherborne.edu",
        grade=11,
        birthday=datetime(
            year=1912,
            month=6,
            day=23
        ),
    )

    Harry_thuku = Student(
        name="Harry Thuku",
        email="Harrythuku@sherborne.edu",
        grade=11,
        birthday=datetime(
            year=1970,
            month=12,
            day=9
        ),
    )
    
    session.bulk_save_objects([albert,alan_turing])
    session.commit()
    students=session.query(Student).all()
    # below is for returning a student 
    for student in students:
        print(student)
    print(f"new student id is {albert.email}")


    # selecting only certain columns 

    names=[name for name in session.query(Student.name)]
    print(names)

    # orrdering
    student_by_name=[student for student in session.query(Student.name).order_by(Student.name)]
    print(student_by_name)

    #ordering by descending order 
    student_by_grade_desc=[student for student in session.query(Student.grade).order_by(desc(Student.grade))]
    print(student_by_grade_desc)

    # limiting 
    oldest_student=[student for student in session.query(Student.name,Student.birthday).order_by(desc(Student.grade)).first()]
    print(oldest_student)

    #    query for deleting an instance in the database 

    harry_thuku=session.query(Student.name).filter(Student.name=="Alan Turing")
    query=harry_thuku.first()
    session.delete(query)
    session.commit()