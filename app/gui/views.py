import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox


class InputFrame(ttk.Frame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = controller

        # Model selection
        ttk.Label(self, text="Select Model:").grid(row=0, column=0, sticky="w")
        self.model_combo = ttk.Combobox(
            self,
            textvariable=controller.model_var,
            values=["Sentiment", "Image"],
            state="readonly",
        )
        self.model_combo.grid(row=0, column=1, sticky="we", padx=4)
        self.model_combo.bind("<<ComboboxSelected>>", self._on_model_change)

        # Input type
        ttk.Label(self, text="Input Type:").grid(row=1, column=0, sticky="w")
        self.input_var = tk.StringVar(value="Text")
        self.input_combo = ttk.Combobox(
            self,
            textvariable=self.input_var,
            values=["Text", "Image"],
            state="readonly",
        )
        self.input_combo.grid(row=1, column=1, sticky="we", padx=4)
        self.input_combo.bind("<<ComboboxSelected>>", self._sync_inputs)

        # Text input
        ttk.Label(self, text="Text:").grid(row=2, column=0, sticky="nw")
        self.text_entry = scrolledtext.ScrolledText(self, width=40, height=6)
        self.text_entry.grid(row=2, column=1, sticky="we", padx=4, pady=4)

        # Image picker
        self.image_path = tk.StringVar()
        ttk.Label(self, text="Image path:").grid(row=3, column=0, sticky="w")
        row3 = ttk.Frame(self)
        row3.grid(row=3, column=1, sticky="we", padx=4)
        self.image_entry = ttk.Entry(row3, textvariable=self.image_path)
        self.image_entry.pack(side="left", expand=True, fill="x")
        ttk.Button(row3, text="Browse", command=self._browse).pack(side="left", padx=4)

        # Buttons
        btns = ttk.Frame(self)
        btns.grid(row=4, column=0, columnspan=2, sticky="e", pady=6)
        ttk.Button(btns, text="Run", command=self._run).pack(side="left", padx=4)
        ttk.Button(btns, text="Clear", command=self._clear).pack(side="left", padx=4)

        self.columnconfigure(1, weight=1)
        self._on_model_change()

    def _on_model_change(self, *_):
        name = self.controller.model_var.get()
        # Don't create task immediately - wait until run is pressed
        self.input_var.set("Text" if name == "Sentiment" else "Image")
        self._sync_inputs()

    def _sync_inputs(self, *_):
        if self.input_var.get() == "Text":
            self.text_entry.configure(state="normal")
        else:
            self.text_entry.configure(state="disabled")

    def _browse(self):
        path = self.controller.pick_file(self)
        if path:
            self.image_path.set(path)

    def _clear(self):
        self.text_entry.delete("1.0", "end")
        self.image_path.set("")

    def _run(self):
        try:
            res = self.controller.run_inference(
                input_kind=self.input_var.get(),
                text_value=self.text_entry.get("1.0", "end").strip(),
                image_path=self.image_path.get(),
            )
            # send result to Output tab
            self.master.event_generate("<<ShowResult>>", when="tail", data=str(res))
        except Exception as e:
            messagebox.showerror("Run Error", str(e))


class OutputFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        ttk.Label(self, text="Output:").pack(anchor="w")
        self.out = scrolledtext.ScrolledText(self, width=60, height=12)
        self.out.pack(expand=True, fill="both", padx=4, pady=4)
        self.master.bind("<<ShowResult>>", self._on_result)

    def _on_result(self, event):
        self.out.insert("end", event.data + "\n")
        self.out.see("end")

    def clear(self):
        self.out.delete("1.0", "end")


class InfoFrame(ttk.Frame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        ttk.Label(self, text="Model Info:").pack(anchor="w")
        self.text = scrolledtext.ScrolledText(self, width=60, height=12)
        self.text.pack(expand=True, fill="both", padx=4, pady=4)
        infos = controller.model_infos()
        for k, v in infos.items():
            self.text.insert("end", f"{k}: {v}\n\n")
        self.text.configure(state="disabled")


class OOPFrame(ttk.Frame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        ttk.Label(self, text="OOP Concepts Used:").pack(anchor="w")
        self.text = scrolledtext.ScrolledText(self, width=60, height=14)
        self.text.pack(expand=True, fill="both", padx=4, pady=4)
        self.text.insert("end", controller.oop_explanations())
        self.text.configure(state="disabled")
