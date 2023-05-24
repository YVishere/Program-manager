from PIL import ImageTk, Image
from tkinter import *
import Login as Lg
import os as os
from importlib.machinery import SourceFileLoader

class window(Frame):
    def __init__(self, Frame):
        super().__init__(Frame)

        self.path = "C:/Users/ADMIN/OneDrive/Desktop/Adu/Gui"

        self.Ui()

    def Ui(self):
        self.configure(bg='Dark Blue')
        self.pack(fill=BOTH,expand=True)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.mainframe=Frame(self, bg='Light Blue')
        self.mainframe.pack(padx=20, pady=10, fill=BOTH, expand=True)

        self.canvas=Canvas(self.mainframe,
                           bg='Light Blue', bd=0, highlightthickness=0)
        self.scrollbar=Scrollbar(self.mainframe, orient=VERTICAL, command=self.canvas.yview)
        self.frame=Frame(self.canvas)

        self.scrollbar.pack(side=RIGHT, fill=Y, expand=False)
        self.canvas.pack(fill=BOTH, expand=True)

        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.list=[]

        for path in os.listdir(self.path):
            n=path.find(".py")
            if not n==-1:
                self.list.append(path)
        self.n=len(self.list)

        self.assignButtons(self.list, self.n, self.frame)
        self.frame.bind("<Configure>", self.myfunction)

    def myfunction(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    def openFile(self, i):
        f="C:/Users/ADMIN/OneDrive/Desktop/Adu/Gui/"+self.list[i]
        foo=SourceFileLoader(self.list[i][:-3],f).load_module()
        foo.main()
    def assignButtons(self, L, N, frame):
        for i in range(0,N):
            s=L[i][:-3]
            if s=="Program Manager" or s=="Login":
                continue
            Buttons=Button(frame, text=s, command=lambda i=i:self.openFile(i)
                           , cursor="hand2", activebackground="Light Blue",
                           bg="Light Blue", relief=FLAT)
            Buttons.pack(fill=X, expand=True)
def main():
    root=Tk()
    root.configure(bg="Black")
    root.title("Program manager")
    win=window(root)
    root.protocol("WM_DELETE_WINDOW", quit)
    win.mainloop()


if __name__=='__main__':
    Lg.main()
    main()