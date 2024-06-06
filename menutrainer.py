presentacion_trainer=open("presentacion_trainer.txt", "r")
safe=(presentacion_trainer.read())
print(safe)

eleccion = int(input("Ingrese el numero de la accion que desea ejecutar"))
if eleccion ==1:
    presentacion_camper=open("horario.txt.", "r")
aseguradora=(presentacion_camper.read())
print(aseguradora)