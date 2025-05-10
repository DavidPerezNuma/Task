from controller.controller import Controller
from view.view import View

def main():
    controller = Controller()
    view = View()

    while True:
        view.show_menu()
        choice = view.get_input("Seleccione una opción: ")

        if choice == "1":
            view.show_tasks(controller.get_tasks())
        elif choice == "2":
            title = view.get_input("Título: ")
            description = view.get_input("Descripción: ")
            controller.add_task(title, description)
        elif choice == "3":
            index = int(view.get_input("Número de tarea a editar: ")) - 1
            new_title = view.get_input("Nuevo título: ")
            new_description = view.get_input("Nueva descripción: ")
            controller.edit_task(index, new_title, new_description)
        elif choice == "4":
            index = int(view.get_input("Número de tarea a eliminar: ")) - 1
            controller.delete_task(index)
        elif choice == "5":
            index = int(view.get_input("Número de tarea a completar: ")) - 1
            controller.complete_task(index)
        elif choice == "6":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
