import bcrypt
from sqlalchemy import Integer, Column, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.types import Text


Base = declarative_base()


class Owners(Base):
    __tablename__ = 'owners'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), unique=True)
    password_hash = Column(Text, nullable=False)
    password_salt = Column(String(50), nullable=False)

    def __repr__(self):
        return f'<{self.username})>'


    def set_password(self, password):
        self.password_salt = bcrypt.gensalt().decode('utf-8')
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), self.password_salt.encode('utf-8')).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))


class Website(Base):
    __tablename__ = 'website'

    id = Column(Integer, primary_key=True)
    heading = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    date_add = Column(DateTime, default=True, nullable=False)
    date_update = Column(DateTime, default=True, nullable=False)
    owner_id = Column(Integer, ForeignKey('owners.id'), nullable=False)
    owner = relationship('Owners', backref='website')

    def __repr__(self):
        return f'<{self.heading}>'
