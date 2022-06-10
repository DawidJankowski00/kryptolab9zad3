import sys


def wczytaj_wiadomosc():
    f = open("mess.txt", 'r')
    mess = f.readline()
    out = ""
    f.close()
    for i in range(0, len(mess)):
        temp = bin(int(mess[i], 16))[2:]
        temp2 = ''
        for i in range(0, 4 - len(temp)):
            temp2 += '0'
        temp2 += temp
        out += temp2
    return out


def wstaw_do_pliku(A):
    f = open("watermark.html", 'w')
    for i in range(0, len(A)):
        f.write(A[i])
        f.write('\n')
    f.close


def wstaw_wiadomosc(mess):
    f = open("detect.txt", 'w')
    f.write(mess)
    f.close()


def e1():
    mess = wczytaj_wiadomosc()
    A = []
    f = open("cover.html")
    for line in f:
        temp = line
        if temp[-1] == "\n":
            temp = temp[:-1]
        while temp[-1] == ' ' and len(temp) != 0:
            temp = temp[:-1]
        A.append(temp)
    f.close
    if len(mess) > len(A):
        print("Wiadomosc jest za dluga")
    else:
        for i in range(0, len(mess)):
            if mess[i] == '1':
                A[i] += ' '
        A[len(mess)] += '  '
        wstaw_do_pliku(A)


def e2():
    mess = wczytaj_wiadomosc()
    A = []
    l = 0
    f = open("cover.html")
    for line in f:
        temp = line
        if temp[-1] == "\n":
            temp = temp[:-1]
        temp2 = ''
        temp2 += temp[0]
        for i in range(1, len(temp)):

            if temp[i - 1] == ' ' and temp[i] == ' ':
                pass
            else:
                if temp[i] == ' ':
                    l += 1
                temp2 += temp[i]
        A.append(temp2)

    if len(mess) > l:
        print("Wiadomosc jest za dluga")
    else:
        m = 0
        for i in range(0, len(A)):
            temp = ''
            for j in range(0, len(A[i])):
                if A[i][j] == ' ':
                    if m > len(mess):
                        temp += ' '
                    elif m == len(mess):
                        temp += '   '
                    else:
                        if mess[m] == '0':
                            temp += ' '
                        else:
                            temp += '  '
                    m += 1
                else:
                    temp += A[i][j]
            A[i] = temp
        wstaw_do_pliku(A)


def e3():
    A = []
    l = 0
    f = open("cover.html")
    status = False
    for line in f:
        temp = line
        if temp[-1] == "\n":
            temp = temp[:-1]
        if "<body" in temp:
            status = True

        if status:
            temp2 = ''
            otwarcie_znacznika = False
            start_znacznika = 0
            for i in range(0, len(temp)):

                if temp[i] == "<":
                    if temp[i + 1] != "/":
                        otwarcie_znacznika = True
                        start_znacznika = i
                if otwarcie_znacznika:
                    if temp[i] == '>':
                        if "margin-bottom:" in temp[start_znacznika:i] or "line-height:" in temp[start_znacznika:i]:
                            pass
                        else:
                            l += 1
                            if 'style="margin-bottom: 0cm; line-height: 100%"' in temp[
                                                                                  start_znacznika:i] or 'style="margin' \
                                                                                                        '-botom: 0cm; ' \
                                                                                                        'lineheight: ' \
                                                                                                        '100%"' in temp[
                                                                                                                   start_znacznika:i]:
                                temp2[start_znacznika:i - 1].replace('style="margin-botom: 0cm; lineheight: 100%"',
                                                                     'style="margin-bottom: 0cm; line-height: 100%"')
                                temp2[start_znacznika:i - 1].replace('style="margin-bottom: 0cm; line-height: 100%"',
                                                                     'style="margin-bottom: 0cm; line-height: 100%"')
                            else:
                                temp2 += ' style="margin-bottom: 0cm; line-height: 100%"'
                        otwarcie_znacznika = False
                temp2 += temp[i]
            temp = temp2
        A.append(temp)

    mess = wczytaj_wiadomosc()
    if len(mess) > l:
        print("Wiadomosc jest za dluga")
    else:
        m = 0
        status = False
        for j in range(0, len(A)):
            temp = A[j]
            if "<body" in temp:
                status = True
            if status:
                otwarcie_znacznika = False
                start_znacznika = 0
                if m < len(mess):
                    temp2 = ''
                    for i in range(0, len(temp)):
                        if temp[i] == "<":
                            if temp[i + 1] != "/":
                                otwarcie_znacznika = True
                                start_znacznika = i
                        if otwarcie_znacznika:
                            if temp[i] == '>':

                                if mess[m] == '0':

                                    temp2 = temp2[:start_znacznika] + temp2[start_znacznika:i].replace(
                                        'style="margin-bottom: 0cm; line-height: 100%"',
                                        'style="margin-botom: 0cm; line-height: 100%"')
                                else:

                                    temp2 = temp2[:start_znacznika] + temp2[start_znacznika:i].replace(
                                        'style="margin-bottom: 0cm; line-height: 100%"',
                                        'style="margin-bottom: 0cm; lineheight: 100%"')


                                m += 1
                                otwarcie_znacznika = False

                        temp2 += temp[i]
                    temp = temp2
                    A[j] = temp
                else:
                    break
    wstaw_do_pliku(A)


def e4():
    A = []
    l = 0
    f = open("cover.html")
    for line in f:
        temp = line
        if temp[-1] == "\n":
            temp = temp[:-1]
        for i in range(0,len(temp)):
            if temp[i] == '<':
                if temp[i+1:i+4] == 'div':
                    l += 1
        A.append(temp)
    m = 0
    mess = wczytaj_wiadomosc()
    if len(mess) > l:
        print("Wiadomosc jest za dluga")
    else:
        start = 0
        status = False
        for line in range(0,len(A)):
            temp = A[line]
            temp2 = ''
            for i in range(0, len(temp)):
                if temp[i] == '<':
                    if temp[i + 1:i + 4] == 'div':
                        start = i
                        status = True
                if status:
                    if temp[i] == '>':
                        if m < len(mess)+1:
                            if m < len(mess):
                                if mess[m] == '1':
                                    temp2 += "></div>" + temp[start:i]
                                else:
                                    temp2 += "></div>" + temp[start:i]
                                    temp2 += "></div>" + temp[start:i]
                            else:
                                temp2 += "></div>" + temp[start:i]
                                temp2 += "></div>" + temp[start:i]
                                temp2 += "></div>" + temp[start:i]
                        status = False
                        m += 1

                temp2 += temp[i]
            A[line] = temp2
        wstaw_do_pliku(A)


def d1():
    f = open("watermark.html", 'r')
    mess = ''
    for line in f:
        if line[-1] == '\n':
            if line[-2] and line[-3] == ' ':
                break
            if line[-2] == ' ':
                mess += '1'
            else:
                mess += '0'
        else:
            if line[-1] and line[-2] == ' ':
                break
            if line[-1] == ' ':
                mess += '1'
            else:
                mess += '0'
    f.close()
    mess = hex(int(mess, 2))[2:]
    wstaw_wiadomosc(mess)


def d2():
    f = open("watermark.html", 'r')
    mess = ''
    end = False
    for line in f:
        temp = line
        i = 0
        while i < len(temp):

            if temp[i] == ' ':
                if temp[i + 1] == ' ':
                    if temp[i + 2] == ' ':
                        end = True
                        break
                    mess += '1'
                    i = i + 1
                else:
                    mess += '0'
            i += 1
        if end:
            break
    f.close()
    mess = hex(int(mess, 2))[2:]
    wstaw_wiadomosc(mess)


def d3():
    f = open("watermark.html", 'r')
    mess = ''
    status = False
    for line in f:
        temp = line
        if "<body" in temp:
            status = True
        if status:
            otwarcie_znacznika = False
            start_znacznika = 0
            for i in range(0, len(temp)):
                if temp[i] == "<":
                    if temp[i + 1] != "/":
                        otwarcie_znacznika = True
                        start_znacznika = i
                if otwarcie_znacznika:
                    if temp[i] == '>':
                        if 'style="margin-botom: 0cm; line-height: 100%"' in temp[start_znacznika:i]:
                            mess += '0'
                        elif 'style="margin-bottom: 0cm; lineheight: 100%"' in temp[start_znacznika:i]:
                            mess += '1'
                        otwarcie_znacznika = False

    f.close()
    mess = hex(int(mess, 2))[2:]
    wstaw_wiadomosc(mess)


def d4():
    f = open("watermark.html", 'r')
    mess = ''
    status = False
    for line in f:
        temp = line
        for i in range(0, len(temp)):
            if temp[i] == '<':
                if temp[i + 1:i + 4] == 'div':
                    start = i
                    status = True
            if status:
                if temp[i] == '>':
                    if temp[start:i+1] == temp[start+6+len(temp[start:i+1]):i+6+len(temp[start:i+1])+2]:
                        print("hej")
                    elif temp[start:i+1] == temp[start+6+(i-start)+1:i+6+(i-start)+2]:
                        mess += '1'

                    status = False



def encrypt():
    if sys.argv[2] == "-1":
        e1()
    elif sys.argv[2] == "-2":
        e2()
    elif sys.argv[2] == "-3":
        e3()
    elif sys.argv[2] == "-4":
        e4()
    else:
        print("Niepoprawny arg nr 2")


def decrypt():
    if sys.argv[2] == "-1":
        d1()
    elif sys.argv[2] == "-2":
        d2()
    elif sys.argv[2] == "-3":
        d3()
    elif sys.argv[2] == "-4":
        d4()
    else:
        print("Niepoprawny arg nr 2")


if __name__ == '__main__':
    if sys.argv[1] == "-e":
        encrypt()
    elif sys.argv[1] == "-d":
        decrypt()
    else:
        print("Niepoprawny arg nr 1")
