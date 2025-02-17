import tkinter as tk
from tkinter import messagebox 


dictionaries = {
      "urhobo" : {
           "thank you": "migwo",
           "water": "vene",
           "house": "orho",
           "food": "epha",
           "name": "okpo",
           "husband": "oko",
           "heaven": "erivwi",
           "fire": "esiri",
           "day": "osu",
           "woman": "omote",
           "love": "ovwe",
           "road": "opha",
           "unity": "urhobo",
           "God": "oghene",
           "prayer": "ebe",
           "work": "evwe",
           "friend": "ore",
           "town": "uvwie",
           "town": "ovwian"
      },
      
    "Igbo": {
        "thank you": "daalụ",
        "please": "biko",
        "yes": "ee",
        "no": "mba",
        "water": "mmiri",
        "food": "nri",
        "house": "ụlọ",
        "book": "akwụkwọ",
        "man": "nwoke",
        "woman": "nwaanyị",
        "chair": "oche",
        "bag": "akpa",
        "walk": "ga ije",
        "sit": "nọdụ",
        "leg": "ukwu",
        "shoe": "akpụkpọ ụkwụ",
        "talk": "kwuo",
        "sleep": "ụra",
        "right": "aka nri",
        "left": "aka ekpe",
    },

    "IBIBIO": {
        "water": "Mmong",
        "car": "ogbonon",
        "door": "Etiti usun",
        "food": "udia",
        "book": "edisana",
        "church": "ufok abasi",
        "money": "ima",
        "shoe": "ibon",
        "phone": "ekpendion",
        "pen": "ubon edifon",
        "pencil": "ubon edifon okpok",
        "woman": "ekan",
        "road": "usun",
        "fire": "imim",
        "love": "ifok iban",
        "heaven": "odo abasi",
        "God": "abasi",
        "house": "ufok",
        "hand": "ukpon",
        "leg": "ukpok",
    },

    "Yourba": {
        "thank you": "ẹ ṣeun",
        "please": "ẹ jọ̀ọ́",
        "yes": "béẹ́ni",
        "no": "ràrà",
        "water": "omi",
        "food": "ounjẹ",
        "house": "ilé",
        "book": "ìwé",
        "man": "ọkùnrin",
        "woman": "obìnrin",
        "table": "tẹ́bílì",
        "floor": "ilé",
        "child": "ọmọ",
        "friend": "ọ̀rẹ́",
        "sun": "oorun",
        "moon": "osùpá",
        "sky": "ọ̀run",
        "fire": "iná",
        "road": "ọ̀nà",
        "money": "owo",
    },
}


def search_word():
    selected_dictionary = dictionary_var.get()
    word = entry.get().strip().lower()
    meaning = dictionaries.get(selected_dictionary, {}).get(word)

    if meaning:
        result_label.config(text=f"Meaning: {meaning}")
    else:
        result_label.config(text="")
        messagebox.showinfo(
            "Not Found",
            f"The word '{word}' is not in the {selected_dictionary} dictionary.",
        )


root = tk.Tk()
root.title("Naija Dictioniary")
welcome_label = tk.Label(root, text="Welcome to my cos 101 Dictionary", padx=200, pady=50, bg='black', fg="white", font='italic 16')
welcome_label.pack()
root.geometry("600x600")


title_label = tk.Label(root, text="Please select a Language")
title_label.pack(pady=10)

dictionary_var = tk.StringVar(value="select language")
dictionary_menu = tk.OptionMenu(root, dictionary_var, *dictionaries.keys())
dictionary_menu.pack()


word_label = tk.Label(root, text="Enter a word:")
word_label.pack()

entry = tk.Entry(root)
entry.pack()


search_button = tk.Button(root, text="Search", command=search_word, pady=10, padx=10)
search_button.pack(pady=10)


result_label = tk.Label(root, text="Meaning will appear here.")
result_label.pack(pady=20)


root.mainloop()
