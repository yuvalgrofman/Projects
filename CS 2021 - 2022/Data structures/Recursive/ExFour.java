package Recursive;

import java.util.Random;

public class ExFour {
    
    /**
     * 
     * @param num
     * prints in every row the amount of stars of the corresponding digit in the number
     */
    public static void printStars(int num) {

        if (num < 10) {
            for (int i = 0; i < num; i++) {
                System.out.print("*");
            }
            System.out.println("");

        } else {
            printStars(num / 10);

            for (int i = 0; i < num % 10; i++) {
                System.out.print("*");
            }
            System.out.println("");

        }
    }

    /**
     * 
     * @param num
     * prints in every row the amount of stars of the corresponding digit in the number
     */
    public static void printStarsNoLoop(int num) {

        if (num < 10) {
            System.out.println("*".repeat(num));

        } else {
            printStars(num / 10);
            System.out.println("*".repeat(num % 10));

        }
    }

    /**
     * 
     * @param string
     * @return the amount of times the string "abc" appears in the input string
     */
    public static int countABC(String string) {

        if (string.length() <= 3) {

            if (string.equals("abc")) {
                return 1;
            }

            return 0;
        }

        if (string.substring(0, 3).equals("abc") ) {
            return countABC(string.substring(1)) + 1;
        }

        return countABC(string.substring(1));
    }

    /**
     * 
     * @param string
     * @return the string with up to 5 random characters in the string turned into starts ie: "*"
     */
    public static String randomStars(String string) {

        if (string.equals("")) {
            return "";
        }
        Random random = new Random();

        for (int i = 0; i < 5; i++) {
            int index = random.nextInt(string.length());

            string = string.substring(0, index) + "*" + string.substring(index + 1);
        }

        return string;
    }

    /**
     * 
     * @param string
     * @return the string with up to 5 random characters in the string turned into starts ie: "*"
     */
    public static String randomStarsRecursive(String string) {
        return randomStarsRecursiveStep(string, 0);
    }

    /**
     * 
     * @param string
     * @param count
     * this function is the recursive step of the program it modifies the count and one character in the string and then calls the 
     * function again. 
     * if the count is 5 it ends the recursion. 
     */
    private static String randomStarsRecursiveStep(String string, int count) {

        if (count == 5) {
            return string;
        
        } else {

            if (string.equals(""))
                return "";
            
            Random random = new Random();

            int index = random.nextInt(string.length());
            string = string.substring(0, index) + "*" + string.substring(index + 1);

            return randomStarsRecursiveStep(string, count + 1);
        }
    }


    public static void main(String[] args) {
        System.out.println("Testing printStars");
        printStars(3702);
        System.out.println("------");
        printStars(02);
        System.out.println("------");
        printStars(2);
        System.out.println("------");
        printStars(15);
        System.out.println("------");
        printStars(10001);
        System.out.println("------");
        printStars(0);
        System.out.println("------");
        printStars(1);
        System.out.println("------");

        System.out.println("Testing printStarsNoLoop");
        printStarsNoLoop(3702);
        System.out.println("------");
        printStarsNoLoop(02);
        System.out.println("------");
        printStarsNoLoop(2);
        System.out.println("------");
        printStarsNoLoop(15);
        System.out.println("------");
        printStarsNoLoop(10001);
        System.out.println("------");
        printStarsNoLoop(0);
        System.out.println("------");
        printStarsNoLoop(1);
        System.out.println("------");

        System.out.println("Testing countABC");
        System.out.println(countABC("abc"));
        System.out.println(countABC("ab"));
        System.out.println(countABC("a"));
        System.out.println(countABC(""));
        System.out.println(countABC("abcabc"));
        System.out.println(countABC("abccba"));

        System.out.println("Testing randomStars");
        System.out.println(randomStars("abc"));
        System.out.println(randomStars("abc"));
        System.out.println(randomStars("ab"));
        System.out.println(randomStars("a"));
        System.out.println(randomStars(""));
        System.out.println(randomStars("abcabc"));
        System.out.println(randomStars("abccba"));

        System.out.println("Testing randomStars");
        System.out.println(randomStarsRecursive("abc"));
        System.out.println(randomStarsRecursive("abc"));
        System.out.println(randomStarsRecursive("ab"));
        System.out.println(randomStarsRecursive("a"));
        System.out.println(randomStarsRecursive(""));
        System.out.println(randomStarsRecursive("abcabc"));
        System.out.println(randomStarsRecursive("abccba"));

    }
}
