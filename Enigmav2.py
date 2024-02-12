'''
--------mapping from wiki-----
Rotor detail     :  1941,feb7
Model and Number : "GERMAN RAILWAY(ROCKET)"
'''
class enigma:
    def __init__(self):
        self.NTOA = {
            0: 'A',
            1: 'B',
            2: 'C',
            3: 'D',
            4: 'E',
            5: 'F',
            6: 'G',
            7: 'H',
            8: 'I',
            9: 'J',
            10: 'K',
            11: 'L',
            12: 'M',
            13: 'N',
            14: 'O',
            15: 'P',
            16: 'Q',
            17: 'R',
            18: 'S',
            19: 'T',
            20: 'U',
            21: 'V',
            22: 'W',
            23: 'X',
            24: 'Y',
            25: 'Z'
        }#coverts numbers to alpabets
        self.ATON = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3,
            'E': 4,
            'F': 5,
            'G': 6,
            'H': 7,
            'I': 8,
            'J': 9,
            'K': 10,
            'L': 11,
            'M': 12,
            'N': 13,
            'O': 14,
            'P': 15,
            'Q': 16,
            'R': 17,
            'S': 18,
            'T': 19,
            'U': 20,
            'V': 21,
            'W': 22,
            'X': 23,
            'Y': 24,
            'Z': 25
        }#converts alphabets to numbers
        self.L1 = [
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
        ] #rotor1 mapping
        self.L2 = [
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
        ]#rotor2 mapping
        self.L3 = [
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
        ]#rotor3 mapping
        self.ETW = {
            'A': 'Q',
            'B': 'W',
            'C': 'E',
            'D': 'R',
            'E': 'T',
            'F': 'Z',
            'G': 'U',
            'H': 'I',
            'I': 'O',
            'J': 'A',
            'K': 'S',
            'L': 'D',
            'M': 'F',
            'N': 'G',
            'O': 'H',
            'P': 'J',
            'Q': 'K',
            'R': 'P',
            'S': 'Y',
            'T': 'X',
            'U': 'C',
            'V': 'V',
            'W': 'B',
            'X': 'N',
            'Y': 'M',
            'Z': 'L'
        }# entery mapping
        self.R={
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
} #replector mapping
        '''Rotor mapping and functions are put into one entity so that we can
        suffle around the rotor and use respective functions on that'''
        self.Rotors = [[self.L1, self.fnL1], [self.L2, self.fnL2], [self.L3, self.fnL3]]
    def fnETW(self,v,d):
        ''' d==1 means its going in positive direction else its coming back'''
        if d==1:
            return self.ETW[v]
        else:
            for key, value in self.ETW.items():
                if v == value:
                    return key
    def fnL1(self,v,d):
        if d==1:
            '''First the letter is converted to number
            and then it returns the ith position character in L1 mapping
            '''
            vnumber=self.ATON[v]
            return self.L1[vnumber]
        else:
            '''First finds the index of the letter in L1 mapping
            then converts the number to alpha and returns
            '''
            vnumber=self.L1.index(v)
            return self.NTOA[vnumber]
    def fnL2(self,v,d):
        if d==1:
            '''First the letter is converted to number
            and then it returns the ith position character in L2 mapping
            '''
            vnumber=self.ATON[v]
            return self.L2[vnumber]
        else:
            '''First finds the index of the letter in L2 mapping
            then converts the number to alpha and returns
            '''
            vnumber = self.L2.index(v)
            return self.NTOA[vnumber]
    def fnL3(self,v,d):
        if d==1:
            '''First the letter is converted to number
            and then it returns the ith position character in L3 mapping
            '''
            vnumber=self.ATON[v]
            return self.L3[vnumber]
        else:
            '''First finds the index of the letter in L3 mapping
            then converts the number to alpha and returns
            '''
            vnumber = self.L3.index(v)
            return self.NTOA[vnumber]
    def fnR(self,v):
        return self.R[v]
    def FunctionEnigma(self):
        print(" Order of Wheel:")
        c1=int(input())
        c2=int(input())
        c3=int(input())
        W1=self.Rotors[c1-1]
        W2=self.Rotors[c2-1]
        W3=self.Rotors[c3-1]

        print("Enter Wheel 1 config :")
        ''' number between 1 and 25'''
        w1n=int(input())
        for i in range(w1n):
            tt=W1[0].pop(0)
            W1[0].append(tt)
        print("Enter Wheel 2 config :")
        ''' number between 1 and 25'''
        w2n=int(input())
        for i in range(w2n):
            tt=W2[0].pop(0)
            W2[0].append(tt)
        print("Enter Wheel 3 config :")
        ''' number between 1 and 25'''
        w3n = int(input())
        for i in range(w1n):
            tt = W3[0].pop(0)
            W3[0].append(tt)

        print("--Enter a Characters You want to Encrypt/Decrypt---")
        res=""
        x=str(input()).upper()# coverting it to upper characters
        p1,p2,p3=0,0,0
        for i in x:
            if i==' ':
                res+=' '
                continue
            if p1>=25:
                p1=0
                p2+=1
                t=W2[0].pop(0)
                W2[0].append(t)
            if p2>=25 :
                p2=0
                p3+=1
                t=W3[0].pop(0)
                W3[0].append(t)
            ''' process pipeline '''
            t1=self.fnETW(i,1)
            t2=W1[1](t1,1)
            t3=W2[1](t2,1)
            t4=W3[1](t3,1)
            t5=self.fnR(t4)
            t6=W3[1](t5,-1)
            t7=W2[1](t6,-1)
            t8=W1[1](t7,-1)
            res+=self.fnETW(t8,-1)
            ''' turn rotors 1 for every one charcter and once rotor one turns 25/ completes one round next p2 '''
            t=W1[0].pop(0)
            W1[0].append(t)
        print(res)
temp=enigma()
temp.FunctionEnigma()

# sample commit changes
