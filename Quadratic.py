#Made with love :) by AlexLSD

def quadratic():
	try:
		print("Welcome to the Quadratic Solver Application!!!")
		print("The equation for Quadratic is:")
		print("Ax^2+Bx+C")
		print("\n")
		print("Usage input: Ax,Bx,C ---- 1,5,-50")
		main = input("What is your Ax, Bx, C values?: ").split(",")
	
		Ax = int(main[0])
		Bx = int(main[1])
		C = int(main[2])
			
		print("Value of A:",Ax)
		print("Value of B:",Bx)
		print("Value of C:",C)
		#Factory of factoring!
		Yx = (Bx + (((Bx)**2)-4*Ax*C)**0.5)/2*Ax
		Zx = (Bx - (((Bx)**2)-4*Ax*C)**0.5)/2*Ax
		print("Factored form:")
		print("(X +", Yx.real , ")" , "(X +", Zx.real, ")")
		print("---") #Seperator
		print("Quadratic form:")
		print(Ax,"*x^2+",Bx,"*x+",C)
	except ValueError:
		print("\n \n \n \n \n")
		print("Hey, I never saw someone trying to use text or spaces as a number. That sounds cool though.")
		print("No worries, I will work on some things for people like you soon :)")
		print("\n \n")
		print("Restarting the application for you :)")
		print("\n \n")
		quadratic()
	except KeyboardInterrupt:
		print("\n \n \n \n \n")
		print("Thank you for using my applcation, and remember: compliments are nice :D")
		

quadratic()