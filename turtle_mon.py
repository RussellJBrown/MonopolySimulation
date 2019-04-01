import turtle

class turtles():
	def __init__(self,prob):
		turtle.setup(1000,1000)
		turtle.speed(0)
		self.name = turtle.Turtle()
		self.name.penup()
		self.name.goto(-500,-500)
		self.name.pendown()
		self.name.goto(-500,500)
		self.name.goto(500,500)
		self.name.goto(500,-500)
		self.name.goto(-500,-500)
		self.name.penup()
		self.name.goto(-250,-250)
		self.name.pendown()
		self.name.goto(-250,250)
		self.name.goto(250,250)
		self.name.goto(250,-250)
		self.name.goto(-250,-250)		
		i = 1
		j = 350
		k = -350
		#0-3 times landed Green
		#>3 and <6 landed Yellow
		#6> landed Red	
		self.name.width(10)
		for i in range(1,11):
			self.name.penup()
			self.name.goto(j,k)
			self.name.pendown()		
			if(prob[i]/1000<=2.1):
				self.name.pencolor("green")	
			elif(prob[i]/1000<=2.7 and prob[i]/1000>2.1):
				self.name.pencolor("yellow")
			elif(prob[i]/1000>2.7):	
				self.name.pencolor("red")
			self.name.dot()
			j = j - 70			
		i = 11
		j = -350
		k = -350		
		for i in range(11,21):
			self.name.penup()
			self.name.goto(j,k)
			self.name.pendown()		
			if(prob[i]/1000<=2.1):
				self.name.pencolor("green")	
			elif(prob[i]/1000<=2.7 and prob[i]/1000>2.1):
				self.name.pencolor("yellow")
			elif(prob[i]/1000>2.7):	
				self.name.pencolor("red")
			self.name.dot()
			k = k + 70
		i = 21		
		j = -350
		k = 350	
		for i in range(21,31):
			self.name.penup()
			self.name.goto(j,k)
			self.name.pendown()		
			if(prob[i]/1000<=2.1):
				self.name.pencolor("green")	
			elif(prob[i]/1000<=2.7 and prob[i]/1000>2.1):
				self.name.pencolor("yellow")
			elif(prob[i]/1000>2.7):	
				self.name.pencolor("red")
			self.name.dot()
			j = j + 70			
		i = 31
		j = 350
		k = 350		
		for i in range(31,41):
			self.name.penup()
			self.name.goto(j,k)
			self.name.pendown()		
			if(prob[i]/1000<=2.1):
				self.name.pencolor("green")	
			elif(prob[i]/1000<=2.7 and prob[i]/1000>2.1):
				self.name.pencolor("yellow")
			elif(prob[i]/1000>2.7):	
				self.name.pencolor("red")
			self.name.dot()
			k = k - 70
		
		
			
		turtle.done()