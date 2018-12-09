from tkinter import filedialog, Tk

kd = { 'A': 1.8,'R':-4.5,'N':-3.5,'D':-3.5,'C': 2.5,
       'Q':-3.5,'E':-3.5,'G':-0.4,'H':-3.2,'I': 4.5,
       'L': 3.8,'K':-3.9,'M': 1.9,'F': 2.8,'P':-1.6,
       'S':-0.8,'T':-0.7,'W':-0.9,'Y':-1.3,'V': 4.2 }

root = Tk()
root.filename = filedialog.askopenfilename(initialdir="D:/강의 관련/'18년 2학기/생화학1/과제/2",
                                           title="Choose your file", filetypes=(("Text files", "*.txt"), ("FASTA files","*.fasta"), ("all files","*.*")))
print(root.filename)
root.withdraw()

file = open(root.filename, 'r')
seq = ""
f = file.read().splitlines()
for i in f:
    try:
        if i[0] == '>':
            print(i); continue
        else:
          seq += i
    except IndexError:
        pass
print(seq)