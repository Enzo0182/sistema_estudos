# Rotas da API

## Auth

| Método | Rota      | Descrição                     | Acesso      |
|---|---|---|---|
| POST   | `/login`  | Autentica o usuário           | Público     |
| POST   | `/logout` | Encerra sessão do usuário     | Autenticado |
| POST   | `/signup` | Cadastra o usuário no sistema | Público     |

## Alunos

| Método | Rota           | Descrição                           | Acesso      |
|---|---|---|---|
| GET    | `/alunos`      | Lista os alunos                     | Admin       |
| GET    | `/alunos/{id}` | Consulta um aluno                   | Autenticado |
| PATCH  | `/alunos/{id}` | Modifica uma informação de um aluno | Dono/Admin  |
| DELETE | `/alunos/{id}` | Deleta um aluno                     | Dono/Admin  |

## Conteúdos

| Método | Rota              | Descrição                         | Acesso            |
|---|---|---|---|
| POST   | `/conteudos`      | Cria um conteúdo                  | Admin/Autenticado |
| GET    | `/conteudos`      | Lista os conteúdos                | Autenticado       |
| GET    | `/conteudos/{id}` | Acessa um conteúdo                | Autenticado       |
| PUT    | `/conteudos/{id}` | Modifica um conteúdo              | Admin             |
| PATCH  | `/conteudos/{id}` | Modifica parcialmente um conteúdo | Admin/Autenticado |
| DELETE | `/conteudos/{id}` | Deleta um conteúdo                | Admin             |

## Matérias

| Método | Rota             | Descrição                          | Acesso      |
|---|---|---|---|
| GET    | `/materias`      | Lista as matérias                  | Autenticado |
| GET    | `/materias/{id}` | Acessa uma matéria                 | Autenticado |
| POST   | `/materias`      | Cria uma matéria                   | Admin       |
| PATCH  | `/materias/{id}` | Modifica uma informação da matéria | Admin       |
| DELETE | `/materias/{id}` | Deleta uma matéria                 | Admin       |

## Materiais

| Método | Rota              | Descrição                           | Acesso            |
|---|---|---|---|
| GET    | `/materiais`      | Lista os materiais                  | Autenticado       |
| GET    | `/materiais/{id}` | Acessa um material                  | Autenticado       |
| POST   | `/materiais`      | Cria um material                    | Admin/Autenticado |
| PATCH  | `/materiais/{id}` | Modifica uma informação do material | Dono/Admin        |
| DELETE | `/materiais/{id}` | Deleta um material                  | Admin             |

## Questões

| Método | Rota             | Descrição                         | Acesso        |
|---|---|---|---|
| POST   | `/questoes`      | Cria uma questão                  | Admin/Sistema |
| GET    | `/questoes`      | Lista as questões                 | Admin         |
| GET    | `/questoes/{id}` | Acessa uma questão                | Sistema       |
| PUT    | `/questoes/{id}` | Modifica a questão                | Sistema/Admin |
| PATCH  | `/questoes/{id}` | Modifica parcialmente uma questão | Admin         |
| DELETE | `/questoes/{id}` | Deleta uma questão                | Admin         |

## Rotinas

| Método | Rota            | Descrição                        | Acesso              |
|---|---|---|---|
| POST   | `/rotinas`      | Cria uma rotina                  | Sistema/Autenticado |
| GET    | `/rotinas`      | Lista as rotinas                 | Autenticado         |
| GET    | `/rotinas/{id}` | Acessa uma rotina                | Dono/Admin          |
| PUT    | `/rotinas/{id}` | Modifica uma rotina              | Dono/Sistema        |
| PATCH  | `/rotinas/{id}` | Modifica parcialmente uma rotina | Dono/Sistema        |
| DELETE | `/rotinas/{id}` | Deleta uma rotina                | Dono/Admin          |

## Testes

| Método | Rota           | Descrição                   | Acesso      |
|---|---|---|---|
| POST   | `/testes`      | Cria um teste               | Sistema     |
| GET    | `/testes`      | Lista os testes             | Admin       |
| GET    | `/testes/{id}` | Acessa um teste             | Autenticado |
| PATCH  | `/testes/{id}` | Modifica uma parte do teste | Admin       |
| DELETE | `/testes/{id}` | Deleta um teste             | Admin       |
