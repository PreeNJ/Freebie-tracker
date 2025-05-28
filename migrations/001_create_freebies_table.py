from sqlalchemy import (
    MetaData, Table,
    Column, Integer, String, ForeignKey,
)
from database import engine

def run_migration():
    metadata = MetaData(bind=engine)
    
    Table(
        "freebies", metadata,
        Column("id", Integer, primary_key=True),
        Column("item_name", String),
        Column("value", Integer),
        Column("dev_id", Integer, ForeignKey("devs.id")),
        Column("company_id", Integer, ForeignKey("companies.id")),
    ).create(checkfirst=True)

if __name__ == "__main__":
    run_migration()
    print("✅ Created freebies table")
