from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from app.database.base import Base
from app.models.materia import Materia
from app.models.materialEnsino import MaterialEnsino
from app.models.questao import Questao

class Conteudo(Base):
    __tablename__ = "conteudo"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    descricao:Mapped[str] = mapped_column(String(100))
    id_materia: Mapped[int] = mapped_column(ForeignKey("materia.id"))
    materia: Mapped["Materia"] = relationship(
        back_populates= "conteudos"
    )
    materiais: Mapped[list["MaterialEnsino"]] = relationship(
        back_populates= "conteudo"
    )
    questoes: Mapped[list["Questao"]] = relationship(
        back_populates= "conteudo"
    )