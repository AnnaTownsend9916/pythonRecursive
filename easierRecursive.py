#difference between recursive vs iterative

#recursive

def get_recursive_factorial(n):
#quick error check to indicate error
    if n<0:
        return -1
        #base case 
    elif n < 2:
        return 1
        #recursive case
    else:
        return n * get_recursive_factorial(n-1)
        
        
    
 #iterative
 def get_iterative_factorial(n):
     if n<0:
         return -1
     else:
         fact = 1
         for i in range(1, n+1):
             fact *= i
         return fact
         
  print(get_recursive_factorial(6))
  print(get_iterative_factorial(6))
