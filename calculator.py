import unittest

'''
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
'''

def convert_arab_to_riman(input):
    roman = ''
    c = 0
    conv = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
            [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'],
            [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'],
            [1, 'I']]
    while input > 0:
        while conv[c][0] > input: c += 1
        roman += conv[c][1]
        input -= conv[c][0]

    return roman

def convert(input):
    table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    BAD = -9999

    if len(input) == 0:
        return BAD

    for i in input:
        if i not in 'IVXLCDM':
            return BAD

    count = 0
    res = 0
    i = 0
    counttab = {'I': [0, False],'V': [0, False], 'X': [0, False], 'L': [0, False], 'C': [0, False], 'D': [0, False], 'M': [0, False]}
    while i < len(input):
        s = input[i]
        if counttab['V'][0] > 1 or counttab['L'][0] > 1 or counttab['D'][0] > 1:
            return BAD

        if i < len(input)-1:
            if table[input[i]] >= table[input[i+1]]:
                 res += table[input[i]]
                 if input[i]  in counttab.keys():
                     counttab[input[i]][0] += 1
            else:
                dvojznak = input[i] + input[i+1]
                if dvojznak in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
                    res += table[input[i+1]] - table[input[i]]
                    if input[i] in counttab.keys():
                        counttab[input[i]][0] += 1
                        if input[i+1] in counttab.keys():
                            counttab[input[i+1]][0] += 1
                            counttab[input[i+1]][1] = True

                    i += 1

                else:
                    return BAD

        else:
            res += table[input[i]]

        for q in counttab.items():
            if q[1][0] > 3 and q[1][1] == False:
                return BAD
            if q[1][0] > 4 and q[1][1] == True:
                return BAD

        i += 1
        # res += table[input[i]]

    roman = convert_arab_to_riman(res)
    if input != roman:
        return BAD

    return res

def rimska_kalkulacka(input):
    BAD = -9999
    if len(input.strip()) == 0:
        return BAD

    input = input.strip()
    bol_operator = False
    riman1 = ''
    operator = ''
    riman2 = ''
    for i in input:
        if i == ' ':
            continue
        if i in '+*-/':
            operator = i
            bol_operator = True
        elif bol_operator == False:
            riman1 += i
        else:
            riman2 += i


    arab1 = convert(riman1)
    arab2 = convert(riman2)
    bigarab = 0
    if arab1 != BAD and arab2 != BAD:
        if operator == '+':
            bigarab = arab1 + arab2
        elif operator == '-':
            bigarab = arab1 - arab2
        elif operator == '*':
            bigarab = arab1 * arab2
        else:
            bigarab = arab1 / arab2
            if bigarab != int(bigarab):
                return BAD
            else:
                bigarab = int(bigarab)

    else:
        return BAD

    if 0 <= bigarab <= 3999 and isinstance(bigarab, int):
        return convert_arab_to_riman(bigarab)
    else:
        return BAD


class Tester(unittest.TestCase):
    table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    BAD = -9999
    # testy na convert funkciu
    def test_prazdny_vstup(self):
        self.assertEqual(convert(''), self.BAD)

    def test_zly_vstup(self):
        self.assertEqual(convert(' a  '), self.BAD)

    def test89(self):
        self.assertEqual(convert('LXXXIX'), 89)

    def testBIGriman(self):
        self.assertEqual(convert('MMMMM'), self.BAD)
        self.assertEqual(convert('CCCCCCC'), self.BAD)

    def testI(self):
        self.assertEqual(convert('I'), 1)

    def testII(self):
        self.assertEqual(convert('II'), 2)

    def test1znak(self): #lubovolny
        for i in 'IVXLCDM':
            # print(i, convert(i), self.table[i])
            self.assertEqual(convert(i), self.table[i])

    def test2znaky(self):
        for i in 'MDCLXVI':
            for j in 'MDCLXVI':
                if self.table[i] >= self.table[j]:
                    res = self.table[i] + self.table[j]
                    input = i+j

                    count = [0,0,0]
                    for t in input:
                        if t == 'V':
                            count[0] += 1
                        if t == 'L':
                            count[1] += 1
                        if t == 'D':
                            count[2] += 1
                    if count[0] > 1 or count[1] > 1 or count[2] > 1: res = -9999
                    # print(i+j, convert(i+j), res)
                    self.assertEqual(convert(i+j), res)

    def test3znaky(self):
        for i in 'MDCLXVI':
            for j in 'MDCLXVI':
                for k in 'MDCLXVI':

                    if self.table[i] >= self.table[j] >= self.table[k]:
                        res = self.table[i] + self.table[j] + self.table[k]
                        input = i+j+k
                        count = [0,0,0]
                        for t in input:
                            if t == 'V':
                                count[0] += 1
                            if t == 'L':
                                count[1] += 1
                            if t == 'D':
                                count[2] += 1
                        if count[0] > 1 or count[1] > 1 or count[2] > 1: res = -9999

                        # print(i+j+k, convert(i+j+k), res)
                        self.assertEqual(convert(i+j+k), res)


    def testminus2(self): #povolene odcitavania - IV,  IX,  XL, XC, CD, CM
        for i in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
            # print(i, convert(i), self.table[i[1]] - self.table[i[0]])
            self.assertEqual(convert(i), self.table[i[1]] - self.table[i[0]])

    def testminusALL2(self): #
        for i in 'IVXLCDM':
            for j in 'IVXLCDM':
                if self.table[j] > self.table[i]:
                    res = self.table[j] - self.table[i]
                    if i+j not in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
                        res = self.BAD
                    # print(i + j, convert(i + j), res)
                    self.assertEqual(convert(i + j), res)

    def testWRONGmadness(self):
        # self.assertEqual(convert('MCMCDXCXLXXXIV'), 2464)
        self.assertEqual(convert('MCMCDXCXLXXXIV'), self.BAD)
        self.assertEqual(convert('MMMMCMCDXCXLXXXIV'), self.BAD)
        self.assertEqual(convert('MMCMD'), self.BAD)

    def testGOODmadness(self):
        self.assertEqual(convert('MCMXCV'), 1995)
        self.assertEqual(convert('MMCDLXIV'), 2464)
        self.assertEqual(convert('MMMCM'), 3900)

    def testsomenum(self):
        self.assertEqual(convert('MMMCMXCIX'), 3999)
        self.assertEqual(convert('MMDLXIV'), 2564)
        self.assertEqual(convert('MMMDCCXII'), 3712)

    def test3roznezn(self):
        array = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        for i in range(len(array)):
            for j in range(len(array)):
                for k in range(len(array)):
                    if self.table[array[i]] >= self.table[array[j]] >= self.table[array[k]]:
                        if (i==j==1 or i==j==3 or i==j==5) or (j == k  and (j == 1 or j == 3 or j == 5)):
                            # print(array[i]+array[j]+array[k], convert(array[i] + array[j] + array[k]))
                            self.assertEqual(convert(array[i] + array[j] + array[k]), self.BAD)
                        else:
                            # print(array[i]+array[j]+array[k], convert(array[i]+array[j]+array[k]), self.table[array[i]] +
                            #       self.table[array[j]] + self.table[array[k]])
                            self.assertEqual(convert(array[i]+array[j]+array[k]), self.table[array[i]] +
                                             self.table[array[j]] + self.table[array[k]])

#     testy na kalkulacku
    def test_prazdny_vstup_kalkulacka(self):
        self.assertEqual(rimska_kalkulacka(''), self.BAD)

    def test_zly_vstup_kalkulacka(self):
        self.assertEqual(rimska_kalkulacka(' a  '), self.BAD)
        self.assertEqual(rimska_kalkulacka(' a + ab '), self.BAD)
        self.assertEqual(rimska_kalkulacka(' +  '), self.BAD)
        self.assertEqual(rimska_kalkulacka(' IV +  '), self.BAD)
        self.assertEqual(rimska_kalkulacka(' +  MM '), self.BAD)
        self.assertEqual(rimska_kalkulacka(" MD "), self.BAD)
        self.assertEqual(rimska_kalkulacka("MCDXLIV / MCDXLV"), self.BAD)
        self.assertEqual(rimska_kalkulacka(" MMMM + I"), self.BAD)
        self.assertEqual(rimska_kalkulacka("MMM + M"), self.BAD)
        self.assertEqual(rimska_kalkulacka("MMM @ M"), self.BAD)

    def test_plus(self):
        self.assertEqual(rimska_kalkulacka(' XI + I X '), 'XX')

    def test_deleno(self):
        self.assertEqual(rimska_kalkulacka(' XXV/V '), 'V')

    def test_minus(self):
        self.assertEqual(rimska_kalkulacka("MMCDXLIV-MCCXXII"), "MCCXXII")

    def test_nasobenie(self):
        self.assertEqual(rimska_kalkulacka("C * VIII"), "DCCC")

if __name__ == '__main__':
    unittest.main()
    # rimska_kalkulacka('    M M  + XI')
