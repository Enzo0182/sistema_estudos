from sqlalchemy.orm import  Mapped, mapped_column
from sqlalchemy import Date, Time, ForeignKey, Interval
from app.database.base import Base
from datetime import time, date, timedelta

class Rotina(Base):
    __tablename__ = "Rotina"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    dia: Mapped[date] = mapped_column(Date)
    horario: Mapped[time] = mapped_column(Time)
    duracao: Mapped[timedelta] = mapped_column(Interval)     
    id_aluno: Mapped[int] = mapped_column(ForeignKey("aluno.id"))
    