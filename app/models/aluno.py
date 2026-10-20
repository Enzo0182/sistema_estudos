from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from app.database.base import Base
from app.models.teste import Teste
from app.models.rotina import Rotina


class Aluno(Base):
    __tablename__ = "aluno"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(200))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    username: Mapped[str] = mapped_column(String(100), unique=True)
    senha_hash: Mapped[str] = mapped_column(String(255))
    nivel_autorizacao: Mapped[str] = mapped_column(String(50))
    testes: Mapped[list["Teste"]] = relationship(
        back_populates= "aluno"
    )
    rotinas: Mapped[list["Rotina"]] = relationship(
        back_populates= "aluno"
    )
    