package Recursive;

public class ExSix {

    /**
     * 
     * @param arr array
     * @param pos int
     * @return true if all elements of the array from 0 to position pos are positive 
     */
    public static boolean inRangePositive(int[] arr, int pos){

        if (pos < 0) 
            return true;

        else {

            return arr[pos] > 0 && inRangePositive(arr, pos - 1);
        }

    }

    /**
     * 
     * @param arr array
     * @param rowNum int 
     * @return A complex structure names Pair which has a boolean and int
     * the boolean is true if there is a row that all of the numbers are positive 
     *the int is the number of rows that all of the numbers are positive
     */
    public static Pair rowsIn2DArray(int[][] arr, int rowNum) {
        
        if (rowNum < 0)
            return new Pair(false, 0); 

        else {

            Pair miniPair = rowsIn2DArray(arr, rowNum - 1);

            if (inRangePositive(arr[rowNum], arr[rowNum].length - 1))
                return new Pair(true, 1 + miniPair.getNumOfPositiveRows());

            else {
                 
                return new Pair(miniPair.isPositiveRowExist(), miniPair.getNumOfPositiveRows());
            }
        }
    }

    /**
     * 
     * @param arr
     * @return the largest number in a 2d array 
     *if the array is empty returns Integer.MIN_VALUE
     */
    public static int maxNumIn2dArray(int[][] arr) {
        if (arr.length == 0 || arr[0].length == 0)
            return Integer.MIN_VALUE;

        return maxNum(arr, arr.length - 1);
    }

    /**
     *
     * @param arr array
     *@param pos integer
     * @return the largest number in the 2d array from the column up to column number pos 
     */
    public static int maxNum(int[][] arr, int pos){

        if (pos == 0)
            return maxInRow(arr[0], arr[0].length - 1);

        else {
            return Math.max(maxInRow(arr[pos], arr[pos].length - 1), maxNum(arr, pos - 1));
        }
    }

    /**
     * 
     * @param arr array
     * @param pos int
     * @return the largest number in the array up to position pos
     */
    public static int maxInRow(int[] arr, int pos) {

        if (pos == 0)
            return arr[0];
        
        else {
                
            return Math.max(arr[pos], maxInRow(arr, pos - 1));
        }
    }

    public static void main(String[] args) {
        int[] arr = { 1, 2, - 1, 2};
        System.out.println(inRangePositive(arr, 1));
        System.out.println(inRangePositive(arr, 2));
        System.out.println(inRangePositive(arr, 3));

        int[][] arr2D = { { 1, 3, 1, 2 }, { 1, 2, 1, 2 }, { 1, 2, -1, 2 }, };
        int[][] arr2DTwo = { { 1, 2, -1, 2 }, { 1, 2, -1, 2 }, { 1, 4, -1, 2 }, };
        int[][] arr2DThree = { { } };
        int[][] arrMaxOne = { {1}, {2}, {-1} };

        System.out.println(rowsIn2DArray(arr2D, 0));
        System.out.println(rowsIn2DArray(arr2D, 1));
        System.out.println(rowsIn2DArray(arr2D, 2));
        System.out.println(rowsIn2DArray(arr2DTwo, 2));
        System.out.println(rowsIn2DArray(arr2DThree, 0));

        System.out.println(maxNumIn2dArray(arr2D));
        System.out.println(maxNumIn2dArray(arr2DTwo));
        System.out.println(maxNumIn2dArray(arr2DThree));
        System.out.println(maxNumIn2dArray(arrMaxOne));

    }
    
    
}
