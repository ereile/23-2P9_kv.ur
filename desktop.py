import tkinter as tk


class App:
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.title('Решение квадратного уравнения')
        self.master.geometry('500x250')

        self.input_a = tk.Entry(self.master)
        self.input_b = tk.Entry(self.master)
        self.input_c = tk.Entry(self.master)

        self.button = tk.Button(self.master, text='Вычислить')

