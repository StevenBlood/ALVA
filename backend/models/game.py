import os
import sys
from sqlalchemy import Column, Integer, String, Float, CheckConstraint, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    released = Column(String, nullable=False)

    platform_id = Column(Integer, ForeignKey("platforms.id"), nullable=False)
    publisher_id = Column(Integer, ForeignKey("publishers.id"), nullable=True)
    developer_id = Column(Integer, ForeignKey("developers.id"), nullable=True)

    category1_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category2_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    agerating_id = Column(Integer, ForeignKey("ageratings.id"))

    platform = relationship("Platform")
    publisher = relationship("Publisher")
    developer = relationship("Developer")

    category1 = relationship("Category", foreign_keys=[category1_id])
    category2 = relationship("Category", foreign_keys=[category2_id])
    agerating = relationship("AgeRating")

class Publisher(Base):
    __tablename__ = "publishers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    founded = Column(String, nullable=False)

class Developer(Base):
    __tablename__ = "developers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    members = Column(String, nullable=True)
    isindie = Column(String, nullable=False)

    __table_args__ = (
        CheckConstraint(isindie.in_(['igen', 'nem']), name='indie_igen_nem'),
        )

class Platform(Base):
    __tablename__ = "platforms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True, unique=True)
    released = Column(String, nullable=True) #PC esetén nincs gyártási év
    manufacturer_id = Column(Integer, ForeignKey("manufacturers.id"), nullable=True) #gyártó sincs...

class Manufacturer(Base):
    __tablename__= "manufacturers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable = False, index=True, unique=True)
    founded = Column(String, nullable=False)

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True, unique=True)

class AgeRating(Base):
    __tablename__ = "ageratings"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(String, nullable=False, index=True, unique=True)

    # Ha nagyon leakarnám zárni európai (PEGI) besorolásra:
    #
    # value = Column(Integer, nullable=False, index=True, unique=True)
    # __table_args__ = (CheckConstraint(value.in_([3, 7, 12, 16, 18]), name='korhatarbesorolasok'))



#adatbázis seeding

DB_FILE = "games.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_FILE}" 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def seed_database():

    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
        print(f"{DB_FILE} ha volt is már nincs.")

    Base.metadata.create_all(bind=engine)
    print("Táblák most már vannak")

    db = SessionLocal()
    try:
        print("Feltöltééééés")

        # Manufacturer
        manu_sony = Manufacturer(name="Sony", founded="1993")
        manu_microsoft = Manufacturer(name="Microsoft", founded="1975")
        manu_nintendo = Manufacturer(name="Nintendo", founded="1889")
        
        # Publisher & Developer
        pub_capcom = Publisher(name="Capcom", founded="1979")
        pub_bandainamco = Publisher(name="Bandai Namco", founded="2005")
        pub_nintendo = Publisher(name="Nintendo", founded="1889")

        dev_fromsoft = Developer(name="FromSoftware", members="300", isindie="nem")
        
        # Categories
        cat_horror = Category(name="Horror")
        cat_action = Category(name="Action")
        
        # AgeRatings
        pegi18 = AgeRating(value='18') 
        pegi16 = AgeRating(value='16')
        
        db.add_all([manu_sony, pub_capcom, dev_fromsoft, cat_horror, cat_action, pegi18, pegi16])
        db.commit() 


        # Platforms
        plat_ps5 = Platform(
            name="PlayStation 5", 
            released="2020", 
            manufacturer_id=manu_sony.id
        )
        plat_pc = Platform(
            name="PC", 
            released=None,        
            manufacturer_id=None 
        )
        db.add_all([plat_ps5, plat_pc])
        db.commit() 


        # Games
        game1 = Game(
            name="Resident Evil 4 Remake",
            released="2023",
            platform_id=plat_ps5.id,
            publisher_id=pub_capcom.id,
            developer_id=pub_capcom.id,
            category1_id=cat_horror.id,
            category2_id=cat_action.id,
            agerating_id=pegi18.id
        )

        game2 = Game(
            name="Elden Ring",
            released="2022",
            platform_id=plat_pc.id,
            publisher_id=None, 
            developer_id=dev_fromsoft.id,
            category1_id=cat_action.id,
            category2_id=None,
            agerating_id=pegi16.id
        )
        
        db.add_all([game1, game2])
        db.commit()
        print("Minden adat sikeresen feltöltve.")

    except Exception as e:
        db.rollback()
        print(f"\n[HIBA] Hiba történt a feltöltés során. Visszavonás. Hibaüzenet: {e}")
    finally:
        db.close()
        print("\nAdatbázis feltöltési folyamat befejezve.")

if __name__ == "__main__":
    seed_database()