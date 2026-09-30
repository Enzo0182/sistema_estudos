from fastapi import APIRouter, Depends
from app.schemas.aluno import AlunoCreate
from app.schemas.auth import LoginRequest
from app.database.conexao import get_session
from app.service.aluno_service import logar_aluno, criar_aluno
from sqlalchemy.orm import Session



router = APIRouter()

@router.post("/signup")
def signup(
    dados : AlunoCreate,
    session: Session = Depends(get_session)
):
    return criar_aluno(dados, session)

@router.post("/login")
def login(
    dados: LoginRequest,
    session: Session = Depends(get_session)
):
    return logar_aluno(dados, session)
        