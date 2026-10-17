from sqlalchemy.orm import  Mapped, mapped_column, relationship
from sqlalchemy import Date, Time, ForeignKey, Interval
from app.database.base import Base
from datetime import time, date, timedelta
from app.models.rotina_materia import Rotina_Materia

class Rotina(Base):
    __tablename__ = "rotina"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    dia: Mapped[date] = mapped_column(Date)
    horario: Mapped[time] = mapped_column(Time)
    duracao: Mapped[timedelta] = mapped_column(Interval)     
    id_aluno: Mapped[int] = mapped_column(ForeignKey("aluno.id"))
    materias: Mapped[list["Rotina_Materia"]] = relationship(
        back_populates= "rotina",
        cascade= "all, delete-orphan",
        passive_deletes=True
    )
    