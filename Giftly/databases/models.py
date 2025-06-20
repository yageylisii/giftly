from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger)
    name: Mapped[str]
    user_name: Mapped[str]
    referal_amount: Mapped[int] = mapped_column(BigInteger, default=0)
    time_register: Mapped[int]
    balance_star: Mapped[int] = mapped_column(BigInteger, default=0)
    play_win: Mapped[int] = mapped_column(default=0)
    referals: Mapped[int] = mapped_column(default=0)
    referer: Mapped[int] = mapped_column(BigInteger)
class Gifts(Base):
    __tablename__ = 'Gifts'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    rarity: Mapped[str]
    owned_id: Mapped[str]

class Deposit_TON(Base):
    __tablename__ = 'Ton_DEP'

    id: Mapped[int] = mapped_column(primary_key=True)
    wallet_name: Mapped[str]
    busy: Mapped[bool]
    user_id: Mapped[int]
    last_hash: Mapped[str]
