API del Gestor de Clientes

Este proyecto es una API web creada con FastAPI para gestionar clientes, permitiendo realizar operaciones básicas como `GET`, `POST`, `PUT`, y `DELETE`.

## Requisitos

- Python 
- pipenv
- FastAPI
- Uvicorn

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Renehdez-97/API-del-Gestor-Clientes.git
2. Instala las dependencias:
    ```bash
    pipenv install
## Ejecución
Inicia el servidor:
  ```bash
      pipenv run uvicorn api:app --reload
  ```
## Documentación
Accede a la documentación interactiva en:
  ```bash
  http://127.0.0.1:8000/docs
  ```
## Endpoints
GET /clientes: Obtiene la lista de clientes.

POST /clientes: Crea un nuevo cliente.

PUT /clientes/{id}: Actualiza un cliente existente.

DELETE /clientes/{id}: Elimina un cliente.
