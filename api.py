from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import JSONResponse
from typing_extensions import Annotated
from pydantic import BaseModel, StringConstraints, field_validator
import database as db
import helpers

class ModeloCliente(BaseModel):
    dni: Annotated[str, StringConstraints(min_length=4, max_length=4)]
    nombre: Annotated[str, StringConstraints(min_length=2, max_length=30)]
    apellido: Annotated[str, StringConstraints(min_length=2, max_length=30)]

class ModeloCrearCliente(ModeloCliente):
    @field_validator('dni')
    def validar_este_dni(cls, dni):
        if helpers.validar_dni(dni, db.Clientes.lista):
            return dni
        raise ValueError ("DNI incorrecto o Cliente ya existente, intenta nuevamente")


app = FastAPI(
    title='API del Gestor de Clientes',
    description= "Ofrece distintas funciones para gestionar clientes."
)


@app.get('/clientes/', tags=["Clientes"])
async def clientes():
    content=[cliente.to_dict() for cliente in db.Clientes.lista]
    return JSONResponse(content=content)

@app.get('/clientes/buscar/{dni}/', tags=["Clientes"])
async def clientes_buscar(dni:str):
    cliente = db.Clientes.buscar(dni=dni)
    if not cliente:
        raise HTTPException(status_code=404, detail="Los sentimos, cliente no encontrado")
    return JSONResponse(content=cliente.to_dict())

@app.post('/clientes/crear/', tags=["Clientes"])
async def clientes_crear(datos: ModeloCrearCliente):
    cliente= db.Clientes.crear(datos.dni, datos.nombre, datos.apellido)
    if cliente:
        return JSONResponse(content=cliente.to_dict())
    raise HTTPException(status_code=404, detail="Los sentimos, cliente no creado")
    return

@app.put('/clientes/actualizar/', tags=["Clientes"])
async def clientes_actualizar(datos: ModeloCliente):
    if db.Clientes.buscar(datos.dni):
        cliente = db.Clientes.modificar(datos.dni, datos.nombre, datos.apellido)
        if cliente:
            return JSONResponse(content=cliente.to_dict())
    raise HTTPException(status_code=404, detail="Los sentimos, cliente no encontrado")

@app.delete('/cliente/borrar/{dni}', tags=["Clientes"])
async def clientes_borrar(dni: str):
    if db.Clientes.buscar(dni):
        cliente = db.Clientes.borrar(dni=dni)
        return JSONResponse(content=cliente.to_dict())
    raise HTTPException(status_code=404, detail="Los sentimos, cliente no encontrado")

print("Servidor de la API...")