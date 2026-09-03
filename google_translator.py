from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator


languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru",
    "Portuguese": "pt",
}


def change(text, src, dest):
    translated = GoogleTranslator(
        source=languages[src],
        target=languages[dest]
    ).translate(text)

    return translated


def data():
    s = comb_sor.get()
    d = comb_dest.get()

    msg = sor_txt.get("1.0", END).strip()

    if not msg:
        dest_txt.delete("1.0", END)
        dest_txt.insert(END, "Please enter some text.")
        return

    try:
        textget = change(msg, s, d)

        dest_txt.delete("1.0", END)
        dest_txt.insert(END, textget)

    except Exception as e:
        dest_txt.delete("1.0", END)
        dest_txt.insert(END, "Translation Error:\n" + str(e))


root = Tk()
root.title("Translator")
root.geometry("500x600")
root.config(bg="silver")



title_label = Label(
    root,
    text="Translator",
    font=("Times New Roman", 40, "bold"),
    bg="silver"
)

title_label.place(
    x=100,
    y=30,
    height=70,
    width=320
)



source_label = Label(
    root,
    text="Source Text",
    font=("Times New Roman", 20, "bold"),
    fg="green",
    bg="silver"
)

source_label.place(
    x=100,
    y=105,
    height=30,
    width=300
)



sor_txt = Text(
    root,
    font=("Times New Roman", 12),
    wrap=WORD,
    bg="white",
    fg="black"
)

sor_txt.place(
    x=10,
    y=140,
    height=150,
    width=480
)



list_text = list(languages.keys())

comb_sor = ttk.Combobox(
    root,
    values=list_text,
    state="readonly"
)

comb_sor.place(
    x=10,
    y=310,
    height=30,
    width=110
)

comb_sor.set("English")



button_change = Button(
    root,
    text="Translate",
    relief=RAISED,
    command=data
)

button_change.place(
    x=190,
    y=310,
    height=30,
    width=120
)


comb_dest = ttk.Combobox(
    root,
    values=list_text,
    state="readonly"
)

comb_dest.place(
    x=380,
    y=310,
    height=30,
    width=110
)

comb_dest.set("Hindi")




destination_label = Label(
    root,
    text="Destination Text",
    font=("Times New Roman", 20, "bold"),
    fg="green",
    bg="silver"
)

destination_label.place(
    x=100,
    y=360,
    height=30,
    width=300
)

dest_txt = Text(
    root,
    font=("Times New Roman", 12),
    wrap=WORD,
    bg="white",
    fg="black"
)

dest_txt.place(
    x=10,
    y=400,
    height=150,
    width=480
)


root.mainloop()

