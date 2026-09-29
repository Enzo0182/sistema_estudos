from pydantic import BaseModel, Field


class QuestaoCreate(BaseModel):
    descricao: str = Field(min_length= 20, max_length=200)
    tipo:str = Field(min_length=3, max_length=30)
    alternativa_a:str | None = None
    alternativa_b:str | None = None
    alternativa_c:str | None = None
    alternativa_d:str | None = None
    gabarito: str | None = None
    idConteudo : int
    
class QuestaoResponse(BaseModel):
    id:int
    descricao: str = Field(min_length= 20, max_length=200)
    tipo:str = Field(min_length=3, max_length=30)
    alternativa_a:str | None
    alternativa_b:str | None
    alternativa_c:str | None
    alternativa_d:str | None
    gabarito: str | None
    idConteudo : int
    model_config = {
        "from_attributes": True
    }

class QuestaoUpdate(BaseModel):
    descricao: str | None = None
    tipo:str | None = None
    alternativa_a:str | None = None
    alternativa_b:str | None = None
    alternativa_c:str | None = None
    alternativa_d:str | None = None
    gabarito: str | None = None