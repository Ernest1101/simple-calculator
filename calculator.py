import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("320x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        # Экран (поле ввода)
        self.display = tk.Entry(
            root,
            font=("Arial", 24),
            justify="right",
            bd=0,
            relief=tk.FLAT,
            bg="#f0f0f0",
            fg="#000"
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=20, pady=(20, 10), sticky="nsew")

        # Кнопки
        buttons = [
            ('C', 1, 0, "#ff4d4d"), ('±', 1, 1, "#e0e0e0"), ('%', 1, 2, "#e0e0e0"), ('÷', 1, 3, "#ff9933"),
            ('7', 2, 0, "#e0e0e0"), ('8', 2, 1, "#e0e0e0"), ('9', 2, 2, "#e0e0e0"), ('×', 2, 3, "#ff9933"),
            ('4', 3, 0, "#e0e0e0"), ('5', 3, 1, "#e0e0e0"), ('6', 3, 2, "#e0e0e0"), ('-', 3, 3, "#ff9933"),
            ('1', 4, 0, "#e0e0e0"), ('2', 4, 1, "#e0e0e0"), ('3', 4, 2, "#e0e0e0"), ('+', 4, 3, "#ff9933"),
            ('0', 5, 0, "#e0e0e0", 2), ('.', 5, 2, "#e0e0e0"), ('=', 5, 3, "#ff9933")
        ]

        for btn in buttons:
            if len(btn) == 4:
                text, row, col, bg = btn
                colspan = 1
            else:
                text, row, col, bg, colspan = btn

            tk.Button(
                root,
                text=text,
                font=("Arial", 18),
                bg=bg,
                fg="#000" if bg != "#ff4d4d" else "#fff",
                activebackground="#d4d4d4",
                relief=tk.FLAT,
                command=lambda t=text: self.on_button_click(t)
            ).grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")

        # Настройка растягивания сетки
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)

        self.current_input = ""
        self.last_result = None

    def on_button_click(self, char):
        if char == 'C':
            self.display.delete(0, tk.END)
            self.current_input = ""
        elif char == '±':
            try:
                current = self.display.get()
                if current:
                    if current.startswith('-'):
                        self.display.delete(0, tk.END)
                        self.display.insert(0, current[1:])
                    else:
                        self.display.insert(0, '-')
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Ошибка")
        elif char == '=':
            try:
                expr = self.display.get().replace('×', '*').replace('÷', '/')
                result = eval(expr)
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                messagebox.showerror("Ошибка", "Неверное выражение")
        else:
            if char in '0123456789':
                self.display.insert(tk.END, char)
            elif char == '.':
                if '.' not in self.display.get().split()[-1:]:
                    self.display.insert(tk.END, '.')
            else:
                self.display.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
