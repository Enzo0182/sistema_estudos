from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String
from app.database.base import Base

class MaterialEnsino(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    descricao: Mapped[str] = mapped_column(String(500))
    titulo: Mapped[str] = mapped_column(String(200))
    tipo: Mapped[str] = mapped_column(String(50))
    url: Mapped[str] = mapped_column(String(2048))
    idConteudo: Mapped[int] = mapped_column(ForeignKey("conteudo.id"))