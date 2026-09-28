from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.database.base import Base

class Aluno(Base):
    __tablename__ = "aluno"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(200))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    username: Mapped[str] = mapped_column(String(100), unique=True)
    senha_hash: Mapped[str] = mapped_column(String(255))
    nivel_autorizacao: Mapped[str] = mapped_column(String(50))
    