import math 
import tkinter as tk
from tkinter import ttk

class CalcFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack()

        self.side_a = tk.StringVar()
        self.side_b = tk.StringVar()
        self.side_c = tk.StringVar

        ttk.Label(self, text="Side A:").grid(
            column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.side_a).grid(
            column=1, row=0)
        
        ttk.Label(self, text="Side B:").grid(
            column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.side_b).grid(
            column=1, row=1)
        
        ttk.Label(self, text="Side C:").grid(
            column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.side_c, state="readonly").grid(
            column=1, row=2)
        
        ttk.Button(self, text="Calculate",
                   command=self.calculate).grid(
                       column=1, row=1, sticky=tk.E)
                   
        for child in self.winfo_children():
           child.grid_configure(padx=5, pady=3)  
    
    def calculate(self):
        side_a = float(self.side_a.get())
        side_b = int(self.side_b.get())

        side_c = round(math.sqrt(side_a**2 + side_b**2), 3)

        self.side_c.set(side_c)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Right Triangle Calculator")
    CalcFrame(root)
    root.mainloop()