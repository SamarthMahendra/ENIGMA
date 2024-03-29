'''
--------mapping from wiki-----
Rotor detail     :  1941,feb7
Model and Number : "GERMAN RAILWAY(ROCKET)"
'''

ETW = {
    'A':'Q',
    'B':'W',
    'C':'E',
    'D':'R',
    'E':'T',
    'F':'Z',
    'G':'U',
    'H':'I',
    'I':'O',
    'J':'A',
    'K':'S',
    'L':'D',
    'M':'F',
    'N':'G',
    'O':'H',
    'P':'J',
    'Q':'K',
    'R':'P',
    'S':'Y',
    'T':'X',
    'U':'C',
    'V':'V',
    'W':'B',
    'X':'N',
    'Y':'M',
    'Z':'L'
}
NTOA={
    0:'A',
    1:'B',
    2:'C',
    3:'D',
    4:'E',
    5:'F',
    6:'G',
    7:'H',
    8:'I',
    9:'J',
    10:'K',
    11:'L',
    12:'M',
    13:'N',
    14:'O',
    15:'P',
    16:'Q',
    17:'R',
    18:'S',
    19:'T',
    20:'U',
    21:'V',
    22:'W',
    23:'X',
    24:'Y',
    25:'Z'
}
ATON={
    'A':0,
    'B':1,
    'C':2,
    'D':3,
    'E':4,
    'F':5,
    'G':6,
    'H':7,
    'I':8,
    'J':9,
    'K':10,
    'L':11,
    'M':12,
    'N':13,
    'O':14,
    'P':15,
    'Q':16,
    'R':17,
    'S':18,
    'T':19,
    'U':20,
    'V':21,
    'W':22,
    'X':23,
    'Y':24,
    'Z':25
}
L1=[
    'J',
    'G',
    'D',
    'Q',
    'O',
    'X',
    'U',
    'S',
    'C',
    'A',
    'M',
    'I',
    'F',
    'R',
    'V',
    'T',
    'P',
    'N',
    'E',
    'W',
    'K',
    'B',
    'L',
    'Z',
    'Y',
    'H'
]
L2=[
    'N',
    'T',
    'Z',
    'P',
    'S',
    'F',
    'B',
    'O',
    'K',
    'M',
    'W',
    'R',
    'C',
    'J',
    'D',
    'I',
    'V',
    'L',
    'A',
    'E',
    'Y',
    'U',
    'X',
    'H',
    'G',
    'Q'
]

L3=[
    'J',
    'V',
    'I',
    'U',
    'B',
    'H',
    'T',
    'C',
    'D',
    'Y',
    'A',
    'K',
    'E',
    'Q',
    'Z',
    'P',
    'O',
    'S',
    'G',
    'X',
    'N',
    'R',
    'M',
    'W',
    'F',
    'L'
]
R={
    'A':'Q',
    'B':'Y',
    'C':'H',
    'D':'O',
    'E':'G',
    'F':'N',
    'G':'E',
    'H':'C',
    'I':'V',
    'J':'P',
    'K':'U',
    'L':'Z',
    'M':'T',
    'N':'F',
    'O':'D',
    'P':'J',
    'Q':'A',
    'R':'X',
    'S':'W',
    'T':'M',
    'U':'K',
    'V':'I',
    'W':'S',
    'X':'R',
    'Y':'B',
    'Z':'L'
}
c={
    1:L1,
    2:L2,
    3:L3
}
def fn(w,v):
    for key,value in w.items():
        if v==value:
            return key
print(" Order of Wheel:")
c1=int(input())
c2=int(input())
c3=int(input())
W1=c[c1]
W2=c[c1]
W3=c[c1]

print("Enter Wheel 1 config :")
w1n=int(input())
for i in range(w1n):
    tt=W1.pop(0)
    W1.append(tt)
print("Enter Wheel 2 config :")
w1n=int(input())
for i in range(w1n):
    tt=W2.pop(0)
    W2.append(tt)
print("Enter Wheel 3 config :")
w1n = int(input())
for i in range(w1n):
    tt = W3.pop(0)
    W3.append(tt)

print("--Enter a Characters You want to Encrypt/Decrypt---")
res=""
x=str(input()).upper()
p1,p2,p3=0,0,0
for i in x:
    if i==' ':
        res+=' '
        continue

    if p1>=25:
        p1=0
        p2+=1
        t=W2.pop(0)
        W2.append(t)
    if p2>=25 :
        p2=0
        p3+=1
        t=W3.pop(0)
        W3.append(t)


    temp=R[W3[ATON[W2[ATON[W1[ATON[ETW[i]]]]]]]]
    temp2=fn(ETW,NTOA[W1.index(NTOA[W2.index(NTOA[W3.index(temp)])])])
    res+=temp2
    t=W1.pop(0)
    W1.append(t)
print(res)