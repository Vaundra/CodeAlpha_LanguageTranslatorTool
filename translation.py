import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

class LanguageTranslationTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translation Tool")
        self.translator = Translator()
        
        # Set up the GUI elements
        self.setup_gui()
        
    def setup_gui(self):
        # Input Text
        self.input_text_label = tk.Label(self.root, text="Input Text:")
        self.input_text_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.input_text = tk.Text(self.root, height=10, width=50)
        self.input_text.grid(row=1, column=0, padx=10, pady=10)
        
        # Output Text
        self.output_text_label = tk.Label(self.root, text="Translated Text:")
        self.output_text_label.grid(row=0, column=2, padx=10, pady=10)
        
        self.output_text = tk.Text(self.root, height=10, width=50)
        self.output_text.grid(row=1, column=2, padx=10, pady=10)
        
        # Language Selection
        self.from_lang_label = tk.Label(self.root, text="From Language:")
        self.from_lang_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.to_lang_label = tk.Label(self.root, text="To Language:")
        self.to_lang_label.grid(row=2, column=2, padx=10, pady=10)
        
        self.from_lang = ttk.Combobox(self.root, values=list(LANGUAGES.values()))
        self.from_lang.grid(row=3, column=0, padx=10, pady=10)
        self.from_lang.set("English")
        
        self.to_lang = ttk.Combobox(self.root, values=list(LANGUAGES.values()))
        self.to_lang.grid(row=3, column=2, padx=10, pady=10)
        self.to_lang.set("French")
        
        # Translate Button
        self.translate_button = tk.Button(self.root, text="Translate", command=self.translate_text)
        self.translate_button.grid(row=4, column=1, padx=10, pady=10)
        
    def translate_text(self):
        input_text = self.input_text.get("1.0", tk.END).strip()
        from_lang_key = self.get_language_key(self.from_lang.get())
        to_lang_key = self.get_language_key(self.to_lang.get())
        
        if input_text:
            translated = self.translator.translate(input_text, src=from_lang_key, dest=to_lang_key)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translated.text)
            
    def get_language_key(self, language):
        for key, value in LANGUAGES.items():
            if value == language:
                return key
        return "en"  # Default to English if not found

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslationTool(root)
    root.mainloop()
