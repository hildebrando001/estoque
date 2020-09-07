Estoque - Controle de estoque


Como rodar o projeto?

Clone esse repositório.
    git clone https://github.com/hildebrando001/estoque.git

Crie um virtualenv com Python 3.
    cd estoque
    python3 -m venv .venv

Ative o virtualenv.
    source .venv/bin/activate

Instale as dependências.
    pip install -r requirements.txt

Rode as migrações.
    python contrib/env_gen.py
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
