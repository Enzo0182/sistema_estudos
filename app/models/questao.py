from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from app.database.base import Base

class questao(Base):
    __tablename__ = "questao"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    descricao: Mapped[str] = mapped_column(String(200))
    alternativa_a: Mapped[str] = mapped_column(String(250))
    alternativa_b: Mapped[str] = mapped_column(String(250))
    alternativa_c: Mapped[str] = mapped_column(String(250))
    alternativa_d: Mapped[str] = mapped_column(String(250))
    gabarito: Mapped[str] = mapped_column(String(20))
    id_conteudo: Mapped[int] = mapped_column(ForeignKey("conteudo.id"))