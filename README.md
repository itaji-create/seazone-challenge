# Boas-vindas ao repositório do projeto `Seazone Challenge`!

Esse projeto visa criar 3 API's usando Django: `/properties`, `/adverts` e `/reservations`

# Orientações
<details>
  <summary><strong>⚠️ Como instalar seu projeto</strong></summary><br />

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:itaji-create/seazone-challenge.git`.
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd seazone-challenge`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`
  - :eyes: Caso precise desativar o ambiente virtual, execute o comando "deactivate".

  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`

</details>

<details>
  <summary><strong>Populando o Bando de Dados :bank: </strong></summary><br />

  <strong>Execute os comandos na seguinte ordem:</strong>

  1. `python3 manage.py loaddata properties.json`
  2. `python3 manage.py loaddata adverts.json`
  3. `python3 manage.py loaddata reservations.json`
</details>

<details>
  <summary><strong>Testes 🛠</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```
</details>

<details>
  <summary><strong>Iniciando projeto :rocket: </strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  ```bash
  $ python3 manage.py runserver
  ```

</details>