from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from app.database.base import Base
from app.models.teste import Teste
from app.models.questao import Questao

class Teste_Questao(Base):
    __tablename__ = "teste_questao"
    

    id_teste: Mapped[int] = mapped_column(ForeignKey("teste.id"), primary_key=True)
    id_questao: Mapped[int] = mapped_column(ForeignKey("questao.id"), primary_key=True)
    teste: Mapped["Teste"] = relationship(
        back_populates= "questoes_associados"
    )
    questao: Mapped["Questao"] = relationship(
        back_populates= "testes_associados"
    )
    
    