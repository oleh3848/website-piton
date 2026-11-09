import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO


text=input("Введи текст=   "  )
root= tk.Tk()
root.title("Cat Generator")
root.geometry("450x600")

title= tk.Label(root,text="Генератор котів ", font=("Arial",18,"bold"))
title.pack(pady=15)
image_label=tk.Label(root)
image_label.pack(pady=15)

status=tk.Label(root, text="Натисни кнопку!")
status.pack(pady=10)


def get_cat():
    global photo
    status.config(text="Завантаження. . . . . .")
    url=f"https://cataas.com/cat/says/{text}"
    response = requests.get(url, timeout=15)
    image=Image.open(BytesIO(response.content))
    image.thumbnail((350, 280))
    photo=ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    status.config(text="У нас новий кіт")
button=tk.Button(
    root,
    text="Показати кота ",
    font=("arial",14),
    command=get_cat
)
button.pack(pady=15)

















root.mainloop()