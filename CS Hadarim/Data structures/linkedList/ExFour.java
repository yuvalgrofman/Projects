package linkedList;

import javax.print.event.PrintEvent;

public class ExFour {

    public static <T> Node<T> removeFirst(Node<T> node){

        Node<T> newFirst = node.getNext(); 
        node.setNext(null);

        return newFirst;
    } 

    public static <T> void removeLast(Node<T> node) {
        
        while (node.getNext().getNext() != null) {
            node = node.getNext();
        }

        node.setNext(null);
    }

    public static <T> Node<T> remove(Node<T> node, T val) {
        Node<T> first = node;

        if (node.getValue().equals(val))
            first = node.getNext();

        while (node.getNext() != null) {


            if (node.getNext().getValue().equals(val)){

                Node<T> toRem = node.getNext();
                node.setNext(toRem.getNext());
                toRem.setNext(null);

            }

            node = node.getNext();

            if (node == null)
                return first;
        }

        return first;
    }

    public static <T> Node<T> removeEvenPos(Node<T> node) {

        Node<T> first = removeFirst(node);
        Node<T> curr = first; 

        while (curr.getNext() != null){

            Node<T> toRem = curr.getNext();
            curr.setNext(toRem.getNext());
            toRem.setNext(null);

            curr = curr.getNext();

            if (curr == null)
                return first;
        }
        
        return first;
    }

    public static <T> Node<T> remove(Node<T> node, int index) {

        if (index == 0)
            return removeFirst(node);

        Node<T> first = node;
        
        for (int i = 0; i < index - 1; i++) {
            node = node.getNext();
        }

        Node<T> toRem = node.getNext(); 
        node.setNext(toRem.getNext());
        toRem.setNext(null);

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

        removeLast(n1);
        ExOne.print(n1);

        Node<Integer> newFirst = removeFirst(n1);
        ExOne.print(newFirst);

        remove(newFirst, 2);
        ExOne.print(newFirst);

        newFirst = removeEvenPos(newFirst);
        ExOne.print(newFirst);

        Node<String> e5 = new Node<String>("1");
        Node<String> e4 = new Node<String>("3", e5);
        Node<String> e3 = new Node<String>("1", e4);
        Node<String> e2 = new Node<String>("2", e3);
        Node<String> e1 = new Node<String>("1", e2);

        Node<String> e0 = remove(e1, "1");
        ExOne.print(e0);
    }
    

}
