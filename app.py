import tkinter as tk
from components.title import create_title
from logic.ui_manager import create_add_task_button, update_task_listbox
from logic.task_manager import add_task

def add_task_command(entry, listbox, app):
    task = entry.get()
    if task:
        add_task(task)
        entry.delete(0, tk.END)
        update_task_listbox(listbox, app)

app = tk.Tk()
app.wm_title("Todo App")
app.geometry("410x820")
app.configure(background="#CCDBDC")

# Crear el título de la aplicación
create_title(app, "Todo App", 20, 20)

# Campo de entrada para agregar nuevas tareas
entry = tk.Entry(app, font=('JetBrains Mono', 12))
entry.place(x=20, y=80, width=200, height=28)

# Frame donde se mostrará la lista de tareas
listbox = tk.Frame(app, background="#EDEDED")
listbox.place(x=20, y=120, width=370, height=680)

# Botón para añadir nuevas tareas
create_add_task_button(app, 240, 80, command=lambda: add_task_command(entry, listbox, app))

# Actualizar la lista de tareas al iniciar la aplicación
update_task_listbox(listbox, app)

app.mainloop()
