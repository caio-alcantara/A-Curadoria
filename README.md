# A Curadoria

A Curadoria é um sistema de recomendação de filmes baseado nas escolhas de votos dos usuários. Ao longo de uma série de votações, onde os usuários escolhem entre pares de filmes, o sistema utiliza essas escolhas para recomendar novos filmes que possam interessar ao usuário. O backend utiliza o **The Movie Database (TMDb)** para buscar as informações dos filmes, e o frontend é desenvolvido com **HTML, CSS e JavaScript**.

## Funcionalidades

- **Votação de Filmes**: O usuário é apresentado a 10 pares de filmes e deve escolher um de cada par. Essas escolhas são armazenadas no navegador.
- **Recomendação de Filmes**: Após a votação, com base nos filmes escolhidos, são feitas recomendações personalizadas.

## Tecnologias Usadas

- **Backend**: 
  - Flask (Python)
  - API do [The Movie Database (TMDb)](https://www.themoviedb.org/documentation/api) para busca de filmes e recomendações.
  
- **Frontend**:
  - HTML, CSS, JavaScript
  - Tailwind
## Rotas da API Backend

1. **Obter Detalhes do Filme**
    ```http
    GET /movie/<int:movie_id>
    ```
    Retorna os detalhes de um filme com base no ID.

2. **Buscar Filmes por Nome**
    ```http
    GET /search?query=<movie_name>
    ```
    Retorna filmes que correspondem ao nome fornecido.

3. **Obter Filmes Populares**
    ```http
    GET /popular
    ```
    Retorna uma lista de filmes populares.

4. **Obter Filmes por Gênero**
    ```http
    GET /genre/<int:genre_id>
    ```
    Retorna filmes de um gênero específico.

5. **Obter Recomendações de um Filme**
    ```http
    GET /<int:movie_id>/recommendations
    ```
    Retorna filmes recomendados com base em um filme específico.

6. **Buscar ID do Filme pelo Nome**
    ```http
    GET /find_id/<movie_name>
    ```
    Retorna o ID de um filme com base no nome fornecido.

## Estrutura de Arquivos

```bash
A-Curadoria/
├── backend/
│   ├── app.py                # Arquivo principal do backend
│   └── requirements.txt      # Dependências do backend
├── frontend/
│   ├── index.html            # Página principal
│   ├── style.css             # Estilos CSS
│   └── script.js             # Lógica JavaScript
└── README.md                 # Documentação do repositório
```

## Como Rodar

### Backend

1. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

2. Execute o servidor Flask:
    ```bash
    python app.py
    ```

3. O backend estará disponível em `http://localhost:5000`.

### Frontend

1. O frontend é estático, então basta abrir o arquivo `frontend/index.html` no seu navegador para visualizar a interface.
2. Além disso, você pode acessar a página na rota base "/", ou seja, acessar `http://localhost:5000/`

## Como Funciona a Votação

1. Ao acessar a página inicial, o usuário será apresentado a dois filmes, cada um com título, gênero, imagem de capa e breve descrição.
2. O usuário deve clicar no card do filme que prefere.
3. Esse voto é armazenado no navegador (localStorage) e, após 10 duplas de filmes, o sistema exibirá 3 filmes recomendados com base nas escolhas do usuário.

## Como Funciona a Recomendação

Após o usuário votar em 10 filmes diferentes, o sistema utiliza essas escolhas para fazer recomendações personalizadas. As recomendações são baseadas em filmes semelhantes aos votados pelo usuário.

## Contribuindo

1. Faça o fork do repositório.
2. Crie uma branch para sua feature: `git checkout -b feature/nome-da-feature`.
3. Commit suas alterações: `git commit -am 'Adiciona nova feature'`.
4. Faça o push para sua branch: `git push origin feature/nome-da-feature`.
5. Abra um Pull Request.

## Contato

Se você tiver algum problema ou sugestão, entre em contato com o mantenedor através de [caioalcantarasantos3@gmail.com].
