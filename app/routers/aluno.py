from app.service.aluno_service import atualizar_dados_aluno, deletar_aluno
from sqlalchemy.orm import Session
from app.database.conexao import get_session
from fastapi import APIRouter, Depends
from app.schemas.aluno import AlunoDelete, AlunoUpdate

router = APIRouter()

@router.patch('/aluno/{id_aluno}')
def atualizar_dados(
    id_aluno: int,
    dados: AlunoUpdate,
    session: Session = Depends(get_session)
):
    return atualizar_dados_aluno(id_aluno, dados, session)

@router.delete('/aluno/{id_aluno}')
def deletar_aluno_(
    id_aluno: int,
    dados: AlunoDelete,
    session: Session = Depends(get_session)
):
    return deletar_aluno(id_aluno, dados, session)
    
