from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.database.base import Base


class Materia(Base):
    __tablename__ = "materia"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50))
    descricao: Mapped[str] = mapped_column(String(200))