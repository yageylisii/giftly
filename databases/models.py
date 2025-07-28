from sqlalchemy import BigInteger, Table, Column, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass

task_users = Table(
    "task_users",
    Base.metadata,
    Column("task_id", ForeignKey("tasks.id"), primary_key=True),
    Column("user_id", ForeignKey("Users.user_id"), primary_key=True)
)

class User(Base):
    __tablename__ = 'Users'

    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str]
    user_name: Mapped[str]
    referal_amount: Mapped[int] = mapped_column(BigInteger, default=0)
    time_register: Mapped[int]
    count_win: Mapped[int] = mapped_column(default=0)
    balance_star: Mapped[int] = mapped_column(BigInteger, default=0)
    play_win: Mapped[int] = mapped_column(default=0)
    referals: Mapped[int] = mapped_column(default=0)
    bet_casino: Mapped[int] = mapped_column(default=25)

    referer: Mapped[int] = mapped_column(BigInteger)
    tasks: Mapped[list["Tasks"]] = relationship(
        secondary=task_users,
        back_populates="users",
        lazy="selectin"
    )
class Gifts(Base):
    __tablename__ = 'Gifts'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    rarity: Mapped[str]
    owned_id: Mapped[str]

class Deposit_TON(Base):
    __tablename__ = 'Ton_DEP'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    TON_count: Mapped[int] = mapped_column(default=0)
    star_count: Mapped[int] = mapped_column(default=0)

class Tasks(Base):
    __tablename__ = 'tasks'

    users: Mapped[list["User"]] = relationship(
        secondary=task_users,
        back_populates="tasks",
        lazy="selectin"
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(500))
    bonus: Mapped[int]
    name: Mapped[str]
    official_name: Mapped[str]
    completed: Mapped[int] = mapped_column(default=0)

