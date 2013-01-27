from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Unicode
from geoalchemy import GeometryDDL, GeometryColumn, Polygon


Base = declarative_base()


class Region(Base):
    __tablename__ = 'regions'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode, nullable=False)
    area = GeometryColumn(Polygon(1))



GeometryDDL(Region.__table__)
