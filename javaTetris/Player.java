

public class Player{

    private int numberOfPieces = 0;
    private int score = 0; 

    public Player(){
        setNumPieces(0);
        setScore(0);
    }

    public void setNumPieces(int numPieces){
        this.numberOfPieces = numPieces;
    }

    public void setScore(int newScore){
        this.score = newScore;
    }

    public int getScore(){
    	return this.score;
    }
    public int getPieces(){
    	return this.numberOfPieces;
    }

}