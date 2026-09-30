from pydantic import Field, BaseModel


class ConteudoCreate(BaseModel):
    descricao: str = Field(min_length=10, max_length=100)
    id_materia: int

class ConteudoResponse(BaseModel):
    id: int
    descricao: str
    id_materia: int
    
    model_config={
        "from_attributes":True
    }
    
class ConteudoUpdate(BaseModel):
    descricao: str | None = None
    id_materia : int | None = None