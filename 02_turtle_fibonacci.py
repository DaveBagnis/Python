from turtle import *

f1 = 1
f2 = 1
i = int(raw_input("Inserisci il numero di segmenti della spirale: "))
for x in range(i):
	f3 = f1 + f2
	f1 = f2
	f2 = f3
	forward(10*f1)
	right(90)
end_fill()
done()