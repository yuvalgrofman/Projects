package linkedList;

import java.util.Scanner;
import java.util.function.Function;

public class ExFive {
    
    /**
     * 
     * @param <T> the type of nodes
     * @param node the first nin linked list
     * prints the values if elements in the array in reversed order
     */
    public static <T> void printReverse(Node<T> node) {
        Node<T> first = node; 

        for (int i = ExTwo.length(node); i >= 0; i--) {
            node = first; 

            for (int j = 1; j < i; j++) {

                node = node.getNext();
                
            }

            System.out.println(node);
        }
    }

    /**
     * 
     * @param node the first nin linked list
     * prints the number of times each value appears in the list without repetition 
     */
    public static <T> void printCountPerVal(Node<T> node) {
        
        Node<T> first = node; 
        int len = ExTwo.length(node);
        
        for (int i = 0; i < len; i++) {

            node = first;
            
            int j = 0;
            while (j < i){
                node = node.getNext();
                j++;
            }

            T val = node.getValue(); 

            node = first;
            Boolean appearsBeforePlaceJ = false;
            
            j = 0;
            while (j < i - 1){

                if (node.getValue() == val) {
                    appearsBeforePlaceJ = true; 
                }

                node = node.getNext();
                j++;
            }

            if (appearsBeforePlaceJ)
                continue;

            System.out.println(("Value " + val + " appears " + countVal(first, val) + " times"));
        }
    }

    /**
     * 
     * @param <T> the type of the nodes
     * @param node the first node in the list
     * @param val a value of type T
     * @return the amount of times the value val appears
     */
    public static <T> int countVal(Node<T> node, T val) {
        
        int count = 0;

        while (node != null) {
            
            if (node.getValue() == val)
                count++;

            node = node.getNext();
        }

        return count; 
    }

    /**
     *  receives chars from the user  
     * @return the first node in a list the is sorted vy the chars
     */
    public static  Node<Character> createSortedCharList(){

        Scanner s = new Scanner(System.in); 
        Character input; 

        input = s.nextLine().charAt(0);

        if (input == '*')
            return null; 

        Node<Character> first = new Node<Character>(input);

        while (input != '*'){

            input = s.nextLine().charAt(0);

            if (input == '*')
                break;

            if (input < first.getValue())
                first = new Node<Character>(input, first);
            
            else {

                Node<Character> node = first; 
                boolean addedChar = false;

                while (node != null && node.getValue() < input && !addedChar) {

                    if (node.getNext() == null) {
                        node.setNext(new Node<Character>(input));
                        addedChar = true;

                    }else if (input <= node.getNext().getValue()) {
                        node.setNext(new Node<Character>(input, node.getNext()));
                        addedChar = true;

                    } else {
                        node = node.getNext();

                    }
                }
            }
        }
        return first;
    }

    public static void main(String[] args) {
        
        Node<Integer> n8 = new Node<Integer>(8);
        Node<Integer> n7 = new Node<Integer>(7, n8);
        Node<Integer> n6 = new Node<Integer>(6, n7);
        Node<Integer> n5 = new Node<Integer>(5, n6);
        Node<Integer> n4 = new Node<Integer>(4, n5);
        Node<Integer> n3 = new Node<Integer>(3, n4);
        Node<Integer> n2 = new Node<Integer>(2, n3);
        Node<Integer> n1 = new Node<Integer>(1, n2);

        printReverse(n1);
        printCountPerVal(n1);

        n5.setValue(1);

        printReverse(n1);
        printCountPerVal(n1);

        Node<Character> e1 = createSortedCharList();
        ExOne.print(e1);
    }

}