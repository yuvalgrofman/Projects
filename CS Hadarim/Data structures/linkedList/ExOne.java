package linkedList;

import java.util.Scanner;


public class ExOne{


    public static <T> void print(Node<T> node) {

        while (node.getNext() != null) {
            
            System.out.print(node + " ");
            node = node.getNext(); 

        }

        System.out.println(node);
    }

    public static <T> boolean isInList(Node<T> node, T val) {

        while (node != null) {
            
            if (val.equals(node.getValue()))
                return true;

            node = node.getNext(); 

        }

        return false;
    }

    public static Node<Integer> createList(){
        Scanner s = new Scanner(System.in);

       System.out.println("Do you want to stop? (Y/N)"); 
       
        if (s.next().equals("Y"))
           return null;

        System.out.println("Write next value");
        int input = s.nextInt();

        Node<Integer> first = new Node<Integer>(input, null); 
        Node<Integer> curr = first; 
        Node<Integer> bef = first;

        while (true) {
           System.out.println("Do you want to stop? (Y/N)"); 

           if (s.next().equals("Y"))
               return first;

            System.out.println("Write next value");
            input = s.nextInt();

            curr = new Node<Integer>(input, null);
            
            bef.setNext(curr);

            bef = curr;
        }
    }


    public static void main(String[] args) {
        
        Node<Integer> first = createList();
        print(first);
    }

}