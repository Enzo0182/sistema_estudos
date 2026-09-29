from pydantic import BaseModel, Field
from datetime import date
from enum import Enum

class TipoAlteracao(Enum):
    ADICIONAR = "adicionar"
    REMOVER = "remover"

class TesteCreate(BaseModel):
    descricao : str = Field(min_length=10, max_length=300)
    dt_realizacao : date
    nota : float
    tipo : str = Field(min_length=3, max_length=30)
    idQuestoes : list[int]
    
class TesteResponse(BaseModel):
    id : int
    descricao : str
    dt_realizacao : date
    nota : float
    tipo : str
    idQuestoes : list[int]
    model_config={
        'from_attributes' : True
    }
    
class TesteUpdate(BaseModel):
    descricao : str | None = None
    dt_realizacao : date | None = None
    nota : float | None = None
    tipo : str | None = None
    idQuestoes : list[int] | None = None
    tipoAlteracao : TipoAlteracao | None = None
