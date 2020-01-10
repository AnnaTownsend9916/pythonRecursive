#you have a bunch of coins
#You have an amount of change you need to make
#do so in as few coins as possible

#4.33

def return_change(to_return, coins = [.01, .05, .10, .25, 1.0, 5.0]:
#how much change you have, you can keep track of values less than amount you want change for
    flag = None
    for c in coins:
        if c == to_return:    return c
        if c < to_return: 
            flag = c
       return flag
   temp_balance = round(to_return - flag, 2)
   return [flag] + return_change(temp_balance)
       
 result=  return_change(4.33) #highly nested iterable, helps you see what recursion is doing
 result
 
 #if not an iterable it raises type error meaning its an item already
 def flatten(L):
     for item in L:
         try:
             yield from flatten(item)
         except TypeError:
             yield item
 #would return a generator which needs to be exhausted and then will return list
 #remember to round so its not false
 
 round(sum(list(flatten(result))), 2)
