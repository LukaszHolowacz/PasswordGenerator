import random
import tkinter as tk
from tkinter import messagebox, END

male_litery = "abcdefghijklmnoqprstuwxyz"
wielkie_litery = "ABCDEFGHIJKLMNOQPRSTUWXYZ"
liczby = "1234567890"
znaki = "!@#$%^&*()_+-={}[]:;\|<>?,./"

def wypisz():
    wynik = ""
    if malestatus.get() == 1:
        wynik += male_litery
    if wielkiestatus.get() == 1:
        wynik += wielkie_litery
    if liczbystatus.get() == 1:
        wynik += liczby
    if znakistatus.get() == 1:
        wynik += znaki
    if malestatus.get() == 0 and wielkiestatus.get() == 0 and liczbystatus.get() == 0 and znakistatus.get() == 0:
        tk.messagebox.showinfo(title="Błąd", message="Musisz coś zaznaczyć")

    result_str = ''.join((random.choice(wynik) for i in range(int(znakitb.get()))))

    entry.config(state="normal")
    entry.delete(0, END)
    entry.insert(0, str(result_str))

window = tk.Tk()
window.geometry("300x200")

malestatus = tk.IntVar()
wielkiestatus = tk.IntVar()
liczbystatus = tk.IntVar()
znakistatus = tk.IntVar()

button = tk.Button(text="Generuj Hasło", command = wypisz)
label1 = tk.Label(text="Twoje hasło!")
entry = tk.Entry(state='disabled')
ile_znakow = tk.Label(text="Ile znaków ma mieć twoje hasło?")
znakitb = tk.Entry()

male = tk.Checkbutton(window, text='Małe Litery', variable=malestatus, onvalue=1, offvalue=0)
wielkie = tk.Checkbutton(window, text='Wielkie Litery', variable=wielkiestatus, onvalue=1, offvalue=0)
liczbycb = tk.Checkbutton(window, text='Liczby', variable=liczbystatus, onvalue=1, offvalue=0)
znakicb = tk.Checkbutton(window, text='Znaki specjalne', variable=znakistatus, onvalue=1, offvalue=0)

label1.pack()
entry.pack()
male.pack()
wielkie.pack()
liczbycb.pack()
znakicb.pack()
ile_znakow.pack()
znakitb.pack()
button.pack()

window.mainloop()
