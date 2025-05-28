from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Freebie(Base):
    __tablename__ = "freebies"

    id         = Column(Integer, primary_key=True)
    item_name  = Column(String)
    value      = Column(Integer)
    dev_id     = Column(Integer, ForeignKey("devs.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))

    dev     = relationship("Dev",     back_populates="freebies")
    company = relationship("Company", back_populates="freebies")

    def print_details(self):
        """
        dev name owns a item_name from company name
        """
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"
