(*BRANDON CAMPBELL
 CS 355 FALL 2018 WSU
 ASSIGNMENT 2
*)




(*map, fold and filter declarations as they will be used extensively
throughout the assignment*)

fun map f [] = []
	| map f (x::rest) = (f x)::(map f rest); 
	
fun fold f base [] = base
	| fold f base (x::rest) = f x (fold f base rest);
	
fun filter pred [] = []
	| filter pred (x::rest) = if pred x then x::(filter pred rest)
							  else (filter pred rest);
							  
							
							
							
							
							
							
							
(*1.*)

(*a. numbersToSum*)
fun numbersToSum sum [] = []
	|numbersToSum 0 _ = []
	|numbersToSum sum (x::rest) = if x > sum then numbersToSum sum rest	
								  else x::(numbersToSum (sum-x) rest);
								  

(*b. numbersToSum but with tail recursion*)
(*was not sure how to have the function input values and return value remain the same as the non-tail recursion version*)			
fun tailNumbersToSum sum accum [] = rev accum
	|tailNumbersToSum 0 _ _ = []
	|tailNumbersToSum sum accum (x::rest) = if x > sum then tailNumbersToSum sum accum rest	
								  else (tailNumbersToSum (sum-x) (x::(accum)) rest);


(*2*)
(*Partition*)
partition f [] = ([], [])
	| partition f (x::rest) = 
	(*we're going to need some sort of helper function that allows for 
	the creation and merging of two separate lists from filter. Need
	to study for interview now, so I will revisit this soon
		
		
								  





















