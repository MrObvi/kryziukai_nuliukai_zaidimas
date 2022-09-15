import random
import sys
import time


def zaidimas_pr_kp():
    print("Zaidimas Kryziukai ir Nuliukai 3000 Pries PC, noredami isjungti program spauskite Enter")

    kriziukai = []

    while True:

        lygis=input("""Pasirinkite lygi:
        a - Lengvas
        b - Sunkus
        c - Uzdaryti zaidima\n""")

        if lygis == "c":
            print("zaidimas uzdaromas")
            break
        if lygis != 'a' and lygis != 'b' and lygis != 'b':
            print("Pasirinkimas netinkamas, bandykite dar karta")
            continue

        def spausdinam():
            return print(f"""
         {kriziukai[7]} | {kriziukai[8]} | {kriziukai[9]}
         {kriziukai[4]} | {kriziukai[5]} | {kriziukai[6]}
         {kriziukai[1]} | {kriziukai[2]} | {kriziukai[3]}
        """)

        def tikrinam_ar_laimejo():

            # eilutes X

            if kriziukai[7] == "X" and kriziukai[8] == "X" and kriziukai[9] == "X":
                print("X Laimejo")
                return True
            if kriziukai[4] == "X" and kriziukai[5] == "X" and kriziukai[6] == "X":
                print("X Laimejo")
                return True
            if kriziukai[1] == "X" and kriziukai[2] == "X" and kriziukai[3] == "X":
                print("X Laimejo")
                return True
            # stulpeliai X
            if kriziukai[7] == "X" and kriziukai[4] == "X" and kriziukai[1] == "X":
                print("X Laimejo")
                return True
            if kriziukai[8] == "X" and kriziukai[5] == "X" and kriziukai[2] == "X":
                print("X Laimejo")
                return True
            if kriziukai[9] == "X" and kriziukai[6] == "X" and kriziukai[3] == "X":
                print("X Laimejo")
                return True
            # istrizaines X
            if kriziukai[7] == "X" and kriziukai[5] == "X" and kriziukai[3] == "X":
                print("X Laimejo")
                return True
            if kriziukai[1] == "X" and kriziukai[5] == "X" and kriziukai[9] == "X":
                print("X Laimejo")
                return True

            # eilutes O
            if kriziukai[7] == "O" and kriziukai[8] == "O" and kriziukai[9] == "O":
                print("O Laimejo")
                return True
            if kriziukai[4] == "O" and kriziukai[5] == "O" and kriziukai[6] == "O":
                print("O Laimejo")
                return True
            if kriziukai[1] == "O" and kriziukai[2] == "O" and kriziukai[3] == "O":
                print("O Laimejo")
                return True
            # stulpeliai O
            if kriziukai[7] == "O" and kriziukai[4] == "O" and kriziukai[1] == "O":
                print("O Laimejo")
                return True
            if kriziukai[8] == "O" and kriziukai[5] == "O" and kriziukai[2] == "O":
                print("O Laimejo")
                return True
            if kriziukai[9] == "O" and kriziukai[6] == "O" and kriziukai[3] == "O":
                print("O Laimejo")
                return True
            # istrizaines O
            if kriziukai[7] == "O" and kriziukai[5] == "O" and kriziukai[3] == "O":
                print("O Laimejo")
                return True
            if kriziukai[1] == "O" and kriziukai[5] == "O" and kriziukai[9] == "O":
                print("O Laimejo")
                return True
            else:
                sk_x = 0
                sk_0 = 0
                for elemtas in kriziukai:
                    if elemtas == "X":
                        sk_x += 1
                    if elemtas == "O":
                        sk_0 += 1

                    if sk_0 + sk_x == 9:
                        print("Lygiosios")
                        toliau = input("Ar norite zaisti dar karta 1 - Taip 2- Ne\n")
                        if toliau == "1":
                            print("Zaidimas paleidziamas isnaujo, noredami pasirinkti kita lygi spauskite Enter")
                            kriziukai.clear()
                            return kriziukai
                        else:
                            print("Programa isjungiama po 4 sekundziu")
                            time.sleep(4)
                            sys.exit("Zaidimas baigtas")






                        # time.sleep(3)



        while True:

            if kriziukai==[]:
                kriziukai = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


            if tikrinam_ar_laimejo():
                spausdinam()
                kriziukai.clear()
                kriziukai = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

                toliau = input("Ar norite zaisti dar karta 1 - Taip 2- Ne\n")
                if toliau == "1":
                    print("Zaidimas paleidziamas isnaujo, noredami pasirinkti kita lygi spauskite Enter")
                    continue
                else:
                    print("Uzdaroma")
                    break

            spausdinam()
            pasirinkimas = input("Iraskykite skaiciu kur norite uzdeti X\n")

            if pasirinkimas == '7' and kriziukai[7] != "X" and kriziukai[7] != "O":
                kriziukai[7] = "X"

            elif pasirinkimas == '8' and kriziukai[8] != "X" and kriziukai[8] != "O":
                kriziukai[8] = "X"


            elif pasirinkimas == '9' and kriziukai[9] != "X" and kriziukai[9] != "O":
                kriziukai[9] = "X"


            elif pasirinkimas == '4' and kriziukai[4] != "X" and kriziukai[4] != "O":
                kriziukai[4] = "X"


            elif pasirinkimas == '5' and kriziukai[5] != "X" and kriziukai[5] != "O":
                kriziukai[5] = "X"


            elif pasirinkimas == '6' and kriziukai[6] != "X" and kriziukai[6] != "O":
                kriziukai[6] = "X"


            elif pasirinkimas == '1' and kriziukai[1] != "X" and kriziukai[1] != "O":
                kriziukai[1] = "X"


            elif pasirinkimas == '2' and kriziukai[2] != "X" and kriziukai[2] != "O":
                kriziukai[2] = "X"


            elif pasirinkimas == '3' and kriziukai[3] != "X" and kriziukai[3] != "O":
                kriziukai[3] = "X"


            elif pasirinkimas == "":
                print("Gristam i menu")
                break
            else:
                print("Netinkamas pasirinkimas, bandyk dar karta")

                continue

            if tikrinam_ar_laimejo():
                spausdinam()
                kriziukai.clear()
                kriziukai = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

                toliau = input("Ar norite zaisti dar karta 1 - Taip 2- Ne\n")
                if toliau == "1":
                    print("Zaidimas paleidziamas isnaujo, noredami pasirinkti kita lygi spauskite Enter")
                    continue
                else:
                    print("Uzdaroma")
                    break

            while True:
                if kriziukai == []:
                    break

                if tikrinam_ar_laimejo():
                    spausdinam()
                    kriziukai.clear()
                    kriziukai = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

                    toliau = input("Ar norite zaisti dar karta 1 - Taip 2- Ne\n")
                    if toliau == "1":
                        print("Zaidimas paleidziamas isnaujo, noredami pasirinkti kita lygi spauskite Enter")
                        continue
                    else:
                        print("Uzdaroma")
                        break

                spausdinam()
                if lygis == "a":
                    pasirinkimas_O = random.randint(1, 9)
                    # print(pasirinkimas_O)
                    print("Kompiuterio ejimas")
                    # standartiniai eijimai
                    if pasirinkimas_O == 7 and kriziukai[7] != "X" and kriziukai[7] != "O":
                        kriziukai[7] = "O"
                        break


                    elif pasirinkimas_O == 8 and kriziukai[8] != "X" and kriziukai[8] != "O":
                        kriziukai[8] = "O"
                        break


                    elif pasirinkimas_O == 9 and kriziukai[9] != "X" and kriziukai[9] != "O":
                        kriziukai[9] = "O"
                        break


                    elif pasirinkimas_O == 4 and kriziukai[4] != "X" and kriziukai[4] != "O":
                        kriziukai[4] = "O"
                        break


                    elif pasirinkimas_O == 5 and kriziukai[5] != "X" and kriziukai[5] != "O":
                        kriziukai[5] = "O"
                        break


                    elif pasirinkimas_O == 6 and kriziukai[6] != "X" and kriziukai[6] != "O":
                        kriziukai[6] = "O"
                        break


                    elif pasirinkimas_O == 1 and kriziukai[1] != "X" and kriziukai[1] != "O":
                        kriziukai[1] = "O"
                        break


                    elif pasirinkimas_O == 2 and kriziukai[2] != "X" and kriziukai[2] != "O":
                        kriziukai[2] = "O"
                        break


                    elif pasirinkimas_O == 3 and kriziukai[3] != "X" and kriziukai[3] != "O":
                        kriziukai[3] = "O"
                        break

                    else:
                        if tikrinam_ar_laimejo():
                            break
                        else:
                            print("Netinkamas pasirinkiams, bandyk dar karta")
                            continue

                if lygis == "b":

                    pasirinkimas_O = random.randint(1, 9)
                    # print(pasirinkimas_O)
                    print("Kompiuterio ejimas")
                    # eiluciu logika pagal 0

                    if kriziukai[7] == "O" and kriziukai[8] == "O" and kriziukai[9] != "X":
                        kriziukai[9] = "O"


                    elif kriziukai[8] == "O" and kriziukai[9] == "O" and kriziukai[7] != "X":
                        kriziukai[7] = "O"

                    elif kriziukai[7] == "O" and kriziukai[9] == "O" and kriziukai[8] != "X":
                        kriziukai[8] = "O"


                    elif kriziukai[4] == "O" and kriziukai[5] == "O" and kriziukai[6] != "X":
                        kriziukai[6] = "O"

                    elif kriziukai[5] == "O" and kriziukai[6] == "O" and kriziukai[4] != "X":
                        kriziukai[4] = "O"

                    elif kriziukai[4] == "O" and kriziukai[6] == "O" and kriziukai[5] != "X":
                        kriziukai[5] = "O"


                    elif kriziukai[1] == "O" and kriziukai[2] == "O" and kriziukai[3] != "X":
                        kriziukai[3] = "O"

                    elif kriziukai[2] == "O" and kriziukai[3] == "O" and kriziukai[1] != "X":
                        kriziukai[1] = "O"

                    elif kriziukai[1] == "O" and kriziukai[3] == "O" and kriziukai[2] != "X":
                        kriziukai[2] = "O"


                    # stulpeliu logika pagal 0
                    elif kriziukai[7] == "O" and kriziukai[4] == "O" and kriziukai[1] != "X":
                        kriziukai[1] = "O"

                    elif kriziukai[1] == "O" and kriziukai[4] == "O" and kriziukai[7] != "X":
                        kriziukai[7] = "O"

                    elif kriziukai[7] == "O" and kriziukai[1] == "O" and kriziukai[4] != "X":
                        kriziukai[4] = "O"


                    elif kriziukai[8] == "O" and kriziukai[5] == "O" and kriziukai[2] != "X":
                        kriziukai[2] = "O"

                    elif kriziukai[2] == "O" and kriziukai[5] == "O" and kriziukai[8] != "X":
                        kriziukai[8] = "O"

                    elif kriziukai[8] == "O" and kriziukai[2] == "O" and kriziukai[5] != "X":
                        kriziukai[5] = "O"


                    elif kriziukai[9] == "O" and kriziukai[6] == "O" and kriziukai[3] != "X":
                        kriziukai[3] = "O"

                    elif kriziukai[6] == "O" and kriziukai[3] == "O" and kriziukai[9] != "X":
                        kriziukai[9] = "O"

                    elif kriziukai[9] == "O" and kriziukai[3] == "O" and kriziukai[6] != "X":
                        kriziukai[6] = "O"

                    # istrizainiu logika pagal 0

                    elif kriziukai[7] == "O" and kriziukai[5] == "O" and kriziukai[3] != "X":
                        kriziukai[3] = "O"

                    elif kriziukai[3] == "O" and kriziukai[5] == "O" and kriziukai[7] != "X":
                        kriziukai[7] = "O"

                    elif kriziukai[7] == "O" and kriziukai[3] == "O" and kriziukai[5] != "X":
                        kriziukai[5] = "O"


                    elif kriziukai[1] == "O" and kriziukai[5] == "O" and kriziukai[9] != "X":
                        kriziukai[9] = "O"

                    elif kriziukai[9] == "O" and kriziukai[5] == "O" and kriziukai[1] != "X":
                        kriziukai[1] = "O"

                    elif kriziukai[1] == "O" and kriziukai[9] == "O" and kriziukai[5] != "X":
                        kriziukai[5] = "O"





                    # eiluciu logika pagal X

                    elif kriziukai[7] == "X" and kriziukai[8] == "X" and kriziukai[9] != "O":
                        kriziukai[9] = "O"

                    elif kriziukai[8] == "X" and kriziukai[9] == "X" and kriziukai[7] != "O":
                        kriziukai[7] = "O"

                    elif kriziukai[7] == "X" and kriziukai[9] == "X" and kriziukai[8] != "O":
                        kriziukai[8] = "O"


                    elif kriziukai[4] == "X" and kriziukai[5] == "X" and kriziukai[6] != "O":
                        kriziukai[6] = "O"

                    elif kriziukai[5] == "X" and kriziukai[6] == "X" and kriziukai[4] != "O":
                        kriziukai[4] = "O"

                    elif kriziukai[4] == "X" and kriziukai[6] == "X" and kriziukai[5] != "O":
                        kriziukai[5] = "O"


                    elif kriziukai[1] == "X" and kriziukai[2] == "X" and kriziukai[3] != "O":
                        kriziukai[3] = "O"

                    elif kriziukai[2] == "X" and kriziukai[3] == "X" and kriziukai[1] != "O":
                        kriziukai[1] = "O"

                    elif kriziukai[1] == "X" and kriziukai[3] == "X" and kriziukai[2] != "O":
                        kriziukai[2] = "O"


                    # stulpeliu logika pagal X
                    elif kriziukai[7] == "X" and kriziukai[4] == "X" and kriziukai[1] != "O":
                        kriziukai[1] = "O"

                    elif kriziukai[1] == "X" and kriziukai[4] == "X" and kriziukai[7] != "O":
                        kriziukai[7] = "O"

                    elif kriziukai[7] == "X" and kriziukai[1] == "X" and kriziukai[4] != "O":
                        kriziukai[4] = "O"


                    elif kriziukai[8] == "X" and kriziukai[5] == "X" and kriziukai[2] != "O":
                        kriziukai[2] = "O"

                    elif kriziukai[2] == "X" and kriziukai[5] == "X" and kriziukai[8] != "O":
                        kriziukai[8] = "O"

                    elif kriziukai[8] == "X" and kriziukai[2] == "X" and kriziukai[5] != "O":
                        kriziukai[5] = "O"


                    elif kriziukai[9] == "X" and kriziukai[6] == "X" and kriziukai[3] != "O":
                        kriziukai[3] = "O"

                    elif kriziukai[6] == "X" and kriziukai[3] == "X" and kriziukai[9] != "O":
                        kriziukai[9] = "O"

                    elif kriziukai[9] == "X" and kriziukai[3] == "X" and kriziukai[6] != "O":
                        kriziukai[6] = "O"

                    # istrizainiu logika pagal X

                    elif kriziukai[7] == "X" and kriziukai[5] == "X" and kriziukai[3] != "O":
                        kriziukai[3] = "O"

                    elif kriziukai[3] == "X" and kriziukai[5] == "X" and kriziukai[7] != "O":
                        kriziukai[7] = "O"

                    elif kriziukai[7] == "X" and kriziukai[3] == "X" and kriziukai[5] != "O":
                        kriziukai[5] = "O"


                    elif kriziukai[1] == "X" and kriziukai[5] == "X" and kriziukai[9] != "O":
                        kriziukai[9] = "O"

                    elif kriziukai[9] == "X" and kriziukai[5] == "X" and kriziukai[1] != "O":
                        kriziukai[1] = "O"

                    elif kriziukai[1] == "X" and kriziukai[9] == "X" and kriziukai[5] != "O":
                        kriziukai[5] = "O"

                    else:
                        # standartiniai eijimai
                        if pasirinkimas_O == 7 and kriziukai[7] != "X" and kriziukai[7] != "O":
                            kriziukai[7] = "O"
                            break


                        elif pasirinkimas_O == 8 and kriziukai[8] != "X" and kriziukai[8] != "O":
                            kriziukai[8] = "O"
                            break


                        elif pasirinkimas_O == 9 and kriziukai[9] != "X" and kriziukai[9] != "O":
                            kriziukai[9] = "O"
                            break


                        elif pasirinkimas_O == 4 and kriziukai[4] != "X" and kriziukai[4] != "O":
                            kriziukai[4] = "O"
                            break


                        elif pasirinkimas_O == 5 and kriziukai[5] != "X" and kriziukai[5] != "O":
                            kriziukai[5] = "O"
                            break


                        elif pasirinkimas_O == 6 and kriziukai[6] != "X" and kriziukai[6] != "O":
                            kriziukai[6] = "O"
                            break


                        elif pasirinkimas_O == 1 and kriziukai[1] != "X" and kriziukai[1] != "O":
                            kriziukai[1] = "O"
                            break


                        elif pasirinkimas_O == 2 and kriziukai[2] != "X" and kriziukai[2] != "O":
                            kriziukai[2] = "O"
                            break


                        elif pasirinkimas_O == 3 and kriziukai[3] != "X" and kriziukai[3] != "O":
                            kriziukai[3] = "O"
                            break

                        else:
                            if tikrinam_ar_laimejo():
                                break
                            else:
                                print("Netinkamas pasirinkiams, bandyk dar karta")
                                continue
                    break

# Jei norit paleisti pycharm programoje atkomentuokit funkcija apacioje
# zaidimas_pr_kp()