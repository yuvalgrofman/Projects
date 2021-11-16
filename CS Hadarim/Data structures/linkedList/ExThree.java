package linkedList;

public class ExThree {
    
    public static <T> Node<T> addFirst(Node<T> node, T val) {
        Node<T> first = new Node<T>(val, node); 
        return first;
    }

    public static <T> void  addLast(Node<T> node, T val){
        while (node.getNext() != null) {
            node = node.getNext();
        }

        node.setNext(new Node<T>(val));
    }

    public static <T> void add(Node<T> node, int index, T val){

        if (index == 0) {
            addFirst(node, val);
            return;
        }

        for (int count = 0; count < index - 1; count++) {
            node = node.getNext(); 
        }

        Node<T> newNode = new Node<T>(val, node.getNext()); 
        node.setNext(newNode);
    }

    public static <T> Node<T> addAll(Node<T> node, T val) {
        Node<T> first = new Node<T>(val, node); 
        
        for (int i = 1; i < ExTwo.length(node); i += 2){
            add(node, i, val);
        }
        
        return first;
    }

    public static void main(String[] args) {
        
        Node<Integer> n4 = new Node<Integer>(4);
        Node<Integer> n3 = new Node<Integer>(3, n4);
        Node<Integer> n2 = new Node<Integer>(2, n3);
        Node<Integer> n1 = new Node<Integer>(1, n2);

        
        ExOne.print(n1);
        Node<Integer> n0 = addFirst(n1, 0);
        ExOne.print(n0);

        addLast(n0, 6);
        ExOne.print(n0);

        addLast(n0, 7);
        ExOne.print(n0);

        add(n0, 5, 5);
        ExOne.print(n0);

        Node<Integer> first = addAll(n0, 10);

        ExOne.print(first);
        

    }
}
