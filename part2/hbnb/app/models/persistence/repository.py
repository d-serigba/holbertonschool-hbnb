from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()


# ----------------- MODELS -----------------

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))


class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    description = Column(Text)


class Amenity(Base):
    __tablename__ = "amenities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    description = Column(Text)


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    text = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))
    place_id = Column(Integer, ForeignKey("places.id"))

    user = relationship("User")
    place = relationship("Place")


# ----------------- REPOSITORY -----------------

class SQLAlchemyRepository:

    def __init__(self):
        self.engine = create_engine("sqlite:///hbnb.db", echo=False)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add(self, obj):
        session = self.Session()
        session.add(obj)
        session.commit()
        session.refresh(obj)
        session.close()
        return obj

    def get_all(self, model_class):
        session = self.Session()
        objects = session.query(model_class).all()
        session.close()
        return objects

    def get(self, model_class, obj_id):
        session = self.Session()
        obj = session.query(model_class).filter_by(id=obj_id).first()
        session.close()
        return obj

    def update(self, model_class, obj_id, data):
        session = self.Session()
        obj = session.query(model_class).filter_by(id=obj_id).first()

        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            session.commit()
            session.refresh(obj)

        session.close()
        return obj

    def delete(self, model_class, obj_id):
        session = self.Session()
        obj = session.query(model_class).filter_by(id=obj_id).first()

        if obj:
            session.delete(obj)
            session.commit()
            session.close()
            return True

        session.close()
        return False
