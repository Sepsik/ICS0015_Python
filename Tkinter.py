from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

currentFilename = None


def about():
    fileWin = Toplevel(tk)
    Label(fileWin, height=4, text="Version: 1\n Author: Anita Sepp").pack()


def openFile():
    global currentFilename
    currentFilename = askopenfilename(parent=tk)
    fileText = readFile(currentFilename)
    setInput(fileText)


def save():
    if currentFilename is not None:
        writeFile(currentFilename, getInput())
    else:
        messagebox.showinfo("nPad", "Open file before saving it!")


def readFile(filename):
    return open(filename).read()


def writeFile(filename, toWrite):
    file = open(filename, 'w')
    file.write(toWrite)
    file.close()


def getInput():
    return textView.get(1.0, 'end-1c')


def setInput(value):
    textView.delete(1.0, 'end-1c')
    textView.insert('end-1c', value)


tk = Tk()
menuBar = Menu(tk)

# text view
textView = Text(tk)
textView.pack(fill="both")

# file menu
menuFile = Menu(menuBar, tearoff=0)
menuFile.add_command(label="Open", command=openFile)
menuFile.add_command(label="Save", command=save)
menuFile.add_separator()
menuFile.add_command(label="Close", command=tk.quit)
menuBar.add_cascade(label="File", menu=menuFile)

# help menu
menuHelp = Menu(menuBar, tearoff=0)
menuHelp.add_command(label="About...", command=about)
menuBar.add_cascade(label="Help", menu=menuHelp)

tk.config(menu=menuBar)

tk.mainloop()