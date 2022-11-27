from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4



app = FastAPI()

class User(BaseModel):
  id: int
  name: str | None = 'Fulanito'
  lastName: str | None = 'De tal'
  email: str | None = 'fula@gmail.com'
  password: str | None = '123'
  address: str | None = 'Avenida siempreviva'
  role: str | None = 'client'

class Car(BaseModel):
  id: int
  name: str | None = 'Chevrolito'
  model: int | None = 1970
  price: int 
  color: str
  category: str | None = 'ligeros'#ligeros,pesados, especiales, agrícola,
  status: str | None = 'new' #used



#User's Endpoints
users = []
@app.post('/users')
async def save_user(user: User,name: str,lastName: str,email: str,password: str,address: str):
  user.id = int(uuid4())
  users.append(user.dict())
  return f'El usuario  ha sido registrado satisfactoriamente. {user.id}'

@app.post('/users/login')
async def log_in(user: User, email: str,password: str):
  for user in users:
    if user['email'] == email and user['password'] == password:
      return {'message':'Logged in successful'}




#Compras al nivel de usuario y  al nivel del negocio.



#Car's Endpoints
cars = []
@app.post('/cars')
async def save_car(car: Car,price: int,color: str):
  car.id = int(uuid4())
  cars.append(car.dict())
  return f'Car creado {car.name} {car.id} {car.color}'


@app.get('/cars/{id}')
async def get_car(id:int):
  for car in cars:
    if car['id'] == id:
      return car 
  return f'Car not found'

  


@app.get('/car/compare/{id1}-{id2}')
async def comparation(id1: int,id2: int):
  newList = []
  for car1,car2 in cars:
    if car1['id'] ==  id1:
      newList.append(car1.dict())
    if car2['id'] ==  id2:
      newList.append(car2.dict())
  return newList


"""
Estado de vehiculos  Nuevo | Usado
Categorias =>  ligeros,pesados, especiales, agrícola, otros(description).

"""

#Creamos el entorno virtual =>  python -m venv env
#Luego lo activamos con el comando =>  env\Scripts\activate
#requirements.txt:

#Instalamos las dependencias =>  pip install -r requirements.txt --no-cache-dir
#Ejecutamos  uvicorn  para enecender el servidor =>  uvicorn main:app --reload
#Actualizar pip =>  python -m pip install --upgrade pip
#Resolver problemas de scripts =>  set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser










#Creamos el entorno virtual =>  python -m venv env
#Luego lo activamos con el comando =>  env\Scripts\activate
#requirements.txt:

#Instalamos las dependencias =>  pip install -r requirements.txt --no-cache-dir
#Ejecutamos  uvicorn  para enecender el servidor =>  uvicorn main:app --reload
#Actualizar pip =>  python -m pip install --upgrade pip
#Resolver problemas de scripts =>  set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser



git remoto agregar origen https://github.com/JoseMiguelFuentes/Get-a-Car.git
git branch -M principal 
git push -u origen principal

