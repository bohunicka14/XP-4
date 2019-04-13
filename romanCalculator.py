import unittest

def romanToNumber(roman_letters, roman_number):
    def convert(letter):
        index = roman_letters.find(letter)
        rad = index//2
        parity = index%2
        if parity == 0:
            return (10**rad, rad)
        else:
            return (5*10**rad, rad)

    BAD = -9999
    if roman_letters == '':
        return BAD
    for letter in roman_letters:
        if roman_letters.count(letter) > 1:
            return BAD

    for letter in roman_number:
        if roman_letters.count(letter) == 0:
            return BAD

    result = 0

    for i in range(len(roman_letters)):
        if i % 2 == 1:
            if roman_number.count(roman_letters[i]) > 1:
                return BAD

    i = 0
    while i < len(roman_number):
        if i < len(roman_number)-1:
            value1, rad1 = convert(roman_number[i])
            value2, rad2 = convert(roman_number[i+1])
            if value1 >= value2:
                result += value1
            else:
                if rad2 - rad1 > 1:
                    return BAD
                result += value2 - value1
                i += 1
        else:
            result += convert(roman_number[i])[0]
        i += 1

    return result


class Tester(unittest.TestCase):
    BAD = -9999

    def test_prazdny_vstup(self):
        self.assertEqual(romanToNumber('', ''), self.BAD)

    def test_opakovany_vstup(self):
        self.assertEqual(romanToNumber('ABBC',''), self.BAD)

    def test_vstup(self):
        self.assertEqual(romanToNumber("IV", "VIII"), 8)
        self.assertEqual(romanToNumber("A", "AAA"), 3)
        self.assertEqual(romanToNumber("I", "IV"), self.BAD)
        self.assertEqual(romanToNumber("IVXL", "LXXXIX"), 89)
        self.assertEqual(romanToNumber("IAVXLCQDM", "QVA"), 1015)
        self.assertEqual(romanToNumber("IVXLCDMPQRS", "SSS"), 300000)
        self.assertEqual(romanToNumber("", "IV"), self.BAD)
        self.assertEqual(romanToNumber("IVXLX", "IV"), self.BAD)

if __name__ == '__main__':
    unittest.main()