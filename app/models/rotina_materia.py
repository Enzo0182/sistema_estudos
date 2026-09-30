from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from app.database.base import Base

class Rotina_Materia(Base):
    __tablename__ = "rotina_materia"
    
    id_materia: Mapped[int] = mapped_column(ForeignKey("materia.id"), primary_key=True)
    id_rotina: Mapped[int] = mapped_column(ForeignKey("rotina.id"), primary_key=True)
    