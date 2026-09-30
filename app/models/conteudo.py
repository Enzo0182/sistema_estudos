from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from app.database.base import Base


class Conteudo(Base):
    __tablename__ = "conteudo"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    descricao:Mapped[str] = mapped_column(String(100))
    id_materia: Mapped[int] = mapped_column(ForeignKey("materia.id"))
    