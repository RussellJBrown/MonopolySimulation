import random
from turtle_mon import turtles

#In Jail
def gotojail(count,board,total):
	temp_count = 1	
	while temp_count == 3:
		dice1 = random.randint(1,6)
		dice2 = random.randint(1,6)
		temp_total = dice1 + dice2
		total = 11
		if dice1 == dice2:
			count += 1
			total = total+temp_total
			return count,board,total
		else: 	
			#if turns ends in jail add 1 to jail
			temp_t = board[total]		
			temp_t +=1
			board[total] = temp_t			
			count += 1
			temp_count+=1	
	return count,board,total		
		
	
def monopoly(count,board,total):
	temp_count = 1	
	while temp_count!=3:
		dice1 = random.randint(1,6)
		dice2 = random.randint(1,6)
		total_t = dice1 + dice2
		total = dice1 + dice2 + total
		if total >= 41:
			total = total - 40
			
		if dice1 == dice2:
			temp_count += 1
			count += 1				
			if temp_count == 3:
				total = 11
				count,board,total = gotojail(count,board,total)
				return count,board,total			
		else:		
			
			if total != 8 or total != 23 or total != 37: 
				
				temp_t = board[total]		
				temp_t +=1
				board[total] = temp_t
			#print(board)
		return count,board,total	
	
#The object of this code is to run 1000 games of monopoly, each of 100 rolls
#This checks for important squares, that have other effects such as chance, community chest, go to jail
#and will perform the action accordingly.	
if __name__ == "__main__":	
	board = [0]*41
	
	for q in range(0,1000):
		count = 1	
		i = 0
		total = 0	
		for i in range(0,100):
			i,board,total = monopoly(i,board,total)
			if total >= 41:
				total = total-40
				#checks for jail
			if total == 31:
				total = 11
				temp_t = board[11]		
				temp_t += 1
				board[total] = temp_t		
				i,board,total = gotojail(i,board,total)
				#represents the locations of community chest and chance
			if total == 3 or total == 18 or total == 34:
				value = random.randint(1,16)
				if value == 3:
					total = 11
					i,board,total = gotojail(i,board,total)
					temp_t = board[11]
					temp_t += 1
					board[11] = temp_t
				
				if value == 8:
					total = 1
					temp_t = board[total]		
					temp_t +=1
					board[total] = temp_t
			
				
			if total == 8 or total == 23 or total == 37:
				old_total = total
				
				value = random.randint(1,16)			
				#if certain value go to jail
				if value == 3:
					total = 11
					i,board,total = gotojail(i,board,total)
					temp_t = board[11]
					temp_t += 1
					board[11] = temp_t
					
				#move to closest railroad
				if value == 5:
					if total < 5 or total > 35:
						total = 6		
					elif total > 5 and total < 15:
						total = 16			
					elif total > 15 and total < 25: 	
						total = 26		
					elif total > 25 and total < 35:
						total = 36
					temp_t = board[total]		
					temp_t +=1
					board[total] = temp_t
				if value == 15:
					temp_t = board[6]		
					temp_t +=1
					board[total] = temp_t
				
				#move to start	
				if value == 8:
					total = 1
					temp_t = board[total]		
					temp_t +=1
					board[total] = temp_t					
				#move to nearest utility
				if value == 9:	
					if total < 12 or total > 28:	
						total = 13
						temp_t = board[total]		
						temp_t +=1
						board[total] = temp_t
					else:
						total = 29
						temp_t = board[total]		
						temp_t +=1
						board[total] = temp_t
				#move to Il ave				
				if value == 10:	
						total = 25
						temp_t = board[total]		
						temp_t +=1
						board[total] = temp_t
				if value == 11:	
						total = total - 3
						temp_t = board[total]		
						temp_t +=1
						board[total] = temp_t
				if total != old_total:		
						temp_t = board[total]		
						temp_t +=1
						board[total] = temp_t
						
		print("simulation")
		print(q)
	
	#Important places in monopoly
	print("final board state")							
	print("reading_railroad")
	print(board[6]/1000)
	print("Pen_railroad")
	print(board[16]/1000)
	print("B&O RailRoad")
	print(board[26]/1000)
	print("Short_railroad")
	print(board[36]/1000)
	print("Boardwalk")
	print(board[40]/1000)
	print("Go")
	print(board[1]/1000)
	print("Jail")
	print(board[11]/1000)
	
	#creates a visual repr
	t = turtles(board)