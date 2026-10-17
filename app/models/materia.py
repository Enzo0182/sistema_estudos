from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import String
from app.database.base import Base
from app.models.conteudo import Conteudo


class Materia(Base):
    __tablename__ = "materia"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50))
    descricao: Mapped[str] = mapped_column(String(200))
    conteudos: Mapped[list["Conteudo"]] = relationship(
        back_populates="materias"
    )