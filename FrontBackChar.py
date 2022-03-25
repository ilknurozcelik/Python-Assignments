'''
Given a string, return a new string where the first and last chars have been exchanged. For example:

print(front_back('clarusway')) --> ylaruswac

print(front_back('a')) --> a

print(front_back('ab')) --> ba
'''

def front_back(word):
  return word[-1] + word[1:-1] + word[0] if len(word) > 1 else word

front_back("clarusway")
