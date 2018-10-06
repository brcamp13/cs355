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
		
		fold add 0 (fold combine [] List)  (*In essence, combine all lists and then add up all values in that compressed list*)
		
		end;
		
(*4b*)

fun sumOption [] = SOME(0)
	| sumOption List = 
		let
			fun addOption x y = SOME((valOf (x)) + (valOf (y))) 
			fun combineOption x y = x @ y
		in
		
		fold addOption (SOME(0)) (fold combineOption [] List) (*Same idea as sum, but with int options instead of just ints*)

		end;
		
		
		
		
(*Due to the career fair and having two exams on Wednesday, I wasn't able to complete the remaining problems*)
	
fun numbersToSumTest () =
 let 
     val numbersToSumT1 = ( numbersToSum 4 [1,2,4,5,3,8,2,3]) = ([1,2])
     val numbersToSumT2 = ( numbersToSum 6 [1,2,1,1,5,3,8,2,3]) = ([1,2,1,1])
     val numbersToSumT3 = ( numbersToSum 0 [1,2,4,5,3,8,2,3]) = ([])
 in 
     print ("numbersToSum:-------------------- \n   test1: " ^ Bool.toString(numbersToSumT1) ^  "\n" ^
            "   test2: " ^ Bool.toString(numbersToSumT2) ^ "\n" ^ 	
            "   test3: " ^ Bool.toString(numbersToSumT3) ^ "\n")		

end;

		
		
		
fun partitionTest () =
 let 
	 fun exists n [] = false |  exists n (x::rest) = if n=x then true else (exists n rest)
     val partitionT1 = ( (partition (fn x => (x<=4)) [1,7,4,5,3,8,2,3]) = ([1,4,3,2,3],[7,5,8]) )
     val partitionT2 = ( (partition null [[1,2],[1],[],[5],[],[6,7,8]]) = ([[],[]],[[1,2],[1],[5],[6,7,8]]) )
     val partitionT3 = ( (partition (exists 1) [[1,2],[1],[],[5],[],[6,7,8]]) = ([[1,2],[1]],[[],[5],[],[6,7,8]]) )
 in 
     print ("partition:-------------------- \n   test1: " ^ Bool.toString(partitionT1) ^  "\n" ^
            "   test2: " ^ Bool.toString(partitionT2) ^ "\n" ^ 	
            "   test3: " ^ Bool.toString(partitionT3) ^ "\n")		

end;


fun areAllUniqueTest () =
 let 
     val areAllUniqueT1 = ( areAllUnique [1,2,3,4,5,6]) = (true)
     val areAllUniqueT2 = ( areAllUnique [1,2,3,4,5,5,6]) = (false)
     val areAllUniqueT3 = ( areAllUnique [1,2,3,4,5,6,7,8,9,100,9]) = (false)
 in 
     print ("areAllUnique:-------------------- \n   test1: " ^ Bool.toString(areAllUniqueT1) ^  "\n" ^
            "   test2: " ^ Bool.toString(areAllUniqueT2) ^ "\n" ^ 	
            "   test3: " ^ Bool.toString(areAllUniqueT3) ^ "\n")		

end;

fun sumTest () =
 let 
     val sumT1 = ( sum [[1,2,3],[4,5,6]]) = (21)
     val sumT2 = ( sum [[3,4,5], [0,1,4]]) = (17)
     val sumT3 = ( sum []) = (0)
 in 
     print ("sum:-------------------- \n   test1: " ^ Bool.toString(sumT1) ^  "\n" ^
            "   test2: " ^ Bool.toString(sumT2) ^ "\n" ^ 	
            "   test3: " ^ Bool.toString(sumT3) ^ "\n")		

end;

fun sumOptionTest () =
 let 
     val sumOptionT1 = ( sumOption [[SOME(1),SOME(2),SOME(3)],[SOME(4),SOME(5),SOME(6)]]) = (SOME(21))
     val sumOptionT2 = ( sumOption [[SOME(3),SOME(4),SOME(5)], [SOME(0),SOME(1),SOME(4)]]) = (SOME(17))
     val sumOptionT3 = ( sumOption []) = (SOME(0))
 in 
     print ("sumOption:-------------------- \n   test1: " ^ Bool.toString(sumOptionT1) ^  "\n" ^
            "   test2: " ^ Bool.toString(sumOptionT2) ^ "\n" ^ 	
            "   test3: " ^ Bool.toString(sumOptionT3) ^ "\n")		

end;






val _ = numbersToSumTest();
val _ = partitionTest();
val _ = areAllUniqueTest();
val _ = sumTest();
val _ = sumOptionTest();
	
	
	
	









	
			
			
			