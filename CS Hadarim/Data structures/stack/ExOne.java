package stack;

public class ExOne {
    
    /**
     * 
     * @param <T>
     * @param stack
     * @param val
     * @return return if val is in stack
     * keeps stack the same
     */
    public static <T> boolean isIn(Stack<T> stack, T val) {

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
     * @param <T> type T
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
     * @param <T> type T
     * @param stack arbitrary stack
     * @param val arbitrary value T 
     * @return return if val is in stack
     * keeps stack the same
     */
    public static <T> int countVal(Stack<T> stack, T val) {

        Stack<T> copyStack = new Stack<T>();
        int count = 0;

        while (!stack.isEmpty()) {

            copyStack.push(stack.pop());

            if (copyStack.top().equals(val)) {
                count++;
            }

        }

        moveStack(stack, copyStack);

        return count;
    }

    /**
     * 
     * @param <T> type T
     * @param stack arbitrary stack
     * @param n int 
     * @return Nth element in stack and keeps stack the same
     */
    public static <T> T getNthElement(Stack<T> stack, int n) {

        T val;
        Stack<T> copy = new Stack<T>();
        
        for (int i = 0; i < n; i++) {
            copy.push(stack.pop());
        }

        val = copy.top();

        moveStack(stack, copy);

        return val;
    }

    /**
     * 
     * @param <T> type T
     * @param stack arbitrary stack
     * @return a copy stack with the same elements (doesn't ruin original stack) 
     */
    public static <T> Stack<T> copy(Stack<T> stack){

        Stack<T> reverse = new Stack<T>();
        Stack<T> copy = new Stack<T>();

        moveStack(reverse, stack);

        while (!reverse.isEmpty()){
            stack.push(reverse.pop());
            copy.push(stack.top());
        }

        return copy;
    }

    /**
     * 
     * @param <T> type T
     * @param stack arbitrary stack
     * @return a reverse stack with the same elements in reverse order(doesn't ruin original stack) 
     */
    public static <T> Stack<T> reverse(Stack<T> stack) {
        
        Stack<T> reverse = new Stack<T>();
        Stack<T> copy = copy(stack);

        moveStack(reverse, copy);
        return reverse;
    }

    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<Integer>();
        Use.receiveInput(stack);

        System.out.println(stack);
        System.out.println((isIn(stack, 5)));
        System.out.println(stack);
        System.out.println(countVal(stack, 5));
        System.out.println(stack);
        System.out.println(getNthElement(stack, 3));
        System.out.println(stack);
        
        Stack<Integer> copy = new Stack<Integer>();
        Stack<Integer> reverse = new Stack<Integer>();

        copy = copy(stack);
        System.out.println(stack);
        System.out.println(copy);
        reverse = reverse(stack);
        System.out.println(stack);
        System.out.println(reverse);
    }

}