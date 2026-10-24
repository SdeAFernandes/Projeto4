# API de Filmes

API REST para consultar e gerenciar filmes e gêneros, desenvolvida com Django e Django REST Framework, com Django-Filter para filtros de pesquisa e autenticação por token. Os dados são armazenados em um banco SQLite.

## Requisitos

- Python 3.12 ou superior
- Git

## Clonar e iniciar

### Windows (PowerShell)

```powershell
git clone https://github.com/SdeAFernandes/Projeto4.git
cd Projeto4
git checkout desenvolvimento

python -m venv venv
.\venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Se o PowerShell bloquear a ativação do ambiente virtual, consulte a documentação de políticas de execução do PowerShell ou use o Command Prompt (CMD).

### Windows (CMD)

```cmd
git clone https://github.com/SdeAFernandes/Projeto4.git
cd Projeto4
git checkout desenvolvimento

python -m venv venv
venv\Scripts\activate

python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Linux ou macOS

```bash
git clone https://github.com/SdeAFernandes/Projeto4.git
cd Projeto4
git checkout desenvolvimento

python3 -m venv venv
source venv/bin/activate

python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

O servidor estará disponível em http://127.0.0.1:8000/.

> Se o repositório não tiver um `requirements.txt`, instale as dependências manualmente:
>
> ```bash
> pip install django django-filter djangorestframework
> ```

## Criar o superusuário

Para acessar o painel administrativo e gerar tokens de autenticação:

```bash
python manage.py createsuperuser
```

## Dados iniciais (opcional)

O banco `db.sqlite3` não é versionado. O comando `migrate` cria um banco local vazio. Para preenchê-lo com os registros de `base_filmes.csv`, execute na raiz do projeto (mesma pasta do `manage.py`):

```bash
python importarDados.py
```

Execute a importação apenas uma vez por banco: o script insere os registros do CSV e não verifica se os filmes já foram importados. Pode gerar duplicação de dados.

## Modelo de dados

| Tabela | Campos |
|--------|--------|
| Generos | `nome` |
| Filmes | `titulo`, `descricao`, `ano_lancamento`, `genero` (chave estrangeira para Generos), `duracao` |

## Endpoints

O Django REST Framework disponibiliza a interface navegável da API no navegador:

| Recurso | Endpoint |
|---------|----------|
| Gêneros | http://127.0.0.1:8000/api/generos/ |
| Filmes | http://127.0.0.1:8000/api/filmes/ |
| Obter token | http://127.0.0.1:8000/api/token/ |
| Administração Django | http://127.0.0.1:8000/admin/ |

Os endpoints de gêneros e filmes oferecem operações CRUD. A listagem aceita filtros via Django-Filter, por exemplo:

```
http://127.0.0.1:8000/api/filmes/?ano_lancamento=2014
http://127.0.0.1:8000/api/filmes/?genero=1
```

## Autenticação

A API usa `IsAuthenticatedOrReadOnly`: consultas (GET) são liberadas, mas criar, editar e excluir exigem autenticação por token ou por sessão (login via navegador).

### Obter um token

```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"seu_usuario","password":"sua_senha"}'
```

No Windows (CMD), use `curl.exe`, `^` para quebrar linha e aspas escapadas no JSON.

## Exemplos com curl

Listar filmes:

```bash
curl http://127.0.0.1:8000/api/filmes/
curl http://127.0.0.1:8000/api/filmes/3/
```

Adicionar um filme:

```bash
curl -X POST http://127.0.0.1:8000/api/filmes/ \
  -H "Authorization: Token SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{"titulo":"Interestelar","descricao":"Uma exploração espacial.","ano_lancamento":2014,"genero":1,"duracao":169}'
```

Editar um filme:

```bash
curl -X PATCH http://127.0.0.1:8000/api/filmes/1/ \
  -H "Authorization: Token SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{"duracao":170}'
```

Excluir um filme:

```bash
curl -X DELETE http://127.0.0.1:8000/api/filmes/1/ \
  -H "Authorization: Token SEU_TOKEN_AQUI"
```

## Tecnologias

- Python
- Django
- Django REST Framework
- Django-Filter
- SQLite