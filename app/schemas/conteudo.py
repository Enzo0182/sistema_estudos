from pydantic import Field, BaseModel


class ConteudoCreate(BaseModel):
    descricao: str = Field(min_length=10, max_length=100)
    idMateria: int

class ConteudoResponse(BaseModel):
    id: int
    descricao: str
    idMateria: int
    
    model_config={
        "from_attributes":True
    }
    
class ConteudoUpdate(BaseModel):
    descricao: str | None = None
    idMateria : int | None = None