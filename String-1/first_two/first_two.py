#Given a string, return the string made of its fir
#st two chars, so the String "Hello" yields "He".
#If the string is shorter than length 2, return whatever
#there is, so "X" yields "X", and the empty string
#"" yields the empty string "".


#first_two('Hello') → 'He'
#first_two('abcdefg') → 'ab'
#first_two('ab') → 'ab'

def first_two(str):
  if len(str)>2:
    return str[:2]
  elif len(str):
    return str
  else:
    return ""