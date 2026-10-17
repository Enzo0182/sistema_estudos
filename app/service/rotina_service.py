from sqlalchemy.orm import Session
from sqlalchemy import select, and_
from app.models.rotina import Rotina
from app.models.rotina_materia import Rotina_Materia
from app.schemas.rotina import RotinaCreate, RotinaUpdate


def criar_rotina(id_aluno: int,dados: RotinaCreate, session: Session):
    try:
        rotina = Rotina(
            dia = dados.dia,
            horario = dados.horario,
            duracao = dados.duracao,
            id_aluno = id_aluno
        )
        session.add(rotina)
        session.flush()
        if len(dados.id_materias) > 0:
            for i in range(len(dados.id_materias)):
                rotina_materia = Rotina_Materia(
                    id_materia = dados.id_materias[i],
                    id_rotina = rotina.id
                )
                session.add(rotina_materia)
        else:
            session.rollback()
            return False
        session.commit()
        return True
    except Exception:
        session.rollback()
        return False
        

def modificar_rotina(id_aluno: int,id_rotina: int, dados: RotinaUpdate, session: Session):
    try:
        resultado = session.execute(
            select(Rotina).where(and_(Rotina.id == id_rotina, Rotina.id_aluno == id_aluno))
        )
        rotina = resultado.scalar_one_or_none()
        if rotina is None:
            return False
        dados_modificados = dados.model_dump(exclude_unset=True) 
        if dados.id_materias is not None:
            if modificar_materias(id_rotina, dados.id_materias, dados.tipo_operacao, session= session) == False:
                session.rollback()
                return False
            dados_modificados.pop("id_materias", default= None)
            dados_modificados.pop("tipo_operacao", default= None)
        for campo, valor in dados_modificados.items():
            setattr(rotina, campo, valor)
        session.commit()
        return True
    except Exception:
        session.rollback()
        return False


def modificar_materias(id_rotina: int,id_materias: list[int], operacao: str, session: Session):
    try:
        if len(id_materias) > 0:    
            if operacao == 'adicionar':
                    for i in range(len(id_materias)):
                        rotina_materia = Rotina_Materia(
                            id_materia = id_materias[i],
                            id_rotina = id_rotina
                        )
                        session.add(rotina_materia)

            elif operacao == 'remover':
                for i in range(0,len(id_materias)):
                    pegar_associacao = session.execute(
                        select(Rotina_Materia).where(and_(Rotina_Materia.id_rotina == id_rotina, Rotina_Materia.id_materia == id_materias[i]))
                    )
                    rotina_materia = pegar_associacao.scalar_one_or_none()
                    if rotina_materia is None:
                        print("Matéria não pertence à rotina!!")
                        return False
                    session.delete(rotina_materia)

            else:
                return False
            return True
        else:
            return None
    except Exception as e:
        print(e)
        return False
    
def deletar_rotina(id_aluno: int, id_rotina: int, session: Session):
    try:
        selecionar_rotina = session.execute(
            select(Rotina).where(and_(Rotina.id_aluno == id_aluno, Rotina.id == id_rotina))
        )
        rotina = selecionar_rotina.scalar_one_or_none()
        if rotina is None:
            return False
        session.delete(rotina)
        session.commit()
        return True
    except Exception:
        session.rollback()
        return False