

def quadratic():    
		print("Welcome to the Quadratic Solver Application!!!")
		print("The equation for Quadratic is:")
		print("Ax^2+Bx+C")
		Ax = int(input("What is your Ax value?: "))
		Bx = int(input("What is your Bx value?: "))
		C = int(input("What is your C value?: "))
		
		print("Value of A:",Ax)
		print("Value of B:",Bx)
		print("Value of C:",C)
		Yx = (Bx + (((Bx)**2)-4*Ax*C)**0.5)/2*Ax
		Zx = (Bx - (((Bx)**2)-4*Ax*C)**0.5)/2*Ax
		print("Factored form:")
		print("(X +", Yx, ")" , "(X +", Zx, ")")
		print("---") #Seperator
		print("Quadratic form:")
		print(Ax,"*x^2+",Bx,"*x+",C)
    
quadratic()