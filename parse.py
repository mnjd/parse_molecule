import unittest
import re


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
        mol = self.reverse_string(mol)
        element_molecule = self.find_elements_molecule(mol)
        count = 0
        # lsubunits_tobe_parsed contains subunits of the molecule that have
        # to be parsed and is used at the begining of the recursion
        subunits_tobe_parsed = []
        while count < len(element_molecule):
            # check the type of element in element_molecule list:
            # number(s), letter(s)
            if element_molecule[count].isdecimal():
                # check the type of +1 element in element_molecule list:
                # parenthesis, letter(s)
                if element_molecule[count + 1] == '(':
                    idx = self.find_rbrac(''.join(element_molecule[count + 2:len(element_molecule)]))
                    multiplier = element_molecule[count]
                    multiplier = int(multiplier[::-1])
                    # empty subunits_tobe_parsed to clear already parsed subunits
                    subunits_tobe_parsed = []
                    # replicate subunits multiplier times and
                    # save them in subunits_tobe_parsed for recursion
                    for _ in range(multiplier):
                        subunits_tobe_parsed.append(
                            ''.join(element_molecule[count + 2:count + idx + 1]))
                    count += idx + 1
                    # recursively parse each element of subunits_tobe_parsed
                    for el in subunits_tobe_parsed:
                        el = self.interchange_braces(el)
                        # reverse chemical formula
                        el = self.reverse_string(el)
                        self.parse_molecule(el)
                elif element_molecule[count + 1].isalpha():
                    str = element_molecule[count + 1]
                    # update dictionary after reversing str and multiplier
                    multiplier = element_molecule[count]
                    multiplier = int(multiplier[::-1])
                    self.result[str[::-1]] = self.result.get(
                                             str[::-1], 0) + multiplier
                    count += 2
                else:
                    count += 1
            elif element_molecule[count].isalpha():
                str = element_molecule[count]
                # update dictionary after reversing str
                self.result[str[::-1]] = self.result.get(str[::-1], 0) + 1
                count += 1
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
    
    def reverse_string(self, str):
        '''
        Reverse a
        '''
        return str[::-1]

    def find_elements_molecule(self, formula):
        '''
        Given a chemical formula having atoms, multipliers and
        parentheses, make a list of these elements using regex 
        '''
        return re.findall(r"[a-z]*[A-Z]|['(']|[')']|\d+", formula)

    def find_rmbrac(self, str):
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


    def find_rbrac(self, str):
        '''
        Find rightmost parenthesis after finding leftmost parenthesis
        in a string including inside nested parentheses if any
        '''
        element_str = self.find_elements_molecule(str)
        count1 = 1
        count2 = 0
        count3 = 1
        while count2 < count1:
            if element_str[count3] == ')':
                count2 += 1
            elif element_str[count3] == '(':
                count2 += -1
            count3 += 1
        return count3


    def find_nth(self, str, pattern, n):
        '''
        Find the nth occurrence of a pattern in string
        '''
        start = str.find(pattern)
        while start >= 0 and n > 1:
            start = str.find(pattern, start+len(pattern))
            n -= 1
        return start

if __name__ == '__main__':
    liste_formula = ['H2O', 'Mg(OH)2', 'K4[ON(SO3)2]2']
    liste_name = ['water', 'magnesium_hydroxide', 'fremy_salt']
    for index, formula in enumerate(liste_formula):
        p = Parser()
        print(liste_name[index], ': ', p.parse_molecule(formula))

