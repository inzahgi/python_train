#coding:utf-8
import tkinter as tk
root = tk.Tk()
lb = tk.Listbox(root)
for item in ['python','tkinter','widget']:
    lb.insert(1,item)
lb.pack()
root.mainloop()
