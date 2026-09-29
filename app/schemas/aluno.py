from pydantic import BaseModel, EmailStr, Field

class AlunoCreate(BaseModel):
    nome: str = Field(min_length = 3, max_length= 200)
    email: EmailStr
    username: str = Field(min_length=3, max_length=100)
    senha: str = Field(min_length= 8, max_length= 50)
    

class AlunoResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    
    model_config={
        "from_attributes" : True
    }

class AlunoUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    senha: str | None = None
    senha_atual: str | None = None
    
class AlunoDelete(BaseModel):
    senha_atual : str
    
