from pydantic import Field, BaseModel

class MateriaResponse(BaseModel):
    id: int
    nome: str = Field(min_length=3, max_length= 50)
    descricao : str = Field(min_length=3, max_length=200)
    model_config = {
            'from_attributes': True
        }

class MateriaUpdate(BaseModel):
    descricao : str 