import tkinter as tk
from tkinter import filedialog

# Lazy import - only import when needed
# from app.gui.tasks import BaseTask, SentimentTask, ImageTask


class AppController:
    """
    Wires the GUI to tasks (models).
    - Polymorphism: all tasks expose run(data)
    - Encapsulation: selected task kept internal
    """

    def __init__(self):
        self._task = None  # Will hold BaseTask instance
        self.model_var = tk.StringVar(value="Sentiment")

    def select_task(self, name: str):
        # Lazy import to avoid loading ML models at startup
        from app.gui.tasks import SentimentTask, ImageTask

        name = (name or "").lower()
        if name.startswith("sent"):
            print(f"Selecting SentimentTask for model: {name}")
            self._task = SentimentTask()
        elif name.startswith("image"):
            print(f"Selecting ImageTask for model: {name}")
            self._task = ImageTask()
        else:
            raise ValueError(f"Unknown task selected: {name}")
        return self._task

    def current_task(self):
        return self._task

    def run_inference(
        self, input_kind: str, text_value: str = "", image_path: str = ""
    ) -> dict:
        # Always select the correct task based on current model selection
        current_model = self.model_var.get()
        self.select_task(current_model)

        if input_kind == "Text":
            if not text_value.strip():
                raise ValueError("Please enter some text.")
            return self._task.run(text_value)

        if input_kind == "Image":
            if not image_path.strip():
                raise ValueError("Please choose an image file.")
            return self._task.run(image_path)

        raise ValueError("Unsupported input kind.")

    def pick_file(self, parent) -> str:
        return (
            filedialog.askopenfilename(
                parent=parent,
                title="Choose an image",
                filetypes=[
                    ("Image files", "*.jpg *.jpeg *.png *.bmp *.gif"),
                    ("All files", "*.*"),
                ],
            )
            or ""
        )

    @staticmethod
    def model_infos() -> dict:
        return {
            "Sentiment": "Text Sentiment via Transformers. Input: a sentence. Output: label + score.",
            "Image": "Image Classification (MobileViT X-Small). Input: image path. Output: detailed predictions with top 5 possibilities and descriptive analysis of image contents.",
        }

    @staticmethod
    def oop_explanations() -> str:
        return (
            "OOP Concepts Used:\n"
            "• Multiple inheritance: model classes combine HFModelBase + LoggingMixin + CachingMixin.\n"
            "• Multiple decorators: @timed and @validate_input wrap model methods to time & validate inputs.\n"
            "• Encapsulation: private/protected attributes (e.g., _model, _last_result) with getters/setters.\n"
            "• Polymorphism: BaseTask.run() is called uniformly; SentimentTask & ImageTask override run().\n"
            "• Method overriding: each Task implements its own run() for its modality.\n"
        )
