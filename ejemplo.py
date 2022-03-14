

def funcion():
    return "El mundo es hermoso y la tierra es verde y azul"


if __name__ == "__main__":
    print("Con git clone se trae el proyecto desde github")
    print("Ejemplo: git clone https://github.com/amurer808/proyecto_de_prueba.git")
    print()

    print("Con git status se muestra el estado de los archivos: los que estan guardados (en verde) y los que no (en rojo) (los tracked y los untracked)")
    print("Ejemplo: git status")
    print()

    print("Con git add se revisan los archivos para guardarlos")
    print("Ejemplo: git add ejemplo.py")
    print("git add * : guarda todos los archivos modificados")
    print()

    print("Para registrar los cambios y hacer un estado utilizo git commit")
    print('Ejemplo: git commit -m "Mensaje"')
    print()

    print("Para subir los cambios a github se usa el git push")
    print("Ejemplo: git push")
    print()

    print("Llamando a funcion:", funcion())

    print("Para actualizar los cambios de github se usa el git pull")
    print("Ejemplo: git pull")
    print()