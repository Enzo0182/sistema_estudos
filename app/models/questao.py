from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from app.database.base import Base
from app.models.conteudo import Conteudo
from app.models.teste_questao import Teste_Questao

class Questao(Base):
    __tablename__ = "questao"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    descricao: Mapped[str] = mapped_column(String(200))
    alternativa_a: Mapped[str] = mapped_column(String(250))
    alternativa_b: Mapped[str] = mapped_column(String(250))
    alternativa_c: Mapped[str] = mapped_column(String(250))
    alternativa_d: Mapped[str] = mapped_column(String(250))
    gabarito: Mapped[str] = mapped_column(String(20))
    id_conteudo: Mapped[int] = mapped_column(ForeignKey("conteudo.id"))
    testes_associados:Mapped[list["Teste_Questao"]] = relationship(
        back_populates= "questao"
    )
    conteudo:Mapped["Conteudo"] = relationship(
        back_populates= "questoes"
    )
    
    