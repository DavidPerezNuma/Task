# Task 📝

**Task** es una aplicación de línea de comandos para gestionar tareas. Permite a los usuarios agregar, editar, eliminar y marcar como completadas sus tareas diarias de forma sencilla, utilizando el patrón de diseño MVC (Modelo-Vista-Controlador).

---

## 📌 Descripción

Task es una aplicación minimalista desarrollada en Python que ayuda a los usuarios a mantener el control de sus pendientes. Es ideal como ejemplo académico del patrón arquitectónico MVC y puede servir como base para proyectos más complejos o para migrar a una interfaz gráfica más adelante.

---

## 📁 Estructura del Proyecto

```

task\_manager/
│
├── model/
│   └── task.py               # Clase Task (modelo)
│
├── view/
│   └── view\.py               # Vista (interacción con el usuario)
│
├── controller/
│   └── controller.py         # Controlador (gestiona la lógica)
│
├── test/
│   └── pruebas\_funcionales.txt     # Manual de pruebas funcionales
│   └── script\_pruebas.py          # Script para ejecutar pruebas funcionales
│
├── main.py                   # Punto de entrada de la aplicación

````

---

## 🎯 Patrón MVC en este Proyecto

**Modelo (Model):**
- Definido en `model/task.py`.
- Contiene la clase `Task` con los atributos `title`, `description` y `completed`.
- Maneja la lógica de negocio y la estructura de los datos.

**Vista (View):**
- Implementada en `view/view.py`.
- Se encarga de mostrar información al usuario y recibir sus entradas (interfaz de texto).
- No contiene lógica de negocio.

**Controlador (Controller):**
- Se encuentra en `controller/controller.py`.
- Orquesta la interacción entre el modelo y la vista.
- Contiene métodos para agregar, editar, eliminar y completar tareas.

---

## 🚀 Cómo ejecutar el proyecto

### ✅ Opción 1: Ejecución manual

Desde la raíz del proyecto, ejecuta:

```bash
python main.py
````

Sigue el menú interactivo para gestionar tus tareas desde la terminal.

---

### 🧪 Opción 2: Ejecutar pruebas funcionales

Para validar que la aplicación funciona correctamente según el manual de pruebas, ejecuta:

```bash
python script_pruebas.py
```

Esto simula las acciones descritas en `pruebas_funcionales.txt`.

> Nota: Asegúrate de tener Python 3 instalado y configurado en tu entorno, Ademas de que en la pruebas automaticas debemo pararnos en el directorio de test para ejecutarla.

---

## 📄 Licencia

Este proyecto es de libre uso con fines educativos.

---

## ✍️ Autor

Desarrollado por \[Juan david Perez Numa - Anner alexis Carabali Banguera].

