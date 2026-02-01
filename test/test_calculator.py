from app.calculator import add,substract

'''
from app -> folder
calculator -> filename
import add,substact (functions)
'''

def test_add ():
  assert add(2,3) == 5

def test_substract ():
  assert substract(5,3) == 2
