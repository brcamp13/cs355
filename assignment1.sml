
(*Question 1*)
(*a*)

fun exists (_, []) = false
	| exists (searchValue, x::rest) = 
		if searchValue = x then true
		else exists (searchValue, rest);
		

(*b*)
(* the `a alpha is a type variable where you can plug in any type for `a, but you must be consistent. In the case 
the function in part a, the type of the function is ``a * ``a list because the function does equality testing, 
and the ``a is a type variable that can only be substituted by types that support equality testing *)

(*c*)
(*General pseudocode: check first item of the list. If it is the value you are counting, return 1 + countInLists.
Otherwise, return countInLists. I believe that this should work*)
fun countInList (_, []) = 0
	| countInList(searchValue, currentValue::inputList) =
		if currentValue = searchValue then 1 + countInList(searchValue, inputList)
		else countInList(searchValue, inputList);
	
	
(*Question 2*)
(*Right now it works, but not really with duplicates*)
fun listDiff ([], []) = []
	| listDiff ([], _) = []
	| listDiff (x::first, second) = 
		if exists (x, second) then listDiff (first, second)
		else x::(listDiff (first, second) );
		
		
				
(*Question 3*)
(*Took a LOT of parentheses manipulation*)
fun firstN [] n = []
	|firstN _ 0 = []
	|firstN (x::rest) n = x::(firstN rest (n-1))
	
(*Question 4*)
(*Part a*)
fun busFinder _ [] = []
	|busFinder busStop ((x, y)::xs) = 				   (*x becomes the bus name, y becomes the list of stops that bus goes to*)	
		if exists (busStop, y) then x::(busFinder busStop xs)   (*if the bus stop exists in the list of bus stops for the current bus, then add that bus to the return list*)
		else busFinder busStop xs;
		
(*Part b*)
(*The reason that the type is ''a -> ('b * ''a list) list 0> 'b list and not
''a -> ('a * ''a list) list -> 'a list is because within the list of tuples, 
the bus stop names are compared to one another and are seen as the same type
whereas the bus names are not compared to one another and are seen as their 
own independent type, or at least as different to the bus stop names. 

*)
		
		
(*Question 5*)
fun parallelResistors [] = 0.0
	|parallelResistors (x) =
	let
		fun inverseSum [] = 0.0
			| inverseSum (y::ys) = 
				((1.0/y) + (inverseSum ys))
		
	in
		(1.0/(inverseSum x))
	end;
		
	
(*My function returns the results that are expected (based on what the assignment says).
It returns these results because the function simulates the given formula.
The real type is used hence the reason there is a decimal point *)


(*Question 6*)	
fun pairNright (number , []) = [[]]
	| pairNright (number , (inputList)) = 
		let 
			fun length [] = 0
				|length (y::rest) = 
					(length rest + 1)
		
			fun helperFunction number [] buffer = [rev buffer]
				| helperFunction number (x::xs) buffer = 
					if (length buffer = number) then (rev buffer)::(helperFunction number xs [x])
					else helperFunction number xs (x::buffer)
		in
			helperFunction number inputList []
		end;
		
		
fun pairNleft (number , []) = [[]]
	| pairNleft (number , (inputList)) = 
		let 
			fun length [] = 0
				|length (y::rest) = 
					(length rest + 1)
		
			fun helperFunction number [] buffer = [buffer]
				| helperFunction number (x::xs) buffer = 
					if (length buffer = number) then (buffer)::(helperFunction number xs [x])
					else helperFunction number xs (x::buffer)
		in
			rev (helperFunction number (rev inputList) [])
		end;
		
		
		
		
		
(*TESTS*)



fun existsTest () =
	let
		val existsT1 = ((exists (1, [1,2,3,4,5,6])) = true)     
		val existsT2 = ((exists (9, [1,2,3,4,5,6])) = false) 
		val existsT3 = ((exists (4, [1,2,3,4,5,6])) = true)  
	in     
	 print ("exists:-------------------- \n" ^ "   test1: " ^         
			 Bool.toString(existsT1) ^ "\n" ^ "   test2: " ^        
			 Bool.toString(existsT2) ^ "\n" ^ "   test3: " ^ 
			 Bool.toString(existsT3) ^ "\n")
			 
	end;
	
	


fun countInListTest () =
	let
		val countInListT1 = ((countInList (1, [1,2,3,4,5,6])) = 1)     
		val countInListT2 = ((countInList (9, [1,2,3,4,5,6])) = 0) 
		val countInListT3 = ((countInList (4, [1,2,3,4,4,4,4,4,5,6])) = 5)  
	in     
	 print ("countInList:-------------------- \n" ^ "   test1: " ^         
			 Bool.toString(countInListT1) ^ "\n" ^ "   test2: " ^        
			 Bool.toString(countInListT2) ^ "\n" ^ "   test3: " ^ 
			 Bool.toString(countInListT3) ^ "\n")
			 
	end;
	
	
fun listDiffTest () =
	let
		val listDiffT1 = ((listDiff ([1,2,3,4,5,6], [4,5,6])) = [1,2,3])     
		val listDiffT2 = ((listDiff ([2,3,4,6,8], [1,2,4])) = [3,6,8])     
		val listDiffT3 = ((listDiff ([1,4,7,99], [4])) = [1,7,99])     
	in     
	 print ("listDiff:-------------------- \n" ^ "   test1: " ^         
			 Bool.toString(listDiffT1) ^ "\n" ^ "   test2: " ^        
			 Bool.toString(listDiffT2) ^ "\n" ^ "   test3: " ^ 
			 Bool.toString(listDiffT3) ^ "\n")
			 
	end;
	
	
fun firstNTest() =
	let
		val firstNT1 = ((firstN [1,2,3,4,5,6] 3) = [1,2,3])     
		val firstNT2 = ((firstN [1,2,3,4,5,6] 1) = [1])
		val firstNT3 = ((firstN [1,2,3,4,5,6] 5) = [1,2,3,4,5]) 
	in     
	 print ("firstN:-------------------- \n" ^ "   test1: " ^         
			 Bool.toString(firstNT1) ^ "\n" ^ "   test2: " ^        
			 Bool.toString(firstNT2) ^ "\n" ^ "   test3: " ^ 
			 Bool.toString(firstNT3) ^ "\n")
			 
	end;
	
fun busFinderTest () =
	let
		 val buses =
		[("Lentil",["Chinook", "Orchard", "Valley", "Emerald","Providence", "Stadium",
		"Main", "Arbor", "Sunnyside", "Fountain", "Crestview", "Wheatland", "Walmart",
		"Bishop", "Derby", "Dilke"]),
		("Wheat",["Chinook", "Orchard", "Valley", "Maple","Aspen", "TerreView", "Clay",
		"Dismores", "Martin", "Bishop", "Walmart", "PorchLight", "Campus"]),
		("Silver",["TransferStation", "PorchLight", "Stadium", "Bishop","Walmart",
		"Shopco", "RockeyWay"]),
		("Blue",["TransferStation", "State", "Larry", "TerreView","Grand", "TacoBell",
		"Chinook", "Library"]),
		("Gray",["TransferStation", "Wawawai", "Main", "Sunnyside","Crestview",
		"CityHall", "Stadium", "Colorado"])]

		 val busFinderT1 = ((busFinder "Walmart" buses) = ["Lentil","Wheat","Silver"])
		 val busFinderT2 = ((busFinder "Shopco" buses) = ["Silver"])
		 val busFinderT3 = ((busFinder "Main" buses) = ["Lentil","Gray"])
	in
		 print ("busFinder:-------------------- \n" ^
		 " test1: " ^ Bool.toString(busFinderT1) ^ "\n" ^
		 " test2: " ^ Bool.toString(busFinderT2) ^ "\n" ^
		 " test4: " ^ Bool.toString(busFinderT3) ^ "\n")
	end;
	
	
	
fun parallelResistorsTest () =
	let
		val parallelResistorsT1 = Real.==((parallelResistors [10.0, 10.0, 10.0, 10.0]), 2.5)      
		val parallelResistorsT2 = Real.==((parallelResistors [8.0, 16.0, 4.0, 16.0]), 2.0) 
		val parallelResistorsT3 = Real.==((parallelResistors [5.0, 10.0, 2.0]) , 1.25) 
	in     
	 print ("parallelResistors:-------------------- \n" ^ "   test1: " ^         
			 Bool.toString(parallelResistorsT1) ^ "\n" ^ "   test2: " ^        
			 Bool.toString(parallelResistorsT2) ^ "\n" ^ "   test3: " ^ 
			 Bool.toString(parallelResistorsT3) ^ "\n") 
	end;
	
	
fun pairNrightTest () =
	let
		val pairNrightT1 = ((pairNright (2, [1,2,3,4,5,6,7]))) = [[1,2], [3,4], [5,6], [7]]      
		val pairNrightT2 = ((pairNright (3, [1,2,3,4,5,6,7]))) = [[1,2,3], [4,5,6], [7]]  
		val pairNrightT3 = ((pairNright (2, [1,2,3,4,5,6,7,8]))) = [[1,2], [3,4], [5,6], [7,8]] 
	in     
	 print ("pairNRight:-------------------- \n" ^ "   test1: " ^         
			 Bool.toString(pairNrightT1) ^ "\n" ^ "   test2: " ^        
			 Bool.toString(pairNrightT2) ^ "\n" ^ "   test3: " ^ 
			 Bool.toString(pairNrightT3) ^ "\n") 
	end;
	
	
fun pairNleftTest () =
	let
		val pairNleftT1 = ((pairNleft (2, [1,2,3,4,5,6,7]))) = [[1], [2,3], [4,5], [6,7]]      
		val pairNleftT2 = ((pairNleft (3, [1,2,3,4,5,6,7]))) = [[1], [2,3,4], [5,6,7]]  
		val pairNleftT3 = ((pairNleft (2, [1,2,3,4,5,6,7,8]))) = [[1,2], [3,4], [5,6], [7,8]] 
	in     
	 print ("pairNleft:-------------------- \n" ^ "   test1: " ^         
			 Bool.toString(pairNleftT1) ^ "\n" ^ "   test2: " ^        
			 Bool.toString(pairNleftT2) ^ "\n" ^ "   test3: " ^ 
			 Bool.toString(pairNleftT3) ^ "\n") 
	end;

	
	
	val _ = existsTest ();
	val _ = countInListTest ();
	val _ = listDiffTest ();
	val _ = firstNTest ();
	val _ = busFinderTest ();
	val _ = parallelResistorsTest ();
	val _ = pairNrightTest ();
	val _ = pairNleftTest ();
		
		
		
	
		