from whocares.region import Region
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql:///nhs', echo=True)
session = sessionmaker(bind=engine)()

session.add_all([
    Region(name="R1", area="POLYGON((51.54 -1.8, 51.56 -1.84, 51.54 -1.84, 51.54 -1.8))"),
    Region(name="R2", area="POLYGON((51.55 -1.8, 51.59 -1.84, 51.57 -1.84, 51.55 -1.8))"),
    ])
session.commit()
