from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, object_session
from database import Base, Session

class Dev(Base):
    __tablename__ = "devs"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    freebies = relationship("Freebie", back_populates="dev")
    companies = relationship("Company", secondary="freebies", back_populates="devs", viewonly=True)

    def received_one(self, item_name):
        return any(fb.item_name == item_name for fb in self.freebies)

    def give_away(self, new_dev, freebie):
        if freebie not in self.freebies:
            return False
        session = object_session(self) or Session()
        new_dev = session.merge(new_dev)
        freebie = session.merge(freebie)
        freebie.dev = new_dev
        session.add(freebie)
        session.commit()
        return True

    def __repr__(self):
        return f"<Dev id={self.id!r} name={self.name!r}>"
