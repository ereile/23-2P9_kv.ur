"""TKINTER"""

import tkinter as tk
from main import kv_ur


class App(tk.Tk):
    """APP"""
    def __init__(self):
        super().__init__()
        self.title('Решение квадратного уравнения')
        self.geometry('500x250')

        self.input_a = tk.Entry(self)
        self.input_b = tk.Entry(self)
        self.input_c = tk.Entry(self)
        self.solution_label = tk.Label(self.master, text='')
        self.callback_a_label = tk.Label(self)
        self.callback_b_label = tk.Label(self)
        self.callback_c_label = tk.Label(self)
        self.button = tk.Button(self.master,
                                text='Вычислить',
                                command=self.solution
                                )
        self.inputs = [
            (self.input_a, self.callback_a_label),
            (self.input_b, self.callback_b_label),
            (self.input_c, self.callback_c_label)
            ]

        self.callback_a_label.pack()
        self.input_a.pack()
        self.callback_b_label.pack()
        self.input_b.pack()
        self.callback_c_label.pack()
        self.input_c.pack()
        self.button.pack()
        self.solution_label.pack()

    def input_callback(self, label: tk.Label):
        """Except callback"""
        label.config(text="""↓ Некорректное значение""")

    def solution(self):
        """solution"""

        params = []
        flag = True
        for [input_el, label] in self.inputs:
            try:
                params.append(int(input_el.get()))

            except ValueError:
                self.input_callback(label)
                flag = False
                break

        if flag:
            for lst in self.inputs:
                lst[1].config(text='')

            self.solution_label.config(text=str(
                                       kv_ur(
                                        params[0],
                                        params[1],
                                        params[2]
                                        )))


if __name__ == '__main__':
    app = App()
    app.mainloop()
