import tkinter as tk

def create_add_task_button(app, x, y, text="Add Task +", command=None, bg="#272727", fg="white", font=('JetBrains Mono', 12, 'bold')):
    # Crear un botón en la ventana principal
    button = tk.Button(
        app,
        text=text,
        command=command,
        bg=bg,
        fg=fg,
        font=font
    )
    
    # Configurar el tamaño exacto del botón en píxeles
    button.config(width=150, height=28)

    # Usar `place` para posicionar el botón en la ventana principal
    button.place(x=x, y=y, width=150, height=28)
    
    return button
