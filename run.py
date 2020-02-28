#! /usr/bin/python3
import webbrowser, sys

if len(sys.argv) < 3:
    print("Usage: run.py URLs.txt 0")
    quit()

web = open(sys.argv[1])
tab = int(sys.argv[2])
cont = 1

for op in web:
    cont += 1
    webbrowser.open_new_tab(op)
    if cont == tab:
        cont = 1  
