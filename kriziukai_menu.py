from zaidimas import zaidimas
from zaidimas_prieskompa import zaidimas_pr_kp
import sys
import time

print("Kriziukai Nuliukai 3000")
pasirink = input("""Pasirinkite zaidimo tipa:
1. 1x1 su kitu zaideju
2. Pries kompiuteri
3. Arba Enter uzdaryti programa""")


if pasirink == "1":
    zaidimas()


if pasirink == "2":
    zaidimas_pr_kp()

if pasirink == "3" or pasirink == "":
    print("Menu isjungiamas po 7 sekundziu")
    time.sleep(3)
    print("Menu isjungiamas po 4 sekundziu")
    time.sleep(4)
    sys.exit("Uzdaroma")
