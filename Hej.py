import tkinter as tk
from tkinter import messagebox

male_litery = "abcdefghijklmnoqprstuwxyz"
wielkie_litery = "ABCDEFGHIJKLMNOQPRSTUWXYZ"
liczby = "1234567890"
znaki = "!@#$%^&*()_+-={}[]:;\|<>?,./"

def wypisz():
    wynik = ""
    if malestatus.get()==1:
        wynik += male_litery
    elif wielkiestatus.get()==1:
        wynik += wielkie_litery
    elif liczbystatus.get()==1:
        wynik += liczby
    elif znakistatus.get()==1:
        wynik += znaki
    else:
        tk.messagebox.showinfo(title="Błąd", message="Musisz coś zaznaczyć")

window = tk.Tk()
window.geometry("300x200")


malestatus = tk.IntVar()
wielkiestatus = tk.IntVar()
liczbystatus = tk.IntVar()
znakistatus = tk.IntVar()

button = tk.Button(text="Generuj Hasło", command = wypisz)
label1 = tk.Label(text="Twoje hasło!")
entry = tk.Entry(state='disabled')
znakitb = tk.Entry()
znakitb.insert(0, 'Ile znaków?')

male = tk.Checkbutton(window, text='Małe Litery',variable=malestatus, onvalue=1, offvalue=0)
wielkie = tk.Checkbutton(window, text='Wielkie Litery',variable=wielkiestatus, onvalue=1, offvalue=0)
liczbycb = tk.Checkbutton(window, text='Liczby',variable=liczbystatus, onvalue=1, offvalue=0)
znakicb = tk.Checkbutton(window, text='Znaki specjalne',variable=znakistatus, onvalue=1, offvalue=0)

label1.pack()
entry.pack()
male.pack()
wielkie.pack()
liczbycb.pack()
znakicb.pack()
znakitb.pack()
button.pack()

window.mainloop()
