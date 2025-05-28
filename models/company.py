from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base, Session
from models.freebie import Freebie

class Company(Base):
    __tablename__ = "companies"

    id            = Column(Integer, primary_key=True)
    name          = Column(String)
    founding_year = Column(Integer)

    freebies = relationship("Freebie", back_populates="company")
    # using the freebies join table to reach Dev
    devs = relationship(
        "Dev",
        secondary="freebies",
        back_populates="companies",
        viewonly=True
    )

    

    def give_freebie(self, dev, item_name, value):
        """
         creates & returns a new Freebie tied to this company an the given dev
        """
        session = Session()
        fb = Freebie(
            item_name=item_name,
            value=value,
            dev=dev,
            company=self
        )
        session.add(fb)
        session.commit()
        return fb

    @classmethod
    def oldest_company(cls):
        """
          returns the Company with the smallest founding_year
        """
        session = Session()
        return session.query(cls).order_by(cls.founding_year).first()
