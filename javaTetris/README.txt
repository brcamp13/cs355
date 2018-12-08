Clarification of the process of this program: 
Goes through every element in the board. If the element is a number, it first checks if it is a part of a '355' configuration. 
If it is, it marks '1' on the corresponding locations of the potentialDeletionLocations 2d array, to signify an element to be deleted
. If it's not a '355' configuration, it moves on to the next part. This part (deletePieces) recursively looks around the current element 
for any cells (left, right, or below) that have the same value. If any cell does have the same value, the function is called again, passing 
in the location of the new cell as a parameter. Corresponding potentialDeletionLocations locations are marked as '1'. 
It then performs the same check. Once this function finishes (no more cells to explore), it 
returns. A counter variable is kept and incremented by 1 each time an adjacent cell has the same value. If the count is > 2 (a path > 2 of 
the same values), then the potentialDeletionLocations array is scanned for 1's, and for each cell with a 1, makes the corresponding location 
in 'board' a space. Then, the bored array is checked to see if there any gaps (using shiftDown()). If there are any gaps, this function fills 
them.
This is pretty much the entirety of it. 