from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from app.database.base import Base

class Teste_Questao(Base):
    __tablename__ = "teste_questao"
    
    idTeste: Mapped[int] = mapped_column(ForeignKey("teste.id"), primary_key=True)
    idQuestao: Mapped[int] = mapped_column(ForeignKey("questao.id"), primary_key=True)
    