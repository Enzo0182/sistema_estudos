from pydantic import EmailStr, BaseModel, Field


class LoginRequest(BaseModel):
    id: int | None = None
    email: EmailStr | None = None
    senha: str = Field(min_length=8, max_length=50)
    
    