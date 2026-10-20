from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from app.database.base import Base
from app.models.rotina import Rotina
from app.models.materia import Materia

class Rotina_Materia(Base):
    __tablename__ = "rotina_materia"
    
    id_materia: Mapped[int] = mapped_column(ForeignKey("materia.id"), primary_key=True)
    id_rotina: Mapped[int] = mapped_column(ForeignKey("rotina.id", ondelete="CASCADE"), primary_key=True)
    rotina: Mapped["Rotina"] = relationship(
        back_populates= "materias_associadas"
    )
    materia: Mapped["Materia"] = relationship(
        back_populates= "rotinas_associadas"
    )
    
    