import unittest
import re

water = 'H2O'
magnesium_hydroxide = 'Mg(OH)2'
fremy_salt = 'K4[ON(SO3)2]2'
imaginary = 'ON(SO3)2'


class Parser:

    def __init__(self):
        # result is the dictionary that contains atoms and their counts
        self.result = {}

    def parse_molecule(self, mol):
        '''
        Chemical formula of molecules is parsed here
        '''
        mol = self.replace_braces(mol)
        mol = self.interchange_braces(mol)
        # reverse chemical formula
        mol = mol[::-1]
        # make a list with individual elements found in chemical formula:
        # atoms, multipliers, parenthesis
        element_molecule = re.findall(r"[a-z]*[A-Z]|['(']|[')']|\d+", mol)
        count = 0
        # l contains subunits of the molecule that have to be parsed and
        # is used at the begining of the recursion
        l = []
        while count < len(element_molecule):
            # check the type of element in element_molecule list:
            # number(s), letter(s)
            if element_molecule[count].isdecimal():
                # check the type of +1 element in element_molecule list:
                # parenthesis, letter(s)
                if element_molecule[count + 1] == '(':
                    idx = self.find_rbrac(mol[count + 1:len(mol)])
                    # replicate subunits multiplier times and
                    # save them in l for recursion
                    for i in range(int(element_molecule[count])):
                        l.append(mol[count + 2:count + idx + 1])
                    count += idx + 1
                    # recursively parse each element of l
                    for el in l:
                        el = self.interchange_braces(el)
                        # reverse chemical formula
                        el = el[::-1]
                        self.parse_molecule(el)
                elif element_molecule[count + 1].isalpha():
                    str = element_molecule[count + 1]
                    # update dictionary after reversing str
                    self.result[str[::-1]] = self.result.get(str[::-1], 0) + int(element_molecule[count])
                    count += 2
                ######################
                #  TO DO //// TO DO  #
                # work on else cases #
                #  TO DO //// TO DO  #
                ######################
                else:
                    count += 1
            elif element_molecule[count].isalpha():
                str = element_molecule[count]
                # update dictionary after reversing str
                self.result[str[::-1]] = self.result.get(str[::-1], 0) + 1
                count += 1
            ######################
            #  TO DO //// TO DO  #
            # work on else cases #
            #  TO DO //// TO DO  #
            ######################
            else:
                count += 1
        return self.result

    def replace_braces(self, str):
        '''
        Replace square and brackets with parenthesis
        '''
        str = str.replace('[', '(')
        str = str.replace(']', ')')
        str = str.replace('{', '(')
        str = str.replace('}', ')')
        return str

    def interchange_braces(self, str):
        '''
        Interchange left and right parenthesis
        '''
        str = str.replace('(', ']')
        str = str.replace(')', '(')
        str = str.replace(']', ')')
        return str

    def find_rbrac(self, str):
        '''
        Find rightmost parenthesis after finding leftmost parenthesis
        '''
        count = 0
        for idx, ch in enumerate(str):
            if ch == '(':
                count += 1
        for idx, ch in enumerate(str):
            position = self.find_nth(str, ')', count)
            return position

    def find_nth(self, str, pattern, n):
        '''
        Find the nth occurrence of a pattern in string
        '''
        start = str.find(pattern)
        while start >= 0 and n > 1:
            start = str.find(pattern, start+len(pattern))
            n -= 1
        return start

p = Parser()
print(p.parse_molecule('K44(ONa)4SO3'))


class MyTest(unittest.TestCase):
    def test_water(self):
        p = Parser()
        self.assertEqual(p.parse_molecule(water), {'H': 2, 'O': 1})

    def test_magnesium_hydroxide(self):
        p = Parser()
        self.assertEqual(p.parse_molecule(magnesium_hydroxide), {'Mg': 1, 'O': 2, 'H': 2})

    def test_fremy_salt(self):
        p = Parser()
        self.assertEqual(p.parse_molecule(fremy_salt), {'K': 4, 'O': 14, 'N': 2, 'S': 4})


if __name__ == '__main__':
    unittest.main()
