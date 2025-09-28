import tkinter as tk
from tkinter import ttk

from app.gui.controllers import AppController
from app.gui.views import InputFrame, OutputFrame, InfoFrame, OOPFrame


def main():
    root = tk.Tk()
    root.title("🤖 HIT137 — AI Model Demo")
    root.geometry("900x700")
    root.minsize(700, 500)

    # Configure style for better appearance
    style = ttk.Style()
    style.theme_use("clam")  # Modern theme

    # Configure custom styles
    style.configure("Accent.TButton", foreground="white")
    style.map(
        "Accent.TButton", background=[("active", "#0078d4"), ("!active", "#106ebe")]
    )

    controller = AppController()

    # Main notebook with custom styling
    nb = ttk.Notebook(root)
    nb.pack(expand=True, fill="both", padx=8, pady=8)

    # Create tabs with icons in names
    input_tab = ttk.Frame(nb)
    output_tab = ttk.Frame(nb)
    info_tab = ttk.Frame(nb)
    oop_tab = ttk.Frame(nb)

    nb.add(input_tab, text="🚀 Run Analysis")
    nb.add(output_tab, text="📊 Output")
    nb.add(info_tab, text="ℹ️ Model Info")
    nb.add(oop_tab, text="🏗️ OOP Concepts")

    # Create frames with notebook reference
    output_frame = OutputFrame(output_tab)
    output_frame.pack(expand=True, fill="both", padx=8, pady=8)

    input_frame = InputFrame(input_tab, controller, output_frame, notebook=nb)
    input_frame.pack(expand=True, fill="both", padx=8, pady=8)

    info_frame = InfoFrame(info_tab, controller)
    info_frame.pack(expand=True, fill="both", padx=8, pady=8)

    oop_frame = OOPFrame(oop_tab, controller)
    oop_frame.pack(expand=True, fill="both", padx=8, pady=8)

    # Enhanced menu
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    # File menu
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="🔄 Clear Output", command=output_frame.clear)
    file_menu.add_separator()
    file_menu.add_command(label="ℹ️ About", command=lambda: show_about(root))
    file_menu.add_separator()
    file_menu.add_command(label="❌ Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=file_menu)

    # View menu
    view_menu = tk.Menu(menubar, tearoff=0)
    view_menu.add_command(label="🚀 Go to Run", command=lambda: nb.select(input_tab))
    view_menu.add_command(
        label="📊 Go to Output", command=lambda: nb.select(output_tab)
    )
    view_menu.add_command(
        label="ℹ️ Go to Model Info", command=lambda: nb.select(info_tab)
    )
    view_menu.add_command(
        label="🏗️ Go to OOP Concepts", command=lambda: nb.select(oop_tab)
    )
    menubar.add_cascade(label="View", menu=view_menu)

    # Status bar
    status_frame = ttk.Frame(root)
    status_frame.pack(fill="x", side="bottom")
    status_label = ttk.Label(
        status_frame, text="Ready - Select a model and run analysis", relief="sunken"
    )
    status_label.pack(side="left", fill="x", expand=True, padx=(4, 0))

    # Version info
    version_label = ttk.Label(status_frame, text="v1.0", relief="sunken")
    version_label.pack(side="right", padx=(0, 4))

    root.mainloop()


def show_about(parent):
    """Show about dialog"""
    from tkinter import messagebox

    messagebox.showinfo(
        "About HIT137 AI Demo",
        "🤖 HIT137 Assignment 3 - AI Model Demo\n\n"
        "Features:\n"
        "• Sentiment Analysis with DistilBERT\n"
        "• Image Classification with MobileViT\n"
        "• Object-Oriented Programming Concepts\n"
        "• User-friendly Tkinter GUI\n\n"
        "Developed with ❤️ for HIT137",
    )


if __name__ == "__main__":
    main()
