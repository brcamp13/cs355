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
fun partition F L = (filter F L, filter (not o F) L); (*uses function composition to pass into filter the opposite of whatever function was initially passed in*)



(*3*)
(*Idea behind this process: 
The newMap function takes the input list and returns a list of 1's and 0's representing the presence of a repeated elements
So if there are no repeated elements, then the list would be comprised of all 0's, and if there is > 0 1's, then there is a repeated element somewhere
Then, call filter upon this new list, with the function x > 0, meaning it will return a list of any 1's that exist in the mapped list
So if there is a single element in this list, that means there is a repeated number within the list
Therefore, compare this resulting list to the empty list in order to get the result, as empty list means no repeating elements which == true when compared to empty list
*)
fun areAllUnique List =
	let
		fun countInList _ [] = 0
			| countInList searchValue (currentValue::inputList) =
								if currentValue = searchValue then 1 + countInList searchValue inputList
								else countInList searchValue inputList;
		fun newMap f [] = []
			| newMap f (x::rest) = (f x rest)::(newMap f rest); (*A slight alteration of map which allows for a function with two parameters*)
	in	
		if List = [] then false
		else (filter (fn x => (x > 0)) (newMap countInList List)) = [] (*This filters n elements into a new list, where n corresponds to number of repeated elements. So comparing it to empty list returns correct bool (list should be empty if all unique, hence true)*)
	end;
	
(*4*)

(*4a *)

fun sum [] = 0
	| sum List = 
		let	
			fun add x y = x+y
			fun combine x y = x @ y
		in
		
		fold add 0 (fold combine [] List)  
		
		end;
		
(*4b*)

fun sumOption [] = SOME(0)
	| sumOption List = 
		let
			fun addOption x y = SOME((valOf (x)) + (valOf (y))) 
			fun combineOption x y = x @ y
		in
		
		fold addOption (SOME(0)) (fold combineOption [] List)

		end;
		
		
(*4c*)

datatype either = Istring of string | Iint of int

sumEither [] = Iint 0
	| sumEither List = 
		let
		
		in
		
		end;
	
	
	









	
			
			
			