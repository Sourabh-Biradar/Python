# string methods

NOTE : strings are immutable ; methods return new string ; WON'T change existing strings

`len()` : returns length of string/array

`upper()` & `lower()` : to upper case & to lower case

`rstrip()` : removes specified TRAILING chars (WON'T work on begining chars)

`replace()` : replaces all occurances with GIVEN string

`split()` : creates LIST from specified char

`capitalize()` : first letter to Cap

`center()` : makes string length to specified length by leaving spaces at begining

`count()` : returns count of specified char/chars

`endswith()` : True if string ENDS with specified char/chars

`startswith()` : True if string STARTS with specified char/chars

`find()` : returns index of char, -1 if not found

`index()` : returns index of char, value error if not found

`isalnum()` : if string has ONLY a-z,A-Z,0-9 returns True ; otherwise False ; NO special chars

`isalpha()` : True ONLY if string has a-z & A-Z ; NO numbers & spl. chars

`islower()` : True if all chars are in LOWER case

`isupper()` : True if all chars are in UPPER case

`swapcase()` : swaps lower case to upper & vice-versa

`isprintable()` : True if all chars are printable ; false for \n \t etc.

`isspace()` : True if string has WHITE SPACES

`title()` : converts all FIRST letter of words to UPPER case

`istitle()` : True if first letter of ALL words are CAPS

