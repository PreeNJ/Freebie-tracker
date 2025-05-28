from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, object_session
from database import Base, Session

class Dev(Base):
    __tablename__ = "devs"

    id   = Column(Integer, primary_key=True)
    name = Column(String)

    # —— Relationships ——
    freebies = relationship("Freebie", back_populates="dev")
    companies = relationship(
        "Company",
        secondary="freebies",
        back_populates="devs",
        viewonly=True
    )

    # —— Aggregate / Association methods ——

    def received_one(self, item_name):
        """
        4 pts: return True if any of this Dev's freebies
        has item_name == the argument, otherwise False.
        """
        return any(fb.item_name == item_name for fb in self.freebies)

    def give_away(self, new_dev, freebie):
        """
        4 pts: change freebie.dev to new_dev,
        but only if self currently owns that freebie.
        Returns True on success, False otherwise.
        """
        if freebie not in self.freebies:
            return False

        # reuse the session managing this Dev (fallback to new)
        session = object_session(self) or Session()
        # merge both into that session
        new_dev = session.merge(new_dev)
        freebie = session.merge(freebie)

        freebie.dev = new_dev
        session.add(freebie)
        session.commit()
        return True
