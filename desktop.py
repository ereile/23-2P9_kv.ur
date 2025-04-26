"""TKINTER"""

import tkinter as tk
from main import kv_ur


class App:
    """_summary_
    """
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.title('Решение квадратного уравнения')
        self.master.geometry('500x250')

        self.input_a = tk.Entry(self.master)
        self.input_b = tk.Entry(self.master)
        self.input_c = tk.Entry(self.master)
        self.label = tk.Label(self.master, text='')

        self.input_a.pack()
        self.input_b.pack()
        self.input_c.pack()

        self.button = tk.Button(self.master,
                                text='Вычислить',
                                command=self.solution
                                )

        self.button.pack()
        self.label.pack()

    def solution(self):
        """_summary_"""

        try:
            a = int(self.input_a.get())
            b = int(self.input_b.get())
            c = int(self.input_c.get())
            self.label.config(text=str(kv_ur(a, b, c)))

        except ValueError:
            pass


root = tk.Tk()
app = App(root)
root.mainloop()
