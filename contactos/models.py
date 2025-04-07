from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from connect import db

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    apellido: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    telefono: Mapped[str] = mapped_column(nullable=False)
