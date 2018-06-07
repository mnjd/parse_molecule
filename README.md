# Parse molecule
## Python code that parses chemical formulae of molecules and displays names of atoms and their numbers in a dictionary.

# Prerequisites
python3.6, unittest, re

# Getting started
Download parse.py, input.py and test.py

To work on interactive mode with a terminal, execute:
```
python input.py
```

# Running the tests
test.py includes tests on 3 molecules that are water (H2O), magnesium hydroxide (Mg(OH)2), fremy salt (K4[ON(SO3)2]2).

```
python test.py
```

# Some ideas behind this code
The first idea is to use the reversed chemical formula. If normal formula is used, multipliers only appear after parsing subunits they apply to. Values of these multipliers if obtained before parsing subunits is very useful. This is acheivedby reversing the chemical formula. On top of this advantage, if a lowercase appear, one can immediately guess that following letter will be uppercase. With an unreversed formula, if an uppercase is encountered, the following can be either a lowercase, a number, a parenthesis.

The second idea is to replicate subunits that are inside parentheses as many times as the value of multipliers in front of them. At the end, we are left with subunits that have any parenthesis and so, they can be parsed easily.

The third idea is to stock subunits that still contain parenthesis in a list and use the latter in recursive calls of the method that parse chemical formula. By doing this subunits get more and more pure (without parenthesis). The smallest possible subunits are added to a dictionary with their multipliers.

The fourth idea is to get rid of square and curly brackets and replace them by parenthesis. In chemical formulae, square and curly brackets only helps us to better visualize the subunits (than if only parenthesis are present).
