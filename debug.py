# debug.py

import ipdb
from database import Session
from models.company import Company
from models.dev import Dev
from models.freebie import Freebie

if __name__ == "__main__":
    session = Session()

    all_companies = session.query(Company).all()
    all_devs      = session.query(Dev).all()
    all_freebies  = session.query(Freebie).all()

    print(f"Found {len(all_companies)} companies, "
          f"{len(all_devs)} devs, {len(all_freebies)} freebies")

    #––– Pause here and drop into ipdb –––
    ipdb.set_trace()