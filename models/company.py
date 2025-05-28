from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, object_session
from database import Base, Session
from models.freebie import Freebie

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    founding_year = Column(Integer)

    freebies = relationship("Freebie", back_populates="company")
    devs = relationship("Dev", secondary="freebies", back_populates="companies", viewonly=True)

    def give_freebie(self, dev, item_name, value):
        session = object_session(self) or Session()
        dev = session.merge(dev)
        fb = Freebie(item_name=item_name, value=value, dev=dev, company=self)
        session.add(fb)
        session.commit()
        return fb

    @classmethod
    def oldest_company(cls):
        session = Session()
        return session.query(cls).order_by(cls.founding_year).first()

    def __repr__(self):
        return f"<Company id={self.id!r} name={self.name!r}>"
