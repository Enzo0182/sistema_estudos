from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.rotina import RotinaCreate, RotinaUpdate
from app.database.conexao import get_session
from app.service.rotina_service import criar_rotina, modificar_rotina


router = APIRouter()

@router.post("{id_aluno}/rotina")
def criar_rotina(
    dados: RotinaCreate,
    session:Session = Depends(get_session)
):
    return criar_rotina(dados, session)

@router.patch("{id_aluno}/rotina/{id_rotina}")
def modificar_rotina(
    dados: RotinaUpdate,
    session: Session = Depends(get_session)
):
    return modificar_rotina(dados, session)

@router.delete("{id_aluno}/rotina/{id_rotina}")
def deletar_rotina(id_aluno, id_rotina):
    return deletar_rotina(id_aluno, id_rotina)