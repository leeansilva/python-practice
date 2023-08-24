from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn

app = FastAPI()
lista = []

@app.get('/')
def leerTodo():
  return lista

@app.get('/{id}')
def leerUno(id):
  return lista[int(id)]

@app.post('/')
def crear(dato):
  lista.append(dato)
  return PlainTextResponse(f'Se creo el elemento {lista[-1]}')

@app.put('/{id}')
def actualizar(id,dato):
  lista[int(id)] = dato
  return PlainTextResponse(f'Se actualizo el elemento {id}')

@app.delete('/{id}')
def borrar(id):
  lista.pop(int(id))
  return PlainTextResponse(f'Se borro el elemento {id}')

if __name__ == '__main__':
  uvicorn.run('main:app', reload=True)

