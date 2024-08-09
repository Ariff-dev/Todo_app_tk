# title_style.py
import tkinter as tk
from assets.styles.round_rectangle import round_rectangle

def create_title(app, text, x, y, width=250, height=50, radius=20, bg="#007EA7", fg="white", font=('JetBrains Mono', 14, 'bold')):
    # Crear un canvas para el label redondeado
    canvas = tk.Canvas(app, width=width, height=height, bg=app["bg"], highlightthickness=0)
    canvas.place(x=x, y=y)

    # Dibujar un rectángulo con bordes redondeados
    round_rectangle(canvas, 0, 0, width, height, radius=radius, fill=bg, outline=bg)

    # Colocar texto encima del rectángulo redondeado
    canvas.create_text(width // 2, height // 2, text=text, fill=fg, font=font)
