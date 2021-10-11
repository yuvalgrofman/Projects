public class Recursive
{
	
	public static int factorial(int N){
			
		if (N == 1){
			return 1;
			
		}else{
			return N * factorial(N - 1);
		}
		
	}
	
	public static int power(int base, int power){
		
		if (power == 0){
			return 1;
		
		}else{
			
			return base * power(base, power - 1);
		}
	}
	
	public static void leftToRight(int num){
		
		if (num < 10){
			System.out.println(num);
		
		}else{
			leftToRight(num/10);
			System.out.println(num % 10);
		}
	}
	
	public static void rightToLeft(int num) {

		if (num < 10) {
			System.out.println(num);

		} else {
			System.out.println(num % 10);
			rightToLeft(num / 10);
		}
	}

	public static Boolean doDigitsDivide3(int num){
		
		if (num < 10){
			return num % 3 == 0;
		
		}else{
			
			int lastDigit = num%10;
			
			return (lastDigit % 3 == 0 && doDigitsDivide3(num/10));
				
		}
	}
		
	public static Boolean isPalindrome(String word){
		if (word.length() == 0)
			return true;
		return isPalindromeRecursive(word, 0);
	}
	
	
	public static Boolean isPalindromeRecursive(String word, int index){
			
		if (index > (word.length() / 2)){
			return true;
		
		}else {
			
			return (word.charAt(index) == word.charAt(word.length() - index - 1) && isPalindromeRecursive(word, index + 1));
		}
	}
	
	
	public static void main(String[] args)
	{
		//checking factorial
		System.out.println("checking factorial");
		System.out.println(factorial(1));
		System.out.println(factorial(3)); 
		System.out.println(factorial(5)); 
		
		//checking power
		System.out.println("checking power");
		System.out.println(power(1,0));
		System.out.println(power(1,1));
		System.out.println(power(2,3)); 
		System.out.println(power(5,3));
		
		//checking leftToRight
		System.out.println("checking LTR");
		leftToRight(1);
		leftToRight(123);
		leftToRight(15657);
		
		//checking leftToRight
		System.out.println("checking RTL");
		rightToLeft(1);
		rightToLeft(123);
		rightToLeft(15657);

		
		//checking do digitsDivide3
		System.out.println("checking do digitsDivide3");
		System.out.println(doDigitsDivide3(0));
		System.out.println(doDigitsDivide3(3));
		System.out.println(doDigitsDivide3(1));
		System.out.println(doDigitsDivide3(369));
		System.out.println(doDigitsDivide3(359));
		
		//checking isPalindrome
		System.out.println("checking isPalindrome");
		System.out.println(isPalindrome(""));
		System.out.println(isPalindrome("baab"));
		System.out.println(isPalindrome("banana"));
		System.out.println(isPalindrome("okccko"));
		System.out.println(isPalindrome("anacna"));
		
		
	}
}
