import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading


class InputFrame(ttk.Frame):
    def __init__(self, master, controller, output_frame=None, notebook=None, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = controller
        self.output_frame = output_frame
        self.notebook = notebook  # Reference to notebook for tab switching

        # Status frame at top
        status_frame = ttk.Frame(self)
        status_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 10))
        self.status_label = ttk.Label(status_frame, text="Ready", foreground="green")
        self.status_label.pack(side="left")
        self.progress = ttk.Progressbar(status_frame, mode="indeterminate")
        self.progress.pack(side="right", padx=(10, 0))

        # Model selection
        ttk.Label(self, text="Select Model:").grid(row=1, column=0, sticky="w")
        self.model_combo = ttk.Combobox(
            self,
            textvariable=controller.model_var,
            values=["Sentiment", "Image"],
            state="readonly",
        )
        self.model_combo.grid(row=1, column=1, sticky="we", padx=4)
        self.model_combo.bind("<<ComboboxSelected>>", self._on_model_change)

        # Dynamic input sections (will be shown/hidden based on model)
        # Text input section
        self.text_frame = ttk.LabelFrame(self, text="Text Input", padding=10)
        self.text_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=4, pady=8)
        self.text_frame.columnconfigure(0, weight=1)

        ttk.Label(self.text_frame, text="Enter text to analyze:").grid(
            row=0, column=0, sticky="w"
        )
        self.text_entry = scrolledtext.ScrolledText(self.text_frame, width=50, height=4)
        self.text_entry.grid(row=1, column=0, sticky="ew", pady=(5, 0))
        self.text_entry.insert(
            "1.0", "I love this project! It's amazing and works perfectly."
        )

        # Image input section
        self.image_frame = ttk.LabelFrame(self, text="Image Input", padding=10)
        self.image_frame.grid(
            row=3, column=0, columnspan=2, sticky="ew", padx=4, pady=8
        )
        self.image_frame.columnconfigure(0, weight=1)

        ttk.Label(self.image_frame, text="Select an image to classify:").grid(
            row=0, column=0, sticky="w"
        )

        img_row = ttk.Frame(self.image_frame)
        img_row.grid(row=1, column=0, sticky="ew", pady=(5, 0))
        img_row.columnconfigure(0, weight=1)

        self.image_path = tk.StringVar()
        self.image_entry = ttk.Entry(img_row, textvariable=self.image_path)
        self.image_entry.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        ttk.Button(img_row, text="Browse", command=self._browse).grid(row=0, column=1)

        # Set default image path
        self.image_path.set("assets/sample.jpg")

        # Buttons
        btns = ttk.Frame(self)
        btns.grid(row=4, column=0, columnspan=2, sticky="e", pady=15)
        self.run_btn = ttk.Button(
            btns, text="🚀 Run Analysis", command=self._run, style="Accent.TButton"
        )
        self.run_btn.pack(side="left", padx=4)
        ttk.Button(btns, text="Clear", command=self._clear).pack(side="left", padx=4)
        ttk.Button(btns, text="View Output", command=self._switch_to_output).pack(
            side="left", padx=4
        )

        self.columnconfigure(1, weight=1)

        # Initialize model selection
        self.model_combo.set("Sentiment")  # Set default
        self._on_model_change()

    def _on_model_change(self, *_):
        """Show/hide input sections based on selected model"""
        model_name = self.controller.model_var.get()

        if model_name == "Sentiment":
            # Show text input, hide image input
            self.text_frame.grid()
            self.image_frame.grid_remove()
            self.status_label.configure(
                text=f"Selected: {model_name} Analysis - Enter text above",
                foreground="blue",
            )
        elif model_name == "Image":
            # Show image input, hide text input
            self.text_frame.grid_remove()
            self.image_frame.grid()
            self.status_label.configure(
                text=f"Selected: {model_name} Classification - Select image above",
                foreground="blue",
            )
        else:
            # Show both if no model selected
            self.text_frame.grid()
            self.image_frame.grid()
            self.status_label.configure(
                text="Please select a model", foreground="orange"
            )

    def _browse(self):
        path = self.controller.pick_file(self)
        if path:
            self.image_path.set(path)
            self.status_label.configure(
                text=f"Image selected: {path.split('/')[-1]}", foreground="green"
            )

    def _clear(self):
        self.text_entry.delete("1.0", "end")
        self.image_path.set("assets/sample.jpg")
        self.status_label.configure(text="Inputs cleared", foreground="green")
        # Re-add sample text for sentiment
        if self.controller.model_var.get() == "Sentiment":
            self.text_entry.insert(
                "1.0", "I love this project! It's amazing and works perfectly."
            )

    def _switch_to_output(self):
        """Switch to output tab"""
        if self.notebook:
            self.notebook.select(1)  # Select output tab (index 1)

    def _run(self):
        """Run inference with improved UX"""
        model_name = self.controller.model_var.get()

        if not model_name:
            messagebox.showwarning("No Model", "Please select a model first!")
            return

        # Determine input type and validate
        if model_name == "Sentiment":
            text_input = self.text_entry.get("1.0", "end").strip()
            if not text_input:
                messagebox.showwarning("No Input", "Please enter some text to analyze!")
                return
            input_kind = "Text"
            image_path = ""
        else:  # Image
            image_path = self.image_path.get().strip()
            if not image_path:
                messagebox.showwarning("No Input", "Please select an image file!")
                return
            input_kind = "Image"
            text_input = ""

        # Start processing animation
        self.status_label.configure(
            text=f"Processing with {model_name} model...", foreground="orange"
        )
        self.progress.start(10)
        self.run_btn.configure(state="disabled", text="Processing...")

        # Update UI
        self.update()

        def run_inference():
            try:
                res = self.controller.run_inference(
                    input_kind=input_kind,
                    text_value=text_input,
                    image_path=image_path,
                )

                # Update UI in main thread
                self.after(0, self._inference_complete, res, None)

            except Exception as e:
                self.after(0, self._inference_complete, None, str(e))

        # Run in background thread to prevent UI freezing
        threading.Thread(target=run_inference, daemon=True).start()

    def _inference_complete(self, result, error):
        """Called when inference is complete"""
        # Stop progress animation
        self.progress.stop()
        self.run_btn.configure(state="normal", text="🚀 Run Analysis")

        if error:
            self.status_label.configure(text=f"Error: {error}", foreground="red")
            messagebox.showerror("Processing Error", error)
        else:
            self.status_label.configure(
                text="✅ Analysis complete! Check Output tab", foreground="green"
            )

            # Send result to output frame
            if self.output_frame:
                model_name = self.controller.model_var.get()
                self.output_frame.display_result(result, model_name)

            # Show notification and offer to switch to output tab
            if messagebox.askyesno(
                "Analysis Complete",
                "Analysis finished successfully!\n\nWould you like to view the results in the Output tab?",
            ):
                self._switch_to_output()


class OutputFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Header with status
        header = ttk.Frame(self)
        header.pack(fill="x", padx=4, pady=(4, 0))

        ttk.Label(
            header, text="Analysis Results:", font=("TkDefaultFont", 10, "bold")
        ).pack(side="left")
        self.result_count_label = ttk.Label(
            header, text="No results yet", foreground="gray"
        )
        self.result_count_label.pack(side="right")

        # Output text area with better styling
        self.out = scrolledtext.ScrolledText(
            self,
            width=70,
            height=15,
            wrap=tk.WORD,
            font=("Consolas", 10),
            relief="sunken",
            borderwidth=2,
        )
        self.out.pack(expand=True, fill="both", padx=4, pady=4)

        # Add welcome message
        welcome_msg = """🤖 AI Model Analysis Results will appear here

• Select a model and provide input in the 'Run' tab
• Click 'Run Analysis' to process your input
• Results will automatically appear here with timestamps

Ready for analysis! 🚀
"""
        self.out.insert("1.0", welcome_msg)
        self.out.configure(state="disabled")

        self.result_count = 0
        self.master.bind("<<ShowResult>>", self._on_result)

    def _on_result(self, event):
        self.out.configure(state="normal")
        self.out.insert("end", event.data + "\n")
        self.out.see("end")
        self.out.configure(state="disabled")

    def display_result(self, result, model_name=None):
        """Display result with proper formatting based on model type"""
        import datetime

        self.out.configure(state="normal")

        # Clear welcome message on first result
        if self.result_count == 0:
            self.out.delete("1.0", "end")

        self.result_count += 1
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")

        # Add formatted result with separator
        separator = "=" * 60
        header = f"\n{separator}\n🔍 Analysis #{self.result_count} - {timestamp}\n{separator}\n"

        self.out.insert("end", header)

        # Format output based on model type
        if model_name == "Image" and isinstance(result, dict):
            self._format_image_result(result)
        elif model_name == "Sentiment" and isinstance(result, dict):
            self._format_sentiment_result(result)
        else:
            # Fallback to string representation
            self.out.insert("end", f"{result}\n")

        self.out.see("end")
        self.out.configure(state="disabled")

        # Update result count
        self.result_count_label.configure(
            text=f"{self.result_count} result{'s' if self.result_count != 1 else ''}",
            foreground="green",
        )

    def _format_image_result(self, result):
        """Format image classification results with enhanced details"""
        # Main classification
        main_label = result.get("label", "Unknown")
        main_score = result.get("score", 0.0)

        self.out.insert("end", f"🖼️  IMAGE CLASSIFICATION RESULTS\n\n")
        self.out.insert("end", f"Primary Classification: {main_label.title()}\n")
        self.out.insert("end", f"Confidence: {main_score:.1%}\n\n")

        # Description if available
        if "description" in result:
            self.out.insert("end", f"📝 Description:\n{result['description']}\n\n")

        # Top predictions if available
        if "top_predictions" in result:
            self.out.insert("end", f"🏆 Top Predictions:\n")
            for i, pred in enumerate(result["top_predictions"], 1):
                label = pred["label"].title()
                score = pred["score"]
                confidence_bar = "█" * int(score * 20)  # Visual confidence bar
                self.out.insert(
                    "end", f"  {i}. {label:<20} {score:>6.1%} {confidence_bar}\n"
                )

    def _format_sentiment_result(self, result):
        """Format sentiment analysis results"""
        label = result.get("label", "Unknown")
        score = result.get("score", 0.0)

        # Emoji mapping for sentiment
        emoji_map = {"POSITIVE": "😊", "NEGATIVE": "😞", "NEUTRAL": "😐"}

        emoji = emoji_map.get(label.upper(), "🤔")

        self.out.insert("end", f"💭 SENTIMENT ANALYSIS RESULTS\n\n")
        self.out.insert("end", f"Sentiment: {label} {emoji}\n")
        self.out.insert("end", f"Confidence: {score:.1%}\n\n")

        # Add interpretation
        if score > 0.8:
            certainty = "Very confident"
        elif score > 0.6:
            certainty = "Confident"
        else:
            certainty = "Somewhat uncertain"

        self.out.insert(
            "end", f"📊 Interpretation: {certainty} in this classification\n"
        )

    def clear(self):
        """Clear all results"""
        self.out.configure(state="normal")
        self.out.delete("1.0", "end")

        # Re-add welcome message
        welcome_msg = """🤖 AI Model Analysis Results will appear here

• Select a model and provide input in the 'Run' tab
• Click 'Run Analysis' to process your input
• Results will automatically appear here with timestamps

Ready for analysis! 🚀
"""
        self.out.insert("1.0", welcome_msg)
        self.out.configure(state="disabled")

        self.result_count = 0
        self.result_count_label.configure(text="No results yet", foreground="gray")


class InfoFrame(ttk.Frame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)

        # Header
        header = ttk.Frame(self)
        header.pack(fill="x", padx=4, pady=(4, 0))
        ttk.Label(
            header, text="🤖 AI Model Information", font=("TkDefaultFont", 12, "bold")
        ).pack(side="left")

        # Info display with better formatting
        self.text = scrolledtext.ScrolledText(
            self,
            width=70,
            height=15,
            wrap=tk.WORD,
            font=("Consolas", 10),
            relief="sunken",
            borderwidth=2,
        )
        self.text.pack(expand=True, fill="both", padx=4, pady=4)

        # Add formatted model information
        infos = controller.model_infos()
        content = "📋 MODEL SPECIFICATIONS\n" + "=" * 50 + "\n\n"

        for k, v in infos.items():
            content += f"🔹 {k}:\n   {v}\n\n"

        content += "\n" + "=" * 50 + "\n"
        content += "💡 These models are loaded lazily for optimal performance!\n"
        content += "🚀 First inference may take longer due to model loading."

        self.text.insert("end", content)
        self.text.configure(state="disabled")


class OOPFrame(ttk.Frame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)

        # Header
        header = ttk.Frame(self)
        header.pack(fill="x", padx=4, pady=(4, 0))
        ttk.Label(
            header,
            text="🏗️ Object-Oriented Programming Concepts",
            font=("TkDefaultFont", 12, "bold"),
        ).pack(side="left")

        # OOP display with better formatting
        self.text = scrolledtext.ScrolledText(
            self,
            width=70,
            height=16,
            wrap=tk.WORD,
            font=("Consolas", 10),
            relief="sunken",
            borderwidth=2,
        )
        self.text.pack(expand=True, fill="both", padx=4, pady=4)

        # Add formatted OOP information
        content = "🎯 OOP CONCEPTS DEMONSTRATION\n" + "=" * 60 + "\n\n"
        content += controller.oop_explanations()
        content += "\n" + "=" * 60 + "\n"
        content += "✅ All major OOP concepts are implemented in this project!\n"
        content += "📚 Check the source code to see these concepts in action."

        self.text.insert("end", content)
        self.text.configure(state="disabled")
