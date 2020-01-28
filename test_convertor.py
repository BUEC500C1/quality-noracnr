import pytest
import convertor

def test_answer():

  arabic = [1,2,3,4,78,420,1939, 3999]
  romans = ['I','II','III','IV','LXXVIII','CDXX','MCMXXXIX', 'MMMCMXCIX']
  for a, r in zip(arabic,romans):
    assert convertor.convert(a) == r

def test_exception1():
  arabic = [-1, 0, -32154356]
  expections1 = "Please enter a number greater than 0"
  for a in arabic:
    assert convertor.convert(a) == expections1

def test_exception2():
  arabic = ["a",'748291']
  expections2 = "Please enter a integer"
  for a in arabic:
    assert convertor.convert(a) == expections2

def test_exception3():
  arabic = [4000,67238]
  expections3 = "Out of range"
  for a in arabic:
    assert convertor.convert(a) == expections3
