# Sistema Web para a ONG GAVIME 

## Descrição do Projeto
Este projeto consiste no desenvolvimento de um sistema web para a ONG Grupo de Apoio Viver Melhor (GAVIME). A organização realiza um importante trabalho social, auxiliando indivíduos e famílias em situação de vulnerabilidade por meio de doações de roupas e alimentos, além de oferecer serviços como atendimento odontológico, acompanhamento psicológico e oficinas profissionalizantes.

O objetivo do sistema é aumentar a visibilidade da ONG e facilitar o acesso às informações sobre suas atividades, contribuindo para atrair voluntários, doações e apoio de órgãos públicos. O projeto também busca aplicar, na prática, os conhecimentos adquiridos durante a formação acadêmica na área de desenvolvimento de sistemas.

## Tecnologias Utilizadas
- Python — Linguagem principal utilizada no desenvolvimento da aplicação e na implementação das regras de negócio.

- Django — Framework web responsável pela construção do backend e disponibilização das APIs.

- MySQL — Utilizado na modelagem inicial e testes do banco de dados.

- SQLite — Banco de dados utilizado na versão atual da aplicação através da configuração padrão do Django.

## Como executar

### Requisitos

- Python 3.13 ou superior
- Django

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
