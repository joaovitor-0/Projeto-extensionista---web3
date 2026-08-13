# Sistema Web para a ONG GAVIME
## Descrição do Projeto
Este projeto consiste no desenvolvimento de um sistema web para a ONG Grupo de Apoio Viver Melhor (GAVIME). A organização realiza um importante trabalho social, auxiliando indivíduos e famílias em situação de vulnerabilidade por meio de doações de roupas e alimentos, além de oferecer serviços como atendimento odontológico, acompanhamento psicológico e oficinas profissionalizantes.

O sistema foi desenvolvido inicialmente como um projeto acadêmico e, posteriormente, aprimorado e implementado como o site da organização.

O objetivo do sistema é aumentar a visibilidade da ONG e facilitar o acesso às informações sobre suas atividades, contribuindo para atrair voluntários, doações e apoio de órgãos públicos.

## Site
O site pode ser acessado através do endereço:

https://gavime.org

## Funcionalidades
- Divulgação de informações institucionais da GAVIME.
- Divulgação e gerenciamento de campanhas.
- Sistema de banners configuráveis para a página principal.
- Página com informações e opções para doações.
- Formulário de contato.
- Inscrição de interessados nas atividades da organização.
- Divulgação de informações de transparência.
- Área restrita para funcionários.
- Gerenciamento de atividades, inscritos e voluntários.
- Gerenciamento das informações de transparência exibidas no site.

## Tecnologias Utilizadas
Python — Linguagem principal utilizada no desenvolvimento da aplicação e na implementação das regras de negócio.
Django — Framework web utilizado para o desenvolvimento do sistema.
HTML e CSS — Utilizados na construção e estilização das páginas do sistema.
MySQL — Utilizado na modelagem inicial e nos testes do banco de dados.
SQLite — Banco de dados utilizado na versão final da aplicação.
GitHub — Utilizado para versionamento e armazenamento do código-fonte.
Render — Plataforma utilizada para hospedagem e disponibilização do site.

### Como executar

### Requisitos
Python 3.13 ou superior
Django

### Instalação

No terminal do PyCharm ou da IDE utilizada, instale o Django.

Comando:

```bash
pip install django
```

### Banco de Dados

Execute as migrações para criar as tabelas do sistema.

Comando:

```bash
python manage.py migrate
```

### Execução

Inicie o servidor local.

Comando:

```bash
python manage.py runserver
```

Após iniciar o servidor, acesse:

```text
http://127.0.0.1:8000/
```

### Área de Funcionários

Área restrita para funcionários, onde é possível consultar e alterar os dados do sistema, além de controlar a exibição das informações de transparência no site.

Acesso através do sistema de login:

```text
http://127.0.0.1:8000/login/
```

## Status do Projeto
Projeto finalizado.

O sistema foi concluído e implementado como site da GAVIME, estando disponível através do endereço:

https://gavime.org
