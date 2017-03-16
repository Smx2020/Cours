def Euler1(tmin,tmax,F,y0,n):
	h = (tmax-tmin)/n
	t = tmin
	for k in range(n+1):
		
		t = t + h
