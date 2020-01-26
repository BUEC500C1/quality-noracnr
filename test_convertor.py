import pytest
import convertor

def test_answer():
  arabic = [1,2,3,4,78,420,1939]
  romans = ['I','II','III','IV','LXXVIII','CDXX','MCMXXXIX']
  for a, r in zip(arabic,romans):
    assert convertor.convert(a) == r