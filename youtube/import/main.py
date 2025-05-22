# import
# module import

# 1
import math
print(math.sqrt(9))
# use ALL available methods : `package.method()`

# 2 `from` keyword
from math import sqrt
print(sqrt(81))
# import specific methods ; no need of package.method()

# 3 from
from math import floor,pi
print(floor(3.43))
print(pi)
# import multiple methods 

# 4 `as`
import math as mt
print(mt.sqrt(144))
# short/detail packages names with custom names

# 5 `dir()`
print(dir(math))
# returns all funcs n variables of package

# 6 custom packages
import custom_pkg
print(custom_pkg.sky)

from custom_pkg import sky,fn
print(sky)
fn()

# import all funcs
from custom_pkg import *
print(sky)



