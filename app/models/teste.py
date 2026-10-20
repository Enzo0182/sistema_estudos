from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Date, Float
from app.database.base import Base
from datetime import date
from app.models.aluno import Aluno
from app.models.teste_questao import Teste_Questao

class Teste(Base):
    __tablename__ = "teste"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    descricao: Mapped[str] = mapped_column(String(300))
    dt_realizacao: Mapped[date] = mapped_column(Date)
    nota: Mapped[float] = mapped_column(Float)
    tipo: Mapped[str] = mapped_column(String(30))
    id_aluno: Mapped[int] = mapped_column(ForeignKey("aluno.id"))
    aluno:Mapped["Aluno"] = relationship(
        back_populates= "testes"
    )
    questoes_associadas: Mapped[list["Teste_Questao"]] = relationship(
        back_populates= "teste"
    )
