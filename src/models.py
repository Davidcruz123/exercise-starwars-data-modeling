import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class LogIn(Base):
    __tablename__ = 'log_In'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    last_name = Column(String(250))
    user_name = Column(String(250),unique=True)
    email=Column(String(250),unique=True)
    password=Column(String(100))

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    data_type = Column(String(250))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    user_id = Column(Integer, ForeignKey('log_In.id'))

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    description = Column(String(550))
    hair_color = Column(String(30))
    skin_color = Column(String(30))
    eye_color = Column(String(30))
    gender = Column(String(30))
    name = Column(String(30))
    planet_origin = Column(String(30))
    picture_url = Column(String(200))
    height=Column(Integer)
    mass=Column(Integer)
    birth_year=Column(Date)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    description = Column(String(550))
    climate = Column(String(30))
    gravity = Column(String(30))
    name = Column(String(30))
    terrain = Column(String(30))
    picture_url = Column(String(200))
    diameter=Column(Integer)
    rotation_period=Column(Integer)
    orbital_period=Column(Integer)
    population=Column(Integer)
    surface_water=Column(Integer)
    
   

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')