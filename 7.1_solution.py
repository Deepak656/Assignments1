# I will be using PYTHON to demonstrate If, else, while, for, recursion, switch, continue, closure.

IF, ELSE & FOR, WHILE & CONTINUE
      # Let's try to understand If, else condition and for loop using a palindrome problem.
  
      #Given an array a = [4,2,6,6,2,4] , return true if it's a palindrome else return false.
      # Palindrome Problem
      for i range(len(a)):
        if a[i] != a[n-1-i]:
          return False
        else : 
          continue
      return True
        
      #Same problem can be solved using While Condition
      n = len(a)
      i = 0
      j = n-1
      while (i < j):
      	if a[i] != a[j]:
          return False
        i +=1
        j -=1
      return True
  
SWITCH CASE
		
	#Concept of Switch statement in javascript
	switch(argument) {
		case 'Monday' : 
		case 'Tuesday':
		case 'Wednesday':
		    console.log("Alarm at 8 AM");
			break;
		case 'Thursday' :
		case 'Friday':
			console.log("Alarm at 7 AM");
			break;
		case 'Saturday' : 
		case 'Sunday' :
			console.log("Alarm at 10 AM");
			break;
		defualt : 
			console.log("Invalid Input";
	};
						
    #Implementation of Switch case in Python
	#We will implement switch case using dictionary in python
	def switch_example(day):
		d = { 'Monday': 'Alarm at 8 AM',
			  'Tuesday' : 'Alarm at 8 AM',
			  'Saturday': 'Alarm at 6 AM,
			  'Sunday': 'No Alarm'}
		return d[day]
  
RECURSION
        # Let's try to understand recursion using Fibonacci Sequence.

        # Fibonacci sequence is 0,1,1,2,3,5.....
        # Here nth element is sum of previous two elements. i.e, F(n) = F(n-1)+F(n-2). Where F(n) is the nth element of the sequence.
        # Fibonacci Sequence
        def fibonacci(n):
          if n == 1:
            return 0
          elif n == 2:
            return 1
          else :
            return fibonacci(n-1) + fibonacci(n-2)
CLOSURES
						
	def multiplier_outer(n):
		def multiplier_inner(x)
			return x*n
		return multiplier_inner
	
	#times = multiplier_outer(3)
	#times(5) ---> 15
				
    
    
    
