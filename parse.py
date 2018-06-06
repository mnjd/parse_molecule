import unittest

water = 'H2O'
magnesium_hydroxide = 'Mg(OH)2'
fremy_salt = 'K4[ON(SO3)2]2'


class Parser:
    
    def __init__(self):
        pass
    
    def replace_braces(self, mol):
        '''
        Replace square and brackets with parenthesis
        '''
        mol = mol.replace('[', '(')
        mol = mol.replace(']', ')')
        mol = mol.replace('{', '(')
        mol = mol.replace('}', ')')
        return mol

#p = Parser()
#print(p.replace_braces(fremy_salt))

'''
class MyTest(unittest.TestCase):
    def test_water(self):
        self.assertEqual(parse_molecule('water'), {'H': 2, 'O': 1})

    def test_magnesium_hydroxide(self):
        self.assertEqual(parse_molecule(magnesium_hydroxide), {'Mg': 1, 'O': 2, 'H': 2})

    def test_fremy_salt(self):
        self.assertEqual(parse_molecule(fremy_salt), {'K': 4, 'O': 14, 'N': 2, 'S': 4})

if __name__ == '__main__':
    unittest.main()
'''