from parse import Parser
print('################################################')
print('From a chemical formula, this code outputs atoms')
print('that make up the chemical unit and their numbers')
print('################################################')
print('')
print('Type chemical formula to be parsed:')

formula = input()

p = Parser()
print(p.parse_molecule(formula))