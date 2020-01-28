#Assignment1: Quality
#Convert Arabic Numerals to Roman Numerals
import sys

def convert(a):
  II = ['','I','II','III','IV','V','VI','VII','VIII','IX']
  XX = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
  CC = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
  MM = ['','M','MM','MMM']
  if type(a) is int:
    if a <= 0:
      return "Please enter a number greater than 0"
    elif a >= 4000:
      return "Out of range"
    else:
      return MM[a//1000] + CC[(a%1000)//100] + XX[(a%100)//10] + II[a%10]
  else:
    return "Please enter a integer"



if __name__ == '__main__':
  arabics = [-1,0,2.3,1,3,4,9,10,13,40,42,117,450,904,1993]
  for a in arabics:
    print(convert(a))