from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser

def Save():
    global text_arrea, text_arrea1, stage
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        if stage == 0 and 'text_arrea' in globals():
            text = text_arrea.get("1.0", END)
        elif stage == 1 and 'text_arrea1' in globals():
            text = text_arrea1.get("1.0", END)
        else:
            print("Nema teksta za čuvanje.")
            return

        with open(file_path, 'w') as file:
            file.write(text)
        print(f'Podaci su sačuvani u {file_path}')

def Open_File():
    global text_arrea, text_arrea1, stage
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            file_content = file.read()

        if stage == 0:
            brisi_widgede1()
            text_arrea = Text(window, width=100, height=30)
            text_arrea.place(x=50, y=70)
            text_arrea.insert(END, file_content)
            Color_button = Button(window, text="Change Color", bg="gray23", fg="Snow2", font=(None, 12), command=change_color)
            Color_button.place(x=600, y=30)
            Underline_button = Button(window, text="Underline", bg="gray23", fg="Snow2", font=(None, 12), command=underline_text)
            Underline_button.place(x=720, y=30)
            stage = 0
            lista_widgeta.append(text_arrea)
            lista_widgeta.append(Color_button)
            lista_widgeta.append(Underline_button)
        elif stage == 1:
            if 'text_arrea1' in globals():
                text_arrea1.delete("1.0", END)
                text_arrea1.insert(END, file_content)
                # Add all buttons back if they don't exist
                if not any(isinstance(widget, Button) for widget in lista_widgeta):
                    New_button = Button(window, text="New file", bg="gray23", fg="Snow2", font=(None, 12), command=Novi_File1)
                    New_button.place(x=10, y=30)
                    Save_button = Button(window, text="Save file", bg="gray23", fg="Snow2", font=(None, 12), command=Save)
                    Save_button.place(x=100, y=30)
                    Open_button = Button(window, text="Open file", bg="gray23", fg="Snow2", font=(None, 12), command=Open_File)
                    Open_button.place(x=190, y=30)
                    Color_button = Button(window, text="Change Color", bg="gray23", fg="Snow2", font=(None, 12), command=change_color)
                    Color_button.place(x=280, y=30)
                    Underline_button = Button(window, text="Underline", bg="gray23", fg="Snow2", font=(None, 12), command=underline_text)
                    Underline_button.place(x=400, y=30)
                    lista_widgeta.append(New_button)
                    lista_widgeta.append(Save_button)
                    lista_widgeta.append(Open_button)
                    lista_widgeta.append(Color_button)
                    lista_widgeta.append(Underline_button)
        else:
            print("Nema widgeta za otvaranje.")
        print(f'Podaci su učitani iz {file_path}')

def Novi_File1():
    global text_arrea1, stage
    if 'text_arrea' in globals():
        text_arrea.destroy()
    text_arrea1 = Text(window, width=100, height=30)
    text_arrea1.place(x=50, y=70)
    stage = 1
    lista_widgeta.append(text_arrea1)

def Novi_File():
    global lista_widgeta, text_arrea, stage
    brisi_widgede1()
    text_arrea = Text(window, width=100, height=30)
    text_arrea.place(x=50, y=70)
    New_button = Button(window, text="New file", bg="gray23", fg="Snow2", font=(None, 12), command=Novi_File1)
    New_button.place(x=10, y=30)
    Save_button = Button(window, text="Save file", bg="gray23", fg="Snow2", font=(None, 12), command=Save)
    Save_button.place(x=100, y=30)
    Open_button = Button(window, text="Open file", bg="gray23", fg="Snow2", font=(None, 12), command=Open_File)
    Open_button.place(x=190, y=30)
    Color_button = Button(window, text="Change Color", bg="gray23", fg="Snow2", font=(None, 12), command=change_color)
    Color_button.place(x=280, y=30)
    Underline_button = Button(window, text="Underline", bg="gray23", fg="Snow2", font=(None, 12), command=underline_text)
    Underline_button.place(x=400, y=30)
    lista_widgeta.append(text_arrea)
    lista_widgeta.append(New_button)
    lista_widgeta.append(Save_button)
    lista_widgeta.append(Open_button)
    lista_widgeta.append(Color_button)
    lista_widgeta.append(Underline_button)
    stage = 0

def brisi_widgede1():
    global lista_widgeta
    for widget in lista_widgeta:
        widget.destroy()
    lista_widgeta.clear()

def change_color():
    global text_arrea, text_arrea1, stage
    color = colorchooser.askcolor()[1]  
    if stage == 0 and 'text_arrea' in globals():
        try:
            text_arrea.tag_add("color", "sel.first", "sel.last")
            text_arrea.tag_config("color", foreground=color)
        except:
            print("Nema selektovanog teksta za promenu boje.")
    elif stage == 1 and 'text_arrea1' in globals():
        try:
            text_arrea1.tag_add("color", "sel.first", "sel.last")
            text_arrea1.tag_config("color", foreground=color)
        except:
            print("Nema selektovanog teksta za promenu boje.")

def underline_text():
    global text_arrea, text_arrea1, stage
    if stage == 0 and 'text_arrea' in globals():
        try:
            text_arrea.tag_add("underline", "sel.first", "sel.last")
            text_arrea.tag_config("underline", underline=1)
        except:
            print("Nema selektovanog teksta za podvlačenje.")
    elif stage == 1 and 'text_arrea1' in globals():
        try:
            text_arrea1.tag_add("underline", "sel.first", "sel.last")
            text_arrea1.tag_config("underline", underline=1)
        except:
            print("Nema selektovanog teksta za podvlačenje.")

lista_widgeta = []
stage = 0

window = Tk()
window.config(bg='gray21')
window.geometry("900x750")
window.title("Notepad+++++")

notepad_text = Label(window, text="Text editor", bg="gray21", fg="Snow", font=(None, 40))
notepad_text.grid(row=0, column=0, pady=10)

notepad_new = Button(window, text="New file", bg="gray23", fg="Snow2", font=(None, 15), command=Novi_File)
notepad_new.grid(row=1, column=0, padx=10, pady=10, sticky=W)

notepad_open = Button(window, text="Open file", bg="gray23", fg="Snow2", font=(None, 15), command=Open_File)
notepad_open.grid(row=2, column=0, padx=10, pady=10, sticky=W)

lista_widgeta.append(notepad_new)
lista_widgeta.append(notepad_text)
lista_widgeta.append(notepad_open)

mainloop()
