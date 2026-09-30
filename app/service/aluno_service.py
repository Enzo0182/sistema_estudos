from sqlalchemy.orm import Session
from sqlalchemy import select
from app.security.password_hashing import verificar_senha, senha_hashing
from app.models.aluno import Aluno
from app.schemas.aluno import AlunoCreate, AlunoUpdate, AlunoDelete
from app.schemas.auth import LoginRequest
from dataclasses import dataclass


@dataclass
class Resultado:
    resultado: bool
    aluno: Aluno | None
    

def logar_aluno(dados: LoginRequest, session: Session):
    resultado = session.execute(
        select(Aluno).where(Aluno.email == dados.email)
    )
    aluno = resultado.scalar_one_or_none()
    if aluno is not None:
        if verificar_senha(dados.senha, aluno.senha_hash):
            return Resultado(True, aluno)
        else:
            return Resultado(False)
    else:
        return Resultado(False)

def criar_aluno(dados: AlunoCreate, session: Session):
    try:
        aluno = Aluno(
            nome = dados.nome,
            email = dados.email,
            username = dados.username,
            senha_hash = senha_hashing(dados.senha)
        )
        session.add(aluno)
        session.commit()
        session.refresh(aluno)
        return True 
    except Exception:
        session.rollback()
        return False

def atualizar_dados_aluno(id_aluno: int, dados: AlunoUpdate, session: Session):
    
    aluno = session.get(Aluno, id_aluno)
    if aluno is None:
        return False
    dados_atualizar = dados.model_dump(exclude_unset=True)
    for campo, valor in dados_atualizar.items():
        if campo == 'senha' and verificar_senha(dados.senha_atual, aluno.senha_hash):
            aluno.senha_hash = senha_hashing(valor)
        elif campo != 'senha_atual':
            setattr(aluno, campo, valor)
    try:
        session.commit()
        return True
    
    except Exception:
        session.rollback()
        return False

        
    