# Python treats single quotes the same as double quotes
var1 = 'Hello World!'
var2 = "Python Programming"

# Accessing values in strings
# Python does not support a character type, no length attribute
print "var1[0]", var1[0]
print "var2[1:5]", var2[1:5]

# updating strings
print "Updating String :-", var1[:6] + 'Python'

# Special operators
# Assume a holds 'Hello' and b holds 'Python'
a = 'Hello'
b = 'Python'

# '+' is concatenation, it's for add values together
print a + b # HelloPython

# '*' is for repetition
print a*2 #HelloHello

# '[]' is slice, which gives the character from the given index
print a[1] # e

# '[ : ]' is Range Slice, which gives the characters from the given range
print a[1:4] # ell

# 'in' is membership, returns true if a character exists in the given string
print 'H' in a # true
print 'x' in a # false

# 'not in', membership, returns true if a character doesn't exist in the given string
print 'x' not in a #true

# String formatting operator
print "My name is %s and weight is %d kg!" % ('Hongbo', 74)
# "My name is Hongbo and weight is 74 kg!"

# %c    character
# %s    string conversion via str() prior to formatting
# %i    signed decimal integer
# %d    signed decimal integer
# %u    unsigned decimal integer
# %o    octal integer 8
# %x    hexadecimal integer(lowercase letters)
# %X    hexadecimal integer(UPPERcase letters)
# %e    exponential notation(with lowercase 'e')
# %E    exponential notation(with UPPERcase 'E')
# %f    floating point real number
# %g    the shorter of %f and %e
# %G    the shorter of %f and %E

# Triple quotes
# Python's triple quotes comes to the rescue by allowing strings ot span multiple lines, including verbatim NEWLINEs, TABs, and any other special characters.
# Syntax: 3 consecutive single or double quotes
para_str =  """
This is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
            """
print para_str

# Raw strings: every character you put into a raw string stays the way you wrote it.
print 'C:\\nowhere' # C:\nowhere

print r'C:\\nowhere' # C:\\nowhere
