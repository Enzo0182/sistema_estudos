from datetime import datetime
from enum import Enum
from app.database.base import Base
from sqlalchemy import Enum as SQLEnum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column


class StatusMaterial(Enum):
    PENDENTE = "pendente"
    APROVADO = "aprovado"
    REJEITADO = "rejeitado"


class MaterialEnsino(Base):

    id: Mapped[int] = mapped_column(primary_key=True)

    descricao: Mapped[str] = mapped_column(String(500))
    titulo: Mapped[str] = mapped_column(String(200))
    tipo: Mapped[str] = mapped_column(String(50))
    url: Mapped[str] = mapped_column(String(2048))

    id_conteudo: Mapped[int] = mapped_column(
        ForeignKey("conteudo.id")
    )

    id_aluno: Mapped[int] = mapped_column(
        ForeignKey("aluno.id")
    )

    status: Mapped[StatusMaterial] = mapped_column(
        SQLEnum(StatusMaterial),
        default=StatusMaterial.PENDENTE
    )

    criado_em: Mapped[datetime] = mapped_column()