# Car Rental Service 🚗

## Description

This project is a car rental application where users can view a list of available cars for rent. The back-end is developed in **Python (Flask)**, and the front-end is built with **React** and **Tailwind CSS** for responsive design and styling.

- **Back-end**: RESTful API built with **Flask**.
- **Front-end**: Application built with **React** and **Axios** for HTTP requests, and **Tailwind CSS** for styling.

-----

## Technologies Used

### Back-End
- **Python 3.x**
- **Flask**: Web framework for building the API.
- **CORS**: Middleware to allow cross-origin requests.

### Front-End
- **React.js**: JavaScript library for building user interfaces.
- **Tailwind CSS**: Utility-first CSS framework for styling the front-end.
- **Axios**: Library for making HTTP requests in React.

-----

## Features

- Displays a list of cars available for rent.
- Each car shows the name and daily rental price.
- Allows clicking "Rent/Return" (functionality is not implemented in the front-end yet).

-----

## Project Structure

### Back-End (Python + Flask)
1. `app.py`: Main file for the Flask API.
2. `requirements.txt`: List of back-end dependencies.

### Front-End (React + Tailwind CSS)
1. `src/App.js`: Main component that fetches car data from the API and displays it.
2. `public/index.html`: Main HTML file.
3. `tailwind.config.js`: Tailwind CSS configuration.

-----

## How to Run the Project

### 1. Set Up the Back-End (Flask)

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/car-rental.git
   cd car-rental
   ```

2 - Install the back-end dependencies:

 ```bash
Copiar código
pip install -r requirements.txt
 ```

3 - Run the Flask server:

```bash
python app.py
 ```

-----

##### The server will be running at http://127.0.0.1:5000/api/cars.

#### 2. Set Up the Front-End (React)

1 - Navigate to the front-end folder:

```bash
cd front-end
```

2 - Install the front-end dependencies:

```bash
npm install
```

3 - Run the React server:

```bash
npm start
```

-----

##### The front-end will be available at http://localhost:3000.

#### 3. Set Up CORS

 - If you're having issues with CORS (Cross-Origin Resource Sharing), as indicated in the previous logs, add the following to your app.py file (back-end):

```bash
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
```

- This will allow your front-end (running at http://localhost:3000) to make requests to the back-end without CORS restrictions.

-----

#### 4. Testing

 - With both servers (back-end and front-end) running, open http://localhost:3000 in your browser and you should see the list of cars displayed on the homepage.

-----

### Folder Structure
```bash

car-rental/
│
├── back-end/                        # Flask server code
│   ├── app.py                       # Main API file
│   └── requirements.txt             # Back-end dependencies
│
├── front-end/                       # React front-end code
│   ├── public/
│   │   └── index.html               # Main HTML file
│   ├── src/
│   │   ├── App.js                   # Main component
│   │   └── index.js                 # React entry point
│   ├── tailwind.config.js           # Tailwind CSS configuration
│   └── package.json                 # Front-end dependencies
│
└── README.md                        # This file

```
-----

### How to Contribute
1 - Fork the repository.
2 - Create a new branch for your changes (git checkout -b my-feature).
3 - Make your changes and commit (git commit -am 'Add new feature').
4 - Push your branch to the remote repository (git push origin my-feature).
5 - Open a pull request.

-----

#### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Key Points in the Markdown:

1. **Project Description**: Explains what the project does, highlighting the use of Python (Flask) for the back-end and React for the front-end.
2. **Technologies Used**: Lists both the back-end and front-end technologies.
3. **Features**: Describes the features of the app, such as displaying available cars for rent.
4. **How to Run the Project**: Provides detailed instructions for running both the back-end and front-end locally.
5. **Project Structure**: Shows how the project files are organized.
6. **How to Contribute**: Explains how others can contribute to the project.
7. **License**: Mentions the MIT license and provides a link to the license file.

This will help users and collaborators understand your project, set it up, and contribute to it easily.

-----

#### Portugues 

# Locadora de Carros 🚗

## Descrição

Este projeto é uma aplicação de locadora de carros, onde é possível visualizar uma lista de carros disponíveis para aluguel. O back-end é desenvolvido em **Python (Flask)** e o front-end em **React** com **Tailwind CSS** para o design responsivo e estilização.

- **Back-end**: API RESTful em Python utilizando o **Flask**.
- **Front-end**: Aplicação em **React** com **Axios** para requisições HTTP e **Tailwind CSS** para o design.

## Tecnologias Usadas

### Back-End
- **Python 3.x**
- **Flask**: Framework web para criar a API.
- **CORS**: Middleware para permitir requisições de origens diferentes.

### Front-End
- **React.js**: Biblioteca JavaScript para construir interfaces de usuário.
- **Tailwind CSS**: Framework de CSS utilitário para estilizar o front-end.
- **Axios**: Biblioteca para fazer requisições HTTP no React.

## Funcionalidades

- Exibe uma lista de carros disponíveis para aluguel.
- Cada carro mostra o nome e o preço diário.
- Permite clicar em "Alugar/Devolver" para interação (sem funcionalidade definida no front-end).

## Estrutura do Projeto

### Back-End (Python + Flask)
1. `app.py`: Arquivo principal da API em Flask.
2. `requirements.txt`: Lista de dependências do back-end.

### Front-End (React + Tailwind CSS)
1. `src/App.js`: Componente principal que faz a requisição dos carros à API e exibe-os.
2. `public/index.html`: Arquivo HTML principal.
3. `tailwind.config.js`: Configurações do Tailwind CSS.

--------

## Como Rodar o Projeto

### 1. Configurar o Back-End (Flask)

##### 1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/locadora-carros.git
  
   cd locadora-carros
 ```

   -----

##### 2 - Instale as dependências do back-end:

  ```bash
pip install -r requirements.txt
  ```

-------

 ##### 3 - Inicie o servidor do Flask:

  ```bash
python app.py
  ```

###### - O servidor estará rodando em http://127.0.0.1:5000/api/carros.

--------

##### 2. Configurar o Front-End (React)
Navegue até a pasta do front-end:

  ```bash
cd front-end
  ```
 - Instale as dependências do front-end:

  ```bash
npm install
  ```

 - Inicie o servidor do React:

  ```bash
npm start
  ```
 - O front-end estará disponível em http://localhost:3000.
   
-------

##### 3. Configurar o CORS
Se você estiver tendo problemas de CORS (Cross-Origin Resource Sharing), como indicado nos logs anteriores, adicione o seguinte no arquivo app.py (back-end):

  ```bash
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
  ```

 - Isso permitirá que o seu front-end (que está rodando em http://localhost:3000) faça requisições para o back-end sem problemas de bloqueio de CORS.

------

##### 4. Testando
 - Com ambos os servidores (back-end e front-end) rodando, acesse http://localhost:3000 no seu navegador e você verá a lista de carros exibida na página inicial.

  ```bash
locadora-carros/
│
├── back-end/                        # Código do servidor Flask
│   ├── app.py                       # Arquivo principal da API
│   └── requirements.txt             # Dependências do back-end
│
├── front-end/                       # Código do front-end React
│   ├── public/
│   │   └── index.html               # HTML principal
│   ├── src/
│   │   ├── App.js                   # Componente principal
│   │   └── index.js                 # Ponto de entrada do React
│   ├── tailwind.config.js           # Configurações do Tailwind CSS
│   └── package.json                 # Dependências do front-end
│
└── README.md                        # Este arquivo
  ```






