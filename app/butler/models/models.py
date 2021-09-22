from sqlalchemy.sql.schema import ForeignKey
from butler.database import database
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

class Client(database.Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String) 
    nationality = Column(String) 
    id_card_num = Column(String) 
    phone = Column(String) 
    birth_date = Column(String) 
    under_cover = Column(String) 
    comments = Column(String) 
    email = Column(String) 
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship('User', back_populates="client") 
    client_type_id = Column(Integer, ForeignKey('client_type.id'))
    client_type = relationship('ClientType', back_populates="client")
    bills = relationship('Bill', back_populates='client')
    reservations = relationship('Reservation', back_populates='client')

class ClientType(database.Base):
    __tablename__ = 'client_type'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    clients = relationship('Client', back_populates='client_type')

class Space(database.Base):
    __tablename__ = 'space'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    price = Column(Float)
    comments = Column(String)
    space_type_id = Column(Integer, ForeignKey('space_type.id'))
    space_type = relationship('SpaceType', back_populates="space")
    space_state_id = Column(Integer, ForeignKey('space_state.id'))
    space_state = relationship('SpaceState', back_populates="space")
    reservations = relationship('Reservation', back_populates='space')

class SpaceType(database.Base):
    __tablename__ = 'space_type'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    spaces = relationship('Space', back_populates='space_type')

class SpaceState(database.Base):
    __tablename__ = 'space_state'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    spaces = relationship('Space', back_populates='space_state')

class Reduction(database.Base):
    __tablename__ = 'reduction'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    rate = Column(Float)
    reservations = relationship('Reservation', back_populates='reduction')

class Reservation(database.Base):
    __tablename__ = 'reservation'
    id = Column(Integer, primary_key=True, index=True)
    begin_date = Column(DateTime)
    end_date = Column(DateTime)
    comments = Column(String)
    reservation_state = Column(String)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship('Client', back_populates="reservation")
    space_id = Column(Integer, ForeignKey('space.id'))
    space = relationship('Space', back_populates="reservation")
    reduction_id = Column(Integer, ForeignKey('reduction.id'))
    reduction = relationship('Reduction', back_populates="reservation")

class Bill(database.Base):
    __tablename__ = 'bill'
    id = Column(Integer, primary_key=True, index=True)
    b_date = Column(DateTime)
    b_num = Column(String)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship('Client', back_populates="bill")

class ToBill(database.Base):
    __tablename__ = 'to_bill'
    id = Column(Integer, primary_key=True, index=True)
    tb_date = Column(DateTime)
    tb_num = Column(String)
    amount_to_be_paid = Column(Float)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship('Client', back_populates="to_bill")
    bill_id = Column(Integer, ForeignKey('bill.id'))
    bill = relationship('Bill', back_populates="to_bill")
    reservation_id = Column(Integer, ForeignKey('reservation.id'))
    reservation = relationship('Reservation', back_populates="to_bill")
    
class User(database.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship('Blog', back_populates='creator')
