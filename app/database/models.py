from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker
from settings import URL, ECHO

engine = create_engine(url=URL, echo=ECHO)

Session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass


class User(Base):
    tablename = 'user'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int]
    balance: Mapped[float]


class Item(Base):
    tablename = 'item'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    desc: Mapped[str] = mapped_column(String(512))
    owner: Mapped[int] = mapped_column(ForeignKey('user.id'))
    price: Mapped[float]


Base.metadata.create_all(bind=engine)