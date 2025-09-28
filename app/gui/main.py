import tkinter as tk
from tkinter import ttk

from app.gui.controllers import AppController
from app.gui.views import InputFrame, OutputFrame, InfoFrame, OOPFrame


def main():
    root = tk.Tk()
    root.title("HIT137 — AI Model Demo (Tkinter)")

    controller = AppController()

    nb = ttk.Notebook(root)
    nb.pack(expand=True, fill="both")

    input_tab = ttk.Frame(nb)
    output_tab = ttk.Frame(nb)
    info_tab = ttk.Frame(nb)
    oop_tab = ttk.Frame(nb)

    nb.add(input_tab, text="Run")
    nb.add(output_tab, text="Output")
    nb.add(info_tab, text="Model Info")
    nb.add(oop_tab, text="OOP Concepts")

    input_frame = InputFrame(input_tab, controller)
    input_frame.pack(expand=True, fill="both", padx=8, pady=8)

    output_frame = OutputFrame(output_tab)
    output_frame.pack(expand=True, fill="both", padx=8, pady=8)

    info_frame = InfoFrame(info_tab, controller)
    info_frame.pack(expand=True, fill="both", padx=8, pady=8)

    oop_frame = OOPFrame(oop_tab, controller)
    oop_frame.pack(expand=True, fill="both", padx=8, pady=8)

    # Menu
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Clear Output", command=output_frame.clear)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=file_menu)

    root.mainloop()


if __name__ == "__main__":
    main()
