package Recursive;

public class Pair {

    private boolean positiveRowExist;
    private int numOfPositiveRows;

    public Pair(boolean positiveRowExist, int numOfPositiveRows) {
        this.positiveRowExist = positiveRowExist;
        this.numOfPositiveRows = numOfPositiveRows;
    }

    public boolean isPositiveRowExist() {
        return positiveRowExist;
    }

    public void setPositiveRowExist (boolean positiveRowExist) {
        this.positiveRowExist = positiveRowExist;
    }

    public int getNumOfPositiveRows () {
        return numOfPositiveRows;
    }

    public void setNumOfPositiveRows (int numOfPositiveRows) {
        this.numOfPositiveRows = numOfPositiveRows;
    }

    public String toString() {
        return "Pair [positiveRowExist = " + positiveRowExist + " ,numOfPositiveRows  = " + numOfPositiveRows + "]";
    }
}