from tkinter import filedialog, Tk
from pylab import *
import matplotlib

window_size = 7

try:
    def hydropathy_index(window_size, sequence):
        hydropathy = []
        for i in range(len(sequence)-window_size+1):
            sum = 0
            for s in sequence[i:i+window_size]:
                sum += kd[s]
            hydropathy.append(sum/window_size)
        return hydropathy

    def positive_number(hydropathy_list):
        ans = 0
        index = 0
        indexList = []
        ansList = []
        for i in hydropathy_list:
            if i >= 0:
                indexList.append(index)
            else:
                if len(indexList) >= 20:
                    indexList.append(index)
                    ans += 1
                    ansList.append(indexList[::])
                    indexList = []
                else:
                    indexList = []
            index += 1
        return ans, ansList


    kd = {'A': 1.8,'R':-4.5,'N':-3.5,'D':-3.5,'C': 2.5,
           'Q':-3.5,'E':-3.5,'G':-0.4,'H':-3.2,'I': 4.5,
           'L': 3.8,'K':-3.9,'M': 1.9,'F': 2.8,'P':-1.6,
           'S':-0.8,'T':-0.7,'W':-0.9,'Y':-1.3,'V': 4.2}

    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir="D:/강의 관련/'18년 2학기/생화학1/과제/2",
                                               title="Choose your file", filetypes=(("Text files", "*.txt"), ("FASTA files","*.fasta"), ("all files","*.*")))
    print(root.filename)
    root.withdraw()

    file = open(root.filename, 'r')
    seq = ""
    header = ''
    f = file.read().splitlines()
    for i in f:
        try:
            if i[0] == '>':
                header = i
                print(i); continue
            else:
              seq += i
        except IndexError:
            pass

    name = header.split('|')[1]

    print("Sequence length : %dbp" % len(seq))
    h = hydropathy_index(window_size, seq)
    print("Hydropathy index length : %d" % len(h))
    n, position = positive_number(h)
    print("Number of estimated membrane spanning region : %d" % n)
    for f in range(1, len(position)+1):
        print("Position %d : %d - %d" % (f, position[f-1][0]+int(window_size/2), position[f-1][-1]+int(window_size/2)))


    x_data = range(0,len(h))
    y_data = h

    plot(x_data, y_data)

    axhline(0, color="g")

    xlabel("Residue number")
    ylabel("Hydropathy index (%daa window)" % window_size)
    title("Hydropathy index for %s" % name)

    show()

    matplotlib.get_backend()
    close()
    input()
except Exception as e:
    print(e)
input()