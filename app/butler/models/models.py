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
    created_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    creator = relationship('User', back_populates="clients") 
    modified_at = Column(DateTime)
    modified_by = Column(Integer)
    client_type_id = Column(Integer, ForeignKey('client_type.id'))
    client_type = relationship('ClientType', back_populates="clients")
    bills = relationship('Bill', back_populates='client')
    reservations = relationship('Reservation', back_populates='client')
    

class ClientType(database.Base):
    __tablename__ = 'client_type'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    clients = relationship('Client', back_populates='client_type')
    created_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    modified_at = Column(DateTime)
    modified_by = Column(Integer)
    
    

class Space(database.Base):
    __tablename__ = 'space'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    price = Column(Float)
    comments = Column(String)
    space_type_id = Column(Integer, ForeignKey('space_type.id'))
    space_type = relationship('SpaceType', back_populates="spaces")
    space_state_id = Column(Integer, ForeignKey('space_state.id'))
    space_state = relationship('SpaceState', back_populates="spaces")
    reservations = relationship('Reservation', back_populates='space')
    created_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id')) 
    modified_at = Column(DateTime)
    modified_by = Column(Integer)
    
    

class SpaceType(database.Base):
    __tablename__ = 'space_type'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    spaces = relationship('Space', back_populates='space_type')
    created_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    modified_at = Column(DateTime)
    modified_by = Column(Integer)
    
    

class SpaceState(database.Base):
    __tablename__ = 'space_state'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    spaces = relationship('Space', back_populates='space_state')
    created_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    modified_at = Column(DateTime)
    modified_by = Column(Integer)
    
    

class Reduction(database.Base):
    __tablename__ = 'reduction'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    rate = Column(Float)
    reservations = relationship('Reservation', back_populates='reduction')
    created_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id')) 
    modified_at = Column(DateTime)
    modified_by = Column(Integer)
    
    

class Reservation(database.Base):
    __tablename__ = 'reservation'
    id = Column(Integer, primary_key=True, index=True)
    begin_date = Column(DateTime)
    end_date = Column(DateTime)
    comments = Column(String)
    reservation_state = Column(String)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship('Client', back_populates="reservations")
    space_id = Column(Integer, ForeignKey('space.id'))
    space = relationship('Space', back_populates="reservations")
    reduction_id = Column(Integer, ForeignKey('reduction.id'))
    reduction = relationship('Reduction', back_populates="reservations")
    to_bills = relationship('ToBill', back_populates="reservation")
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    modified_by = Column(Integer)
    
    

class Bill(database.Base):
    __tablename__ = 'bill'
    id = Column(Integer, primary_key=True, index=True)
    b_date = Column(DateTime)
    b_num = Column(String)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship('Client', back_populates="bills")
    to_bills = relationship('ToBill', back_populates="bill")
    created_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id')) 
    modified_at = Column(DateTime)
    modified_by = Column(Integer)
    
    

class ToBill(database.Base):
    __tablename__ = 'to_bill'
    id = Column(Integer, primary_key=True, index=True)
    tb_date = Column(DateTime)
    tb_num = Column(String)
    amount_to_be_paid = Column(Float)
    bill_id = Column(Integer, ForeignKey('bill.id'))
    bill = relationship('Bill', back_populates="to_bills")
    reservation_id = Column(Integer, ForeignKey('reservation.id'))
    reservation = relationship('Reservation', back_populates="to_bills")
    created_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    modified_at = Column(DateTime)
    modified_by = Column(Integer)
    
    

class User(database.Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    role_id = Column(Integer, ForeignKey('role.id'))
    role = relationship('Role', back_populates="users")
    clients = relationship('Client', back_populates='creator')
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    

class Role(database.Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    users = relationship('User', back_populates='role')
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    
