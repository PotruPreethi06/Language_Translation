from tkinter import *
from tkinter import ttk
from googletrans import Translator
from gtts import gTTS
from playsound import playsound

# Create translator object
translator = Translator()

# Function to translate text
def translate_text():
    input_text = text_input.get("1.0", END)
    src_lang = source_lang.get()
    dest_lang = target_lang.get()

    try:
        translated = translator.translate(
            input_text,
            src=src_lang,
            dest=dest_lang
        )

        output_text.delete("1.0", END)
        output_text.insert(END, translated.text)

    except Exception as e:
        output_text.delete("1.0", END)
        output_text.insert(END, "Error: " + str(e))


# Main window
root = Tk()
root.title("Language Translator")
root.geometry("500x500")

Label(root, text="Enter Text").pack()
text_input = Text(root, height=5, width=50)
text_input.pack()

Label(root, text="Source Language").pack()
source_lang = ttk.Combobox(root, values=["en", "hi", "te", "fr"])
source_lang.set("en")
source_lang.pack()

Label(root, text="Target Language").pack()
target_lang = ttk.Combobox(root, values=["hi", "te", "en", "fr"])
target_lang.set("te")
target_lang.pack()

Button(root, text="Translate", command=translate_text).pack(pady=10)

Label(root, text="Translated Text").pack()
output_text = Text(root, height=5, width=50)
output_text.pack()



# Copy

def copy_text():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", END))

Button(root, text="Copy", command=copy_text).pack()



# Speak function
def speak_text():
    text = output_text.get("1.0", END)

    speech = gTTS(text=text, lang=target_lang.get())
    speech.save("voice.mp3")

    playsound("voice.mp3")

Button(root, text="Speak", command=speak_text).pack()


root.mainloop()

