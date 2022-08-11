"""
Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.


sorta_sum(3, 4) → 7
sorta_sum(9, 4) → 20
sorta_sum(10, 11) → 21
"""

def sorta_sum(a, b):
  if a+b==10:
    return 20
  elif a+b==11:
    return 20
  elif a+b==12:
    return 20
  elif a+b==13:
    return 20
  elif a+b==14:
    return 20
  elif a+b==15:
    return 20
  elif a+b==16:
    return 20
  elif a+b==17:
    return 20
  elif a+b==18:
    return 20
  elif a+b==19:
    return 20
  else:
    return a+b

