from pydantic import Field, BaseModel
from datetime import datetime


class MaterialCreate(BaseModel):
    descricao: str = Field(min_length=10, max_length=500)
    titulo: str = Field(min_length=10, max_length=200)
    tipo: str = Field(min_length=3, max_length=50)
    url: str = Field(max_length=2048)
    idConteudo: int

class MaterialResponse(BaseModel):
    id: int
    titulo: str
    descricao: str
    tipo: str
    url: str
    idConteudo: int
    idAluno:int
    criadoEm: datetime
    status: str
    model_config = {
        'from_attributes': True
    }
    
class MaterialUpdate(BaseModel):
    titulo: str | None = None
    descricao: str | None = None
    tipo: str | None = None
    url: str | None = None