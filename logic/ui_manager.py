# ui_manager.py
import tkinter as tk
from logic.task_manager import get_tasks, remove_task, mark_task_completed

def update_task_listbox(listbox, app):
    # Elimina todos los widgets actuales en la lista para actualizarla
    for widget in listbox.winfo_children():
        widget.destroy()

    # Recorre todas las tareas y las muestra en la lista con botones
    for i, task in enumerate(get_tasks()):
        # Alternar colores de fondo para las tareas (default o verde si está completada)
        bg_color = "#E0E0E0" if i % 2 == 0 else "#F5F5F5"
        if task.get("completed"):
            bg_color = "#A9DFBF"  # Verde si la tarea está completada

        # Crear un frame para cada tarea con un color de fondo
        task_frame = tk.Frame(listbox, bg=bg_color)
        task_frame.pack(fill=tk.X, padx=5, pady=5)

        # Etiqueta para el texto de la tarea
        task_label = tk.Label(task_frame, text=task["text"], font=('JetBrains Mono', 12), anchor="w", bg=bg_color)
        task_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Botón para eliminar la tarea
        delete_button = tk.Button(task_frame, text="Delete", command=lambda t_id=task["id"]: delete_task(t_id, listbox, app))
        delete_button.pack(side=tk.RIGHT)

        # Botón para completar la tarea
        complete_button = tk.Button(task_frame, text="Completar", command=lambda t_id=task["id"]: complete_task(t_id, listbox, app))
        complete_button.pack(side=tk.RIGHT, padx=5)

def delete_task(task_id, listbox, app):
    # Elimina la tarea del task_manager y actualiza la lista
    remove_task(task_id)
    update_task_listbox(listbox, app)

def complete_task(task_id, listbox, app):
    # Marca la tarea como completada y actualiza la lista
    mark_task_completed(task_id)
    update_task_listbox(listbox, app)
    
def create_add_task_button(app, x, y, command):
    add_button = tk.Button(app, text="Añadir Tarea", command=command, width=15, height=1)
    add_button.place(x=x, y=y)
