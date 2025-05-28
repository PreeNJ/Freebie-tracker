from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, object_session
from database import Base, Session
from models.freebie import Freebie

class Company(Base):
    __tablename__ = "companies"

    id            = Column(Integer, primary_key=True)
    name          = Column(String)
    founding_year = Column(Integer)

    # —— Relationships ——
    freebies = relationship("Freebie", back_populates="company")
    devs = relationship(
        "Dev",
        secondary="freebies",
        back_populates="companies",
        viewonly=True
    )

    # —— Aggregate / Association methods ——

    def give_freebie(self, dev, item_name, value):
        """
        4 pts: creates & returns a new Freebie tied to this company + the given dev.
        Reuses the existing session to avoid cross‐session errors.
        """
        # grab the session already managing this Company (fallback to a new one)
        session = object_session(self) or Session()
        # merge the Dev into that same session
        dev = session.merge(dev)

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
        4 pts: returns the Company instance with the earliest founding_year.
        """
        session = Session()
        return session.query(cls).order_by(cls.founding_year).first()
