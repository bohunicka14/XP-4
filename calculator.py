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


def convert(input):
    table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    key = input[0]

    res = 0
    for i in input:
           res += table[i]

    return res



class Tester(unittest.TestCase):
    results = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def testI(self):
        self.assertEqual(convert('I'), 1)

    def testII(self):
        self.assertEqual(convert('II'), 2)

    def test3vrade(self):

        for i in 'IVXLCDM':
            for j in range(1,4):
                self.assertEqual(convert(i*j), j*self.results[i])

    def test2roznevr(self):
        for i in 'MDCLXVI':
            for j in 'MDCLXVI':
                if self.results[i] >= self.results[j]:
                    #print(i+j, convert(i+j), self.results[i] + self.results[j])
                    self.assertEqual(convert(i+j), self.results[i] + self.results[j])

    def testminus(self):
        for i in 'IVXLCDM':
            for j in 'IVXLCDM':
                if self.results[j] > self.results[i]:
                    # print(i + j, convert(i + j), self.results[j] - self.results[i])
                    self.assertEqual(convert(i + j), self.results[j] - self.results[i])
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()