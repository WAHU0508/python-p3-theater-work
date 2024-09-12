from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Boolean, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)
engine = create_engine('sqlite:///theaters.db')
Session = sessionmaker(bind=engine)
session = Session()

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer(), primary_key = True)
    character_name = Column(String())

    auditions = relationship('Audition', backref = backref('role'))

    def __repr__(self):
        return f'Role(id={self.id}, ' + \
            f'character_name={self.character_name})'

    def actors(self):
        return [audition.actor for audition in self.auditions]
    
    def locations(self):
        return [audition.location for audition in self.auditions]
    
    def lead(self):
        query = session.query(Audition).filter(Audition.hired == True, Audition.role_id == self.id).first()
        if query:
            return query
        else:
            return 'No actor has been hired for this role.'
    def understudy(self):
        query = session.query(Audition).filter(Audition.hired == True, Audition.role_id == self.id).all()
        if len(query) >= 2:
            return query[1]
        else:
            return 'No actor has been hired for understudy for this role.'
class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer(), primary_key = True)
    actor = Column(String())
    location = Column(String())
    phone = Column(Integer())
    hired = Column(Boolean())

    role_id = Column(Integer(), ForeignKey('roles.id'))

    def call_back(self):
        if self.hired == False:
            self.hired = True
            session.commit()

    def __repr__(self):
        return f'Audition(id={self.id}, ' + \
            f'actor={self.actor}, ' + \
            f'location={self.location}, ' + \
            f'phone={self.phone}, ' + \
            f'hired={self.hired})'