package stack;

import java.util.Scanner;

public class Use {

    /**
     * 
     * @param stack
     * receives stack and input from user and puts input in stack 
     */
    public static void receiveInput(Stack<Integer> stack) {

        Scanner s = new Scanner(System.in);
        int input = 0;

        while (input != -999){

            System.out.println("Enter Number:");
            input = s.nextInt();
            
            if (input != -999)
                stack.push(input);
        } 
    } 

    /**
     * 
     * @param <T>
     * @param stackToAdd 
     * @param stackToMove
     * moves stackToMove into stackToAdd
     */
    public static <T> void moveStack(Stack<T> stackToAdd, Stack<T> stackToMove) {
        
        while (!stackToMove.isEmpty()) {

            stackToAdd.push(stackToMove.pop());
        }
    }

    /**
     * 
     * @param <T>
     * @param stack
     * @param val
     * @return if val is in stack
     * deletes elements up to stack
     */
    public static <T> boolean isIn(Stack<T> stack, T val) {
        
        while (!stack.isEmpty()) {

            if (stack.pop().equals(val))
                return true;
        }

        return false;
    } 

    /**
     * 
     * @param <T>
     * @param stack
     * @param val
     * @return return if val is in stack
     * keeps stack the same
     */
    public static <T> boolean fixedIsIn(Stack<T> stack, T val) {

        Stack<T> copyStack = new Stack<T>();

        while (!stack.isEmpty()) {

            copyStack.push(stack.pop());

            if (copyStack.top().equals(val)) {
                
                moveStack(stack, copyStack);                

                return true;
            }

        }

        moveStack(stack, copyStack);

        return false;
    }

    /**
     * 
     * @param <T>
     * @param stack
     * @return returns stack in reversed order
     */
    public static <T> Stack<T> reverseStack(Stack<T> stack) {

        Stack<T> reverseStack = new Stack<T>();
        Stack<T> copy = new Stack<T>();

        while (!stack.isEmpty()) {
            reverseStack.push(stack.pop());
            copy.push(reverseStack.top());
        }

        moveStack(stack, copy);

        return reverseStack;
    }

    public static void main(String[] args) {

        Stack<Integer> stack = new Stack<>();
        receiveInput(stack);

        System.out.println(stack);
        System.out.println(fixedIsIn(stack, 5));
        System.out.println(stack);

        System.out.println(stack);
        Stack<Integer> reverseStack = reverseStack(stack);
        System.out.println(stack);
        System.out.println(reverseStack);


    }
}
