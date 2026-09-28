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

    idConteudo: Mapped[int] = mapped_column(
        ForeignKey("conteudo.id")
    )

    idAluno: Mapped[int] = mapped_column(
        ForeignKey("aluno.id")
    )

    status: Mapped[StatusMaterial] = mapped_column(
        SQLEnum(StatusMaterial),
        default=StatusMaterial.PENDENTE
    )

    criadoEm: Mapped[datetime] = mapped_column()