>>> def is_a_vowel(c):
...     return c.lower() in "aeiou"
... 
>>> is_a_vowel('i')
True
>>> 
>>> def report_if_vowel(c):
...     if is_a_vowel(c):
...         print('yes')       
...     else:
...         print('no')       
...             
... report_if_vowel('i')
  File "<stdin>", line 7
    report_if_vowel('i')
                  ^
SyntaxError: invalid syntax
>>> 