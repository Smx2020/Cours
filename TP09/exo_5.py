#def F(a,b,x,y):
#	return(a*x - b*x*y)

#def G(c,y,d,x):
#	return(-1*c*y + d*x*y)

def Eulers1(tmin,tmax,F,G,x0,y0,n):
	h = (tmax-tmin)/n
	T = [tmin]
	Y = [y0]
	X = [x0]
	for i in range(n):
		T.append(T[i] + h)
		X.append(X[i] + h*F(X[i],Y[i],T[i]))
		Y.append(Y[i] + h*G(X[i],Y[i],T[i]))
	return(T,X,Y)

def trace_Euler1s(tmin,tmax,F,G,x0,y0):
	
