python:3.8.1

## Setup

#### Rodar:

```
pip install -r requirements.txt
```

#### Copiar o .env.template e adicionar as envs 

```
cp .env.template .env
```

#### Flask env
```
export FLASK_ENV=app.py
```

#### Database

1 - Criar o Database colocado no arquivo .env <DATABASE_NAME>

2 - Rodar o comando
```
flask db upgrade
```

#### Rodar a aplicação
```
flask run
```

## Endpoints

### Autenticação
#### POST /auth

headers: { "Content-Type": "application/json" }
body: { "cpf": "<cpf>", "password": "<password>" }

### Compras
#### GET /purchases
headers: { "Authorization": "JWT <token>"}

#### POST /purchases
headers: { "Content-Type": "application/json", "Authorization": "JWT <token>" }
body: { "code": "<code>", "value": "<value>","date": "<date>","reseller_cpf": "<reseller_cpf>"  }

### Revendedores
#### GET /resellers
headers: { "Authorization": "JWT <token>"}

#### POST /resellers
headers: { "Content-Type": "application/json", "Authorization": "JWT <token>" }
body: { "name": "<name>", "cpf": "<cpf>","email": "<email>","password": "<password>"  }

### Cashbacks
#### GET /cashbacks/<cpf>
headers: { "Authorization": "JWT <token>" }

## Logs

Ficam na pasta logs