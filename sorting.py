#insertion sort
#takes unsorted sequence and divides into two sub lists with sorted and an unsorted list
#takes left item and moves into sorted list to be compared to left, if its higher than item trying to sort it will move it to the left until there are no more higher numbers

#function takes in sequence 
def insertion_sort(list_a):
#all values after first one
    indexing_length = range(1, len(list_a))
    #for every value you want to sort them
    for i in indexing_length:
        value_to _sort = list_a[i]
        #condition to look for is if value on left is higher than right then sort 
       while list_a[i-1] > value_to_sort and i>0
       #swaps two values 
           list_a[i], list_a[i-1] = list_a[i-1],
           i = i-1
           
           
           
    return list_a
    
 print(insertion_sort([7,8,9,8,6,7,4])
 
 
 
 
 
 
 #selection sort
 #find minimum value in list by comparing value to right
 #at end of iteration it moves smallest to the left sorted list continues every time
 
 
 def selection_sort(list_a);
 #once its last item you can assume its highest since its last left
     indexing_length = range(0,len(list_a)-1
     #for every item in index length set min value to index
     for i in indexing_length:
         min_value = i
         #for every element on the right  if its less than current min replace with j element as min
         for j in range(i+1, len(list_a));
             if list_a[j] < list_a[min_value]:
                 min_value = j
                 
         #if item has lower value than default switch items by taking min and element and switching
        if min_value != i:
            list_a[min_value], list_a[i], list_a[min_value]
            
        return list_a
        
   print(selection_sort([7,7,8,9,6]))
   
   
   
   
   #bubble sort
   #orders it in ascending values
   #takes a ton of iterations going over each two and then doing another run
   
   
   def bubble(list_a):
   #cant perform on last item of list because there is nothing to compare it to
       indexing_length = len(list_a)-1
       #break out after list is sorted
       sorted = False
       
       #do these actions while false
       while not sorted:
           sorted = True
           for i in range(0, indexing_length):
           #if value is greater on left than right then sorted = false 
               if list_a[i] > list_a[i+1]:
                   sorted = False
                   #flip elements
                   list_a[i], list_a[i+1], list_a[i]
                   
                   
      return list_a
      
    print(bubble([4,6,5,3,2,6,4])
   
 
