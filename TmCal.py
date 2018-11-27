from tkinter import filedialog, Tk
import re
from math import log10


def translate(seq):
    seqSplit = []
    for i in range(int(len(seq) / 3)):
        seqSplit.append(seq[3 * i:3 * i + 3])

    proseq = ""
    for i in seqSplit:
        if codon[i] == "Stop":
            break
        else:
            proseq += aacode[codon[i]]
    return proseq


def printSeq(S):
    for i in range(int(len(S)/20)+1):
        try:
            print(S[i*20:(i+1)*20])
        except IndexError:
            print(S[i*20:])


def Tm(seq):
    Xcg = len(re.findall("[GC]", seq)) / len(seq)
    Tm = Xcg * 41.1 + 16.6 * log10(10**(-2)) + 81.5
    return Tm


def maxTm(seq):
    seqSplit = []
    for i in range(int(len(seq) / 3)):
        seqSplit.append(seq[3 * i:3 * i + 3])

    for s in range(len(seqSplit)):
        if seqSplit[s][2] == ("C" or "G"):
            continue
        else:
            if codon[seqSplit[s]] == (codon[seqSplit[s][0:2]+"C"]):
                seqSplit[s] = seqSplit[s][0:2]+"C"
            elif codon[seqSplit[s]] == (codon[seqSplit[s][0:2]+"G"]):
                seqSplit[s] = seqSplit[s][0:2]+"G"
    alterSeq = ""
    for i in seqSplit:
        alterSeq += i
    return Tm(alterSeq)


codon = {"TTT" : "Phe", "TTC" : "Phe", "TTA" : "Leu", "TTG" : "Leu",
         "CTT" : "Leu", "CTC" : "Leu", "CTA" : "Leu", "CTG" : "Leu",
         "ATT" : "Ile", "ATC" : "Ile", "ATA" : "Ile", "ATG" : "Met",
         "GTT" : "Val", "GTC" : "Val", "GTA" : "Val", "GTG" : "Val",
         "TCT" : "Ser", "TCC" : "Ser", "TCA" : "Ser", "TCG" : "Ser",
         "CCT" : "Pro", "CCC" : "Pro", "CCA" : "Pro", "CCG" : "Pro",
         "ACT" : "Thr", "ACC" : "Thr", "ACA" : "Thr", "ACG" : "Thr",
         "GCT" : "Ala", "GCC" : "Ala", "GCA" : "Ala", "GCG" : "Ala",
         "TAT" : "Tyr", "TAC" : "Tyr", "TAA" : "Stop", "TAG" : "Stop",
         "CAT" : "His", "CAC" : "His", "CAA" : "Gln", "CAG" : "Gln",
         "AAT" : "Asn", "AAC" : "Asn", "AAA" : "Lys", "AAG" : "Lys",
         "GAT" : "Asp", "GAC" : "Asp", "GAA" : "Glu", "GAG" : "Glu",
         "TGT" : "Cys", "TGC" : "Cys", "TGA" : "Stop", "TGG" : "Trp",
         "CGT" : "Arg", "CGC" : "Arg", "CGA" : "Arg", "CGG" : "Arg",
         "AGT" : "Ser", "AGC" : "Ser", "AGA" : "Arg", "AGG" : "Arg",
         "GGT" : "Gly", "GGC" : "Gly", "GGA" : "Gly", "GGG" : "Gly"}

aacode = {"Ala" : "A", "Arg" : "R", "Asn" : "N", "Asp" : "D", "Cys" : "C",
          "Gln" : "Q", "Glu" : "E", "Gly" : "G", "His" : "H", "Ile" : "I",
          "Leu" : "L", "Lys" : "K", "Met" : "M", "Phe" : "F", "Pro" : "P",
          "Ser" : "S", "Thr" : "T", "Trp" : "W", "Tyr" : "Y", "Val" : "V"}

root = Tk()
root.filename = filedialog.askopenfilename(initialdir="D:/강의 관련/'18년 2학기/생화학1/과제/1",
                                           title="Choose your file", filetypes=(("FASTA files","*.fasta"), ("all files","*.*")))
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

print("Sequence length : %dbp" % len(seq))
print("Translated Protein length : %daa" % len(translate(seq)))
print("Thermal denaturation (Tm) at 10^-2M [Na+] : %.2f'C" % Tm(seq))
print("Max thermal Tm at 10^-2M [Na+] : %.2f'C" % maxTm(seq))
a = input("Do you want to see all protein sequences? (y/n) [n]")
if a == ('y' or 'Y'):
    printSeq(translate(seq))
elif a == ('n' or 'N' or ''):
    pass

input()
