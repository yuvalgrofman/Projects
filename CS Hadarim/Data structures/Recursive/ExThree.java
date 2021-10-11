public class ExThree {
    
    /**
     * 
     * @param string
     * @param ch
     * @return returns true is all of the characters in the string have a greater value than the char
     */
    public static boolean areAllCharsGreater(String string, char ch) {
        if (string.length() == 0) {
            return true;
        }

        return string.charAt(0) > ch && areAllCharsGreater(string.substring(1), ch);

    }
    
    /**
     * 
     * @param string
     * @param ch
     * @return returns true if at least one character in the string is greater than the char
     */
    public static boolean isOneCharGreater(String string, char ch) {
        if (string.length() == 0) {
            return false;
        }
        
        return string.charAt(0) > ch || isOneCharGreater(string.substring(1), ch);
    }
    

    /**
     * 
     * @param word
     * @return true if the string is a palindrome 
     */
    public static Boolean isPalindrome(String word) {

        
        if (word.length() <= 1) {
            return true;

        } else {
            
            return word.charAt(0) == word.charAt(word.length() - 1)
                    && isPalindrome(word.substring(1, word.length() - 1));
        }

	}
	
	
    /**
     * 
     * @param string
     * @return the inputed string with a star after every 3 chars 
     */
    public static String addStars(String string) {

        if (string.length() < 3)
            return string;

        return string.substring(0, 3) + "*" + addStars(string.substring(3));
    }

    public static void main(String[] args) {
        
       System.out.println("Testing areAllCharsGreater"); 
       System.out.println(areAllCharsGreater("", 'a')); 
       System.out.println(areAllCharsGreater("bcde", 'a')); 
       System.out.println(areAllCharsGreater("abcde", 'a')); 
       System.out.println(areAllCharsGreater("bacde", 'a')); 
       System.out.println(areAllCharsGreater("bcadae", 'a')); 
       System.out.println(areAllCharsGreater("bcdea", 'a'));
       System.out.println(""); 

       System.out.println("Testing isOneCharGreater"); 
       System.out.println(isOneCharGreater("", 'a')); 
       System.out.println(isOneCharGreater("bcde", 'a')); 
       System.out.println(isOneCharGreater("bcdea", 'a'));
       System.out.println(isOneCharGreater("bcdea", 'g'));
       System.out.println(isOneCharGreater("g", 'g'));
       System.out.println(""); 
       
       System.out.println("checking isPalindrome");
       System.out.println(isPalindrome(""));
       System.out.println(isPalindrome("baab"));
       System.out.println(isPalindrome("banana"));
       System.out.println(isPalindrome("okccko"));
       System.out.println(isPalindrome("anacna"));
       System.out.println("");

       System.out.println("checking addStars");
       System.out.println(addStars(""));
       System.out.println(addStars("baab"));
       System.out.println(addStars("banana"));
       System.out.println(addStars("okccko"));
       System.out.println(addStars("anacna"));
       System.out.println(addStars("anacnae"));
       System.out.println("");
       

    }
    
}
