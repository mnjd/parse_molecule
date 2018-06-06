# Parse molecule
## Python code that parses chemical formulae of molecules and displays names of atoms and their numbers in a dictionary.

# Getting started
Download parse.py and type:

```
python parse.py
```

# Prerequisites
python3.6, unittest, re

# Running the tests
Tests on 3 molecules run automatically when parse.py is executed.

The molecules are water (H2O), magnesium hydroxide (Mg(OH)2), fremy salt (K4[ON(SO3)2]2).

# Some ideas behind this code
The core idea is to use the reversed chemical formula. If normal formula is used, multipliers outside brackets (so they appear at right) are challenging; they have to be considered carefully. If the formula is reversed, the multipliers appear before the subunits they apply to.

The second idea is to replicate subunits as many times as the value of multipliers in front of them. At the end, we are left with subunits that have any parenthesis and so, they can be parsed easily.

The third idea is to get rid of square and curly brackets and replace them by parenthesis. In chemical formulae, square and curly brackets only helps us to better visualize the subunits (than if only parenthesis are present).

The fourth idea is to stock subunits that still contain parenthesis in a list and use the latter in recursive calls of the method that parse chemical formula. By doing this subunits get more and more pure (without parenthesis). The smallest possible subunits are added to a dictionary with their multipliers.


# Improvements
Some "else" cases need to be considered (as of now, there is a possibility that they break the code for complicated formulas).

So, the code has to be challenged against more complicated formulas than the 3 listed above.

Fractional multipliers break the code.
