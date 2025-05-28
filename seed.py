from database import Base, engine, Session
from models.company import Company
from models.dev import Dev

# ensuring every table exists
Base.metadata.create_all(bind=engine)

session = Session()

c1 = Company(name="ZoomCorp", founding_year=2010)
c2 = Company(name="HackCo",   founding_year=2005)

d1 = Dev(name="Alice")
d2 = Dev(name="Bob")

session.add_all([c1, c2, d1, d2])
session.commit()

# givong out freebies
c1.give_freebie(d1, "Sticker Pack", 0)
c1.give_freebie(d2, "T-shirt",      20)
c2.give_freebie(d1, "Mug",           10)

session.close()
print("✅ Seed complete")
