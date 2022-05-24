import numpy as np
def sgn(numero):
    if(numero > 0):
        return 1
    if(numero < 0):
        return -1
    else:
        return 0
def expansor(data,u):
    temp=sgn(data)*(1/u)*(((1+u)**(abs(data)))-1)
    return temp
def compresor(data,u):
    ln1plusU=np.log(1+u)
    temp=sgn(data)*(np.log(1+(u*abs(data)))/ln1plusU)
    return temp
print(expansor(5/128,255))
print(compresor(66/32768,255))
print("ln 10 ", np.log(10))
num=5
bytesval=num.to_bytes(1,'big')
print(bytesval)
