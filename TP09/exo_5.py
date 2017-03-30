import matplotlib.pyplot as plt

def Euler1s(tmin,tmax,F,G,x0,y0,n):
	h = (tmax-tmin)/n
	T = [tmin]
	Y = [y0]
	X = [x0]
	for i in range(n):
		T.append(T[i] + h)
		X.append(X[i] + h*F(X[i],Y[i],T[i]))
		Y.append(Y[i] + h*G(X[i],Y[i],T[i]))
	return(T,X,Y)

def trace_Euler1s(tmin,tmax,F,G,x0,y0,n):
	[T,X,Y] = Euler1s(tmin,tmax,F,G,x0,y0,n)
	plt.plot(T,X)
	plt.plot(T,Y)
	plt.show()

def F1(x,y,t):
	a = 0.6
	b = 0.8
	return(a*x - b*x*y)

def G1(x,y,t):
	c = 0.6
	d = 0.3
	return(-1*c*y + d*x*y)

def F2(x,y,t):
	a = 1.5
	b = 0.05
	return(a*x - b*x*y)

def G2(x,y,t):
	c = 0.48
	d = 0.05
	return(-1*c*y + d*x*y)

def trace_phase__LVa(tmin,tmax,F,G,LX,LY,n):
	for i in range(len(LX)):
		a = 0
		for j in range(len(LY)):
			[T,X,Y] = Euler1s(tmin,tmax,F,G,LX[i],LY[j],n)
			if a == 0:
				plt.plot(T,X)
				a = 1
			plt.plot(T,Y)
		plt.show()
		a = 0



trace_Euler1s(0,50,F1,G1,5,1,1000)
trace_Euler1s(0,50,F2,G2,4,10,1000)

trace_phase__LVa(0,50,F1,G1,[4],[10,15,30,40],1000)
