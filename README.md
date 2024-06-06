API de Gestão de Livros em Flask

Este projeto implementa uma API RESTful para gerenciar livros utilizando o framework Flask e seguindo uma estrutura organizacional em camadas.

Bibliotecas Instaladas:

    blinker==1.8.2
    click==8.1.7
    Flask==3.0.3
    itsdangerous==2.2.0
    Jinja2==3.1.4
    MarkupSafe==2.1.5
    Werkzeug==3.0.3

Estrutura do Projeto:

    database:
        Conexão com o banco de dados e operações CRUD para entidades.
    model:
        Definição das classes de modelo para representar os livros.
    schema:
        Validação de dados de entrada e saída da API.
    settings:
        Armazenamento de configurações da aplicação.
    util:
        Funções auxiliares para o projeto.

Funcionalidades da API:

    Criar livro: Adiciona um novo livro ao banco de dados.
    Ler livro: Recupera um livro específico pelo ID.
    Atualizar livro: Modifica os dados de um livro existente.
    Excluir livro: Remove um livro do banco de dados.
    Listar livros: Retorna uma lista de todos os livros.

Para executar a API:

    Clone o repositório.
    Instale as bibliotecas necessárias: pip install -r requirements.txt
    Crie e configure o banco de dados.
    Execute o script de inicialização: python manage.py init
    Inicie a API: python manage.py run

Documentação da API:

A documentação da API está disponível em https://swagger.io/tools/swaggerhub/.

Contribuindo:

Sinta-se à vontade para contribuir com o projeto! Envie suas sugestões, pull requests e relatórios de bugs.

Licença:

Este projeto está licenciado sob a licença MIT.
