# API DGPE BA

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![SSH Tunnel](https://img.shields.io/badge/SSH-Tunnel-orange)

API para consulta de dados do programa Gestão da Aprendizagem das escolas estaduais da Bahia.

## 📋 Sumário

- [Visão Geral](#visão-geral)
- [Características](#características)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Documentação da API](#documentação-da-api)
- [Endpoints](#endpoints)
- [Modelos de Dados](#modelos-de-dados)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Contribuição](#contribuição)
- [Licença](#licença)

## 🎯 Visão Geral

A API DGPE BA é uma aplicação FastAPI que fornece acesso aos dados educacionais das escolas estaduais da Bahia. A API permite consultar informações sobre escolas, estudantes, professores, municípios, NTEs (Núcleos Territoriais de Educação) e outros dados relacionados ao sistema educacional.

## ✨ Características

- **RESTful API** com FastAPI
- **Conexão segura** via SSH Tunnel para PostgreSQL
- **Documentação automática** com Swagger UI
- **Validação de dados** com Pydantic
- **ORM** com SQLAlchemy
- **CORS** configurado para desenvolvimento
- **Arquitetura modular** com separação de responsabilidades

## 📋 Pré-requisitos

- Python 3.10 ou superior
- PostgreSQL (remoto via SSH)
- Chave SSH privada para conexão com o banco de dados

## 🚀 Instalação

1. **Clone o repositório**:
```bash
git clone <repository-url>
cd api-dgpe-ba
```

2. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

## ⚙️ Configuração

1. **Crie um arquivo `.env`** baseado no exemplo:
```bash
cp .env.example .env
```

2. **Configure as variáveis de ambiente** no arquivo `.env`:
```env
# PostgreSQL
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nome_do_banco
DB_USER=usuario
DB_PASSWORD=senha

# SSH Tunnel (opcional)
SSH_HOST=servidor.exemplo.com
SSH_PORT=22
SSH_USERNAME=usuario_ssh
SSH_PRIVATE_KEY_PATH=keys/chave_privada.pem

# Configurações remotas (se usando SSH)
REMOTE_DB_HOST=localhost
REMOTE_DB_PORT=5432
```

3. **Adicione sua chave SSH** na pasta `keys/` (se necessário)

## 🏃 Uso

### Executar a aplicação

```bash
# Usando uvicorn diretamente
uvicorn app.main:app --reload

# Ou usando o comando do arquivo run.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

A API estará disponível em: `http://localhost:8000`

### Documentação interativa

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Testar SSH Tunnel (se necessário)

```bash
python scripts/create_ssh_tunnel.py
```

## 📖 Documentação da API

### Endpoints Principais

#### 🏫 Escolas
- `GET /api/v1/escola/` - Listar todas as escolas
- `GET /api/v1/escola/{codigo_sec}` - Obter escola por código SEC

**Parâmetros de consulta**:
- `nome`: Filtrar por nome da escola
- `nte`: Filtrar por NTE

#### 🏛️ NTE (Núcleos Territoriais de Educação)
- `GET /api/v1/nte/` - Listar todos os NTEs
- `GET /api/v1/nte/{nte_id}` - Obter NTE por ID

#### 🏙️ Municípios
- `GET /api/v1/municipio/` - Listar todos os municípios
- `GET /api/v1/municipio/{codigo_ibge}` - Obter município por código IBGE

**Parâmetros de consulta**:
- `nome`: Filtrar por nome do município
- `codigo_ibge`: Filtrar por código IBGE
- `coordenadas`: Passar 'on' para incluir coordenadas

#### 🎓 Estudantes
- `GET /api/v1/estudante/` - Listar todos os estudantes
- `GET /api/v1/estudante/{estudante_id}` - Obter estudante por ID

**Parâmetros de consulta**:
- `nome`: Filtrar por nome do estudante
- `rm`: Filtrar por RM (Registro de Matrícula)
- `perfil_id`: Filtrar por ID do perfil

#### 👨‍🏫 Professores
- `GET /api/v1/professor/` - Listar todos os professores
- `GET /api/v1/professor/{professor_id}` - Obter professor por ID

**Parâmetros de consulta**:
- `nome`: Filtrar por nome do professor
- `rm`: Filtrar por RM

#### 📚 Séries
- `GET /api/v1/serie/` - Listar todas as séries
- `GET /api/v1/serie/{serie_id}` - Obter série por ID

#### 🏫 Turmas
- `GET /api/v1/turma/` - Listar todas as turmas
- `GET /api/v1/turma/{turma_id}` - Obter turma por ID

**Parâmetros de consulta**:
- `codigo`: Filtrar por código da turma
- `escola_id`: Filtrar por ID da escola
- `serie_id`: Filtrar por ID da série

#### 👥 Perfis
- `GET /api/v1/perfil/` - Listar todos os perfis
- `GET /api/v1/perfil/{perfil_id}` - Obter perfil por ID

#### 🚩 Flags de Escola
- `GET /api/v1/flag-escola/` - Listar todas as flags
- `GET /api/v1/flag-escola/{flag_id}` - Obter flag por ID

## 📊 Modelos de Dados

### Escola
```json
{
  "id": 1,
  "codigo_sec": 12345,
  "codigo_mec": 67890,
  "nome": "Escola Estadual Exemplo",
  "nte": "NTE 01",
  "municipio": "Salvador",
  "anexo": 0,
  "endereco_logradouro": "Rua Exemplo",
  "endereco_numero": "123",
  "endereco_bairro": "Centro",
  "endereco_cep": 40000000,
  "latitude": -12.9714,
  "longitude": -38.5014
}
```

### Estudante/Professor
```json
{
  "id": 1,
  "rm": 12345,
  "nome": "João Silva",
  "email": "joao.silva@email.com",
  "perfil_id": 1
}
```

### Município
```json
{
  "id": 1,
  "codigo_ibge": 2927408,
  "nome": "Salvador",
  "coordenadas": "-12.9714,-38.5014" // opcional
}
```

## 🏗️ Estrutura do Projeto

```
api-dgpe-ba/
├── app/
│   ├── core/
│   │   ├── config.py          # Configurações da aplicação
│   │   └── database.py        # Configuração do banco de dados
│   ├── models/
│   │   ├── base.py           # Modelo base SQLAlchemy
│   │   └── educacao/         # Modelos do domínio educação
│   │       ├── escola.py
│   │       ├── estudante.py
│   │       ├── professor.py
│   │       ├── municipio.py
│   │       ├── nte.py
│   │       ├── serie.py
│   │       ├── turma.py
│   │       ├── perfil.py
│   │       ├── flag_escola.py
│   │       ├── estudante_turma.py
│   │       └── professor_turma.py
│   ├── routes/
│   │   └── educacao/         # Rotas da API
│   │       ├── escola.py
│   │       ├── estudante.py
│   │       ├── professor.py
│   │       ├── municipio.py
│   │       ├── nte.py
│   │       ├── serie.py
│   │       ├── turma.py
│   │       ├── perfil.py
│   │       └── flag_escola.py
│   ├── schemas/
│   │   ├── base.py           # Schema base Pydantic
│   │   └── educacao/         # Schemas do domínio educação
│   │       ├── escola.py
│   │       ├── estudante.py
│   │       ├── professor.py
│   │       ├── municipio.py
│   │       ├── nte.py
│   │       ├── serie.py
│   │       ├── turma.py
│   │       ├── perfil.py
│   │       ├── flag_escola.py
│   │       ├── estudante_turma.py
│   │       └── professor_turma.py
│   └── main.py               # Aplicação principal FastAPI
├── keys/                     # Chaves SSH (não versionadas)
├── scripts/
│   └── create_ssh_tunnel.py  # Script para criar tunnel SSH
├── .env                      # Variáveis de ambiente (não versionado)
├── .env.example             # Exemplo de variáveis de ambiente
├── requirements.txt         # Dependências Python
├── run.txt                  # Comando para executar a aplicação
└── README.md               # Este arquivo
```

## 🛠️ Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderno e rápido
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - ORM Python
- **[Pydantic](https://pydantic-docs.helpmanual.io/)** - Validação e serialização de dados
- **[PostgreSQL](https://www.postgresql.org/)** - Banco de dados relacional
- **[SSH Tunnel](https://pypi.org/project/sshtunnel/)** - Conexão segura via SSH
- **[Uvicorn](https://www.uvicorn.org/)** - Servidor ASGI
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** - Carregamento de variáveis de ambiente

## 🔧 Exemplos de Uso

### Listar todas as escolas

```bash
curl -X GET "http://localhost:8000/api/v1/escola/"
```

### Buscar escola por nome

```bash
curl -X GET "http://localhost:8000/api/v1/escola/?nome=Colégio"
```

### Obter informações de um município específico

```bash
curl -X GET "http://localhost:8000/api/v1/municipio/2927408"
```

### Listar estudantes por perfil

```bash
curl -X GET "http://localhost:8000/api/v1/estudante/?perfil_id=1"
```

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 🐛 Resolução de Problemas

### Erro de conexão com banco de dados

1. Verifique se as variáveis de ambiente estão configuradas corretamente
2. Teste a conexão SSH separadamente
3. Verifique se o PostgreSQL está rodando no servidor remoto

### Erro de importação de módulos

1. Certifique-se de que o ambiente virtual está ativado
2. Reinstale as dependências: `pip install -r requirements.txt`
3. Verifique se o PYTHONPATH está configurado corretamente

## 📄 Licença

Este projeto é licenciado sob a [MIT License](LICENSE).

---

**Desenvolvido para a Secretaria de Educação da Bahia (SEC-BA) pelo DGPE FGV**

Para mais informações ou suporte, entre em contato com a equipe de desenvolvimento.

Desenvolvido com ❤️ para a educação baiana