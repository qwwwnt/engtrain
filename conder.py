import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)
numbers = [10, 9, 11, 5, 6, 13, 19, 26]

GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN)

for i in numbers:
    GPIO.setup(n, GPIO.OUT)
for n in range(8):
    GPIO.output(numbers[i], 0)

def decToBinList(decNumber):
  bnumber = bin(decNumber)
  ddnumber = bnumber[2:15:1]
  N = ddnumber.zfill(8)
  a = [0, 0, 0, 0, 0, 0, 0, 0]
  for i in range(8):
    a[i] = int(N[i])
  return(a)
  
def dac2dac(decNumber):
    p = decToBinList(decNumber)


def lightNumber(decNumber):
    n = decToBinList(decNumber)
    for i in range(8):
        GPIO.output(numbers[7-i], n[i])

def num2dac(n):
  lightNumber(n)

def bsearch():
    l = 0
    p = 255
    while (p - l>=2):
        c = ((p+l)//2)
        num2dac(c)
        time.sleep(0.001)
        if((GPIO.input(4))):
            l = c
        else:
            p = c
    if (not(GPIO.input(4))) : return (c-1)
    if ((GPIO.input(4))) : return (c+1)
    else: return (c)   

def searchst(n):
  for k in range(9):
    if (32*k>=n): return(k)


try:
  GPIO.output(17,1)
  t_start = t.time()
  listV = []
  listT = []
  f = 0
  while(f<245):
    f = bsearch()
    listV.append((f*3.3)/255)
    listT.append(t.time()-t_start)
    n = int(searchst(f))
    lightNumber(2**n-1)
    print((f*3.3)/255)
    
  GPIO.output(17,0)
  while(f>0):
    f = bsearch()
    listV.append((f*3.3)/255)
    listT.append(t.time()-t_start)
    n = int(searchst(f))
    lightNumber(2**n-1)
    print((f*3.3)/255)

  np.savetxt("data.txt", listV, fnt = '%d')
  plt.plot(listT, listV)
  plt.title("conder")
  plt.xlabel("time")
  plt.ylabel("voltage")
  plt.show()

finally:
    GPIO.cleanup() 