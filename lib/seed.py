from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Role, Audition

if __name__ == '__main__':
    engine = create_engine('sqlite:///theaters.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Role).delete()
    session.query(Audition).delete()

    fake = Faker()
    
    for _ in range(5):
        role = Role(character_name = fake.name())
        session.add(role)
        session.commit()

        for _ in range(3):
            audition = Audition(
            actor = fake.name(), 
            location = fake.city(), 
            phone = fake.random_number(digits = 10, fix_len = True), 
            hired = fake.boolean(), 
            role_id = random.randint(1, 5)
        )
        session.add(audition)
    session.commit()


    # role1 = Role(character_name = 'Joey Tribianni')
    # role2 = Role(character_name = 'Chandler Bing')
    # session.add(role1)
    # session.add(role2)
    # session.commit()
    
    # audition1 = Audition(actor = 'Matt Le Blanc', location = 'New York', phone = 12345678, hired = True, role_id = role1.id)
    # audition2 = Audition(actor = 'Hank Azaria', location = 'Minsc', phone = 23456789, hired = False, role_id = role1.id)
    # audition3 = Audition(actor = 'Matthew Perry', location = 'Los Angeles', phone = 34567891, hired = True, role_id = role2.id)
    # session.add(audition1)
    # session.add(audition2)
    # session.add(audition3)
    # session.commit()
