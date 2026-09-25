from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey, Date, Float
from app.database.base import Base
from datetime import date

class teste(Base):
    __tablename__ = "teste"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    descricao: Mapped[str] = mapped_column(String(300))
    dt_realizacao: Mapped[date] = mapped_column(Date)
    nota: Mapped[float] = mapped_column(Float)
    tipo: Mapped[str] = mapped_column(String(30))
    idAluno: Mapped[int] = mapped_column(ForeignKey("aluno.id"))
