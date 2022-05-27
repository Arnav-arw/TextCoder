import wavio
import numpy as np

s = input("Enter your data: ")
s += '.'
filename = input("Enter filename(without extension): ")
print((''.join(map(bin,bytearray(s, 'utf-8')))))
binout = ((''.join(map(bin,bytearray(s, 'utf-8')))).replace("b", "")).replace(" ", "")
print(binout)

rate = 44100  
T = 1        
f1 = 1200.0
f2 = 2400.0   
start_sequence = 1800.0   
stop_sequence = 3600.0

ms = 10; 
samples = 44100//(1000//ms)

x = []
l = []

t = np.linspace(0, T, T*rate, endpoint=False)
x.append(np.sin(2*np.pi * start_sequence * t[:samples]))


for i in binout:
	t = np.linspace(0, T, T*rate, endpoint=False)
	if i == '0':
		x.append(np.sin(2*np.pi * f1 * t[:samples]))
	if i == '1':
		x.append(np.sin(2*np.pi * f2 * t[:samples]))


t = np.linspace(0, T, T*rate, endpoint=False)
x.append(np.sin(2*np.pi * stop_sequence * t[:samples]))
t = np.linspace(0, T, T*rate, endpoint=False)
x.append(np.sin(2*np.pi * stop_sequence * t[:samples]))
t = np.linspace(0, T, T*rate, endpoint=False)
x.append(np.sin(2*np.pi * stop_sequence * t[:samples]))

for i in x:
	for j in i:
		l.append(j);

l = np.array(l)

wavio.write(filename+".wav", l, rate, sampwidth=2)
