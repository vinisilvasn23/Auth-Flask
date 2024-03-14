# Sistema de Autenticação Flask

![GitHub repo size](https://img.shields.io/github/repo-size/iuricode/README-template?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/iuricode/README-template?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/iuricode/README-template?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/iuricode/README-template?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/iuricode/README-template?style=for-the-badge)

### Este é um sistema de autenticação básico desenvolvido em Flask.
## Funcionalidades
- Registro de novos usuários
- Login de usuários existentes
- Proteção de rotas através de autenticação
  
## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:
Python 3.x

- Você instalou a versão mais recente de `<Python 3.x>`

## 🚀 Instalando projeto

Para instalar, siga estas etapas:

```
<git clone https://github.com/vinisilvasn23/Auth-Flask.git>
```

Para usar iniciar, siga estas etapas:
## Configuração
-O arquivo env.example contém configurações para o aplicativo Flask, como chaves secretas, URI do banco de dados, etc.

-O banco de dados ultilizado é o PostgreSql, mas você pode configurar outros bancos de dados editando a URI no arquivo env.example.
-Após configurar renomeie o arquivo para .env.

Instale as dependências usando o pip:
```
<pip install -r requirements.txt>
```
Execute o aplicativo Flask:
```
flask run
```

Acesse o aplicativo em seu navegador em http://localhost:5000.

## Rotas da API

1. **Listagem de Usuários** (`/users`)
   - `GET`: Retorna uma lista de todos os usuários.
   - `POST`: Cria um novo usuário.

2. **Detalhes de Usuário** (`/users/<int:user_id>`)
   - `GET`: Retorna os detalhes de um usuário específico com o ID fornecido.
   - `PUT`: Atualiza os detalhes de um usuário existente com o ID fornecido.
   - `DELETE`: Exclui um usuário com o ID fornecido.

3. **Login de Usuário** (`/login`)
   - `POST`: Autentica um usuário com as credenciais fornecidas e fornece um token de acesso.

4. **Recuperação de Senha Esquecida** (`/forgot_password`)
   - `POST`: Envia um e-mail de redefinição de senha para o endereço de e-mail fornecido.

5. **Redefinição de Senha** (`/reset_password_api`)
   - `POST`: Reseta a senha do usuário com base no token fornecido e na nova senha.

## Rotas do Flask

Além das rotas da API, existem rotas tradicionais do Flask para funcionalidades específicas:

- **Redefinir Senha** (`/reset_password`)
   - `GET`: Exibe um formulário para redefinir a senha.
   - `POST`: Processa o formulário para redefinir a senha.


