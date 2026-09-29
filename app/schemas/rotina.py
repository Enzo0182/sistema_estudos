from pydantic import BaseModel
from datetime import date, time, timedelta


class RotinaCreate(BaseModel):
    dia: date
    horario: time
    duracao: timedelta
    idMaterias: list[int]
    
class RotinaResponse(BaseModel):
    id: int
    dia: date
    horario: time
    duracao: timedelta
    idMaterias: list[int]
    model_config = {
        'from_attributes': True
    }

class RotinaUpdate(BaseModel):
    dia: date | None = None
    horario: time | None = None
    duracao: timedelta | None = None
    idMateria: list[int] | None = None