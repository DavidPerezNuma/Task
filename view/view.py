class View:
    @staticmethod
    def show_menu():
        print("\n--- Lista de Tareas ---")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Editar tarea")
        print("4. Eliminar tarea")
        print("5. Marcar como completada")
        print("6. Salir")

    @staticmethod
    def show_tasks(tasks):
        if not tasks:
            print("No hay tareas registradas.")
        else:
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")

    @staticmethod
    def get_input(prompt):
        return input(prompt)
