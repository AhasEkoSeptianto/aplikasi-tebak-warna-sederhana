from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title('Program Bahasa Gaul')
root.geometry('550x250')

# check button
def ubah():
    # ambil data
    kata = ambildata.get().upper()
    bahasa = combobox.get()

    # filter
    gaul = ['A','I','U','E','O']
    
    # simpan kelist
    hasilkata = []

    for i in kata:
        if i in gaul:
            hasilkata.append(bahasa)
            continue
        hasilkata.append(i)
    
    # join
    listToStr = ' '.join(map(str, hasilkata))

    labelhasilakhir.configure(text=listToStr)


# variable
labelinput  = Label(root,text='Masukan Kata Yang Ingin Diubah Kebahasa Gaul : ',padx=10)
ambildata   = Entry(root)
btn         = Button(root,text='Submit',command=ubah, bg='blue', fg='white')
labelpilih  = Label(root,text='Pilih Bahasa')
n           = tk.StringVar()
combobox    = ttk.Combobox(root,width=5,textvariable=n)
combobox['values'] = (
    'A',
    'I',
    'U',
    'E',
    'O',
)


labelhasil  = Label(root,text='-- Hasil --')
labelhasilakhir = Label(root,text='None')


# place
labelinput.grid(column=0,row=0)
ambildata.grid(column=1,row=0)
labelpilih.place(relx=0.5,rely=0.2,anchor=CENTER)
combobox.place(relx=0.5,rely=0.3, anchor=CENTER)
btn.place(relx=0.5 , rely=0.5,anchor=CENTER)
labelhasil.place(relx=0.5,rely=0.7, anchor=CENTER)
labelhasilakhir.place(relx=0.5, rely=0.9, anchor=CENTER)

root.resizable(0,0)
root.mainloop()