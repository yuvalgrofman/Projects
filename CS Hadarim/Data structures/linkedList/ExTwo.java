package linkedList;

public class ExTwo {

    /**
     * 
     * @param <T> type of nodes
     * @param curr first node in the linked lust
     * @param val the value to check
     * @return true if their exists a node with the value val
     */
    public static <T> boolean  isInList(Node<T> curr, T val){

        while (curr != null) {
            if (curr.getValue().equals(val))
                return true;

            curr = curr.getNext();
        }

        return false;
    }

    /**
     * @param <T> a type of nodes
     * @param curr the first node in the linked list
     * @return the length of the list
     */
    public static <T> int length(Node<T> curr) {
        int length = 0;
        
        while (curr != null) {

            curr = curr.getNext(); 
            length++;
        }

        return length;
    }

    /**
     * 
     * @param <T> the type of the nodes
     * @param curr the first node on the list
     * @param val the value you want to count
     * @return the amount of nodes in the lust which have the value val
     */
    public static <T> int countVal(Node<T> curr, T val) {
        int count = 0;

        while (curr != null) {
            if (curr.getValue().equals(val))
                count++;

            curr = curr.getNext();
        }

        return count;
    }

    /**
     * 
     * @param node the first node in a char array
     * @return the node with the char with the minimum value
     */
    public static Node<Character> min(Node<Character> node) {
        Node<Character> min = node; 

        while (node != null) {
            
            if (node.getValue().compareTo(min.getValue()) < 0)
                min = node;

            node = node.getNext();
        }

        return min;
    } 


    public static void main(String[] args) {

        Node<Character> n5 = new Node<Character>('a');
        Node<Character> n4 = new Node<Character>('d',n5);
        Node<Character> n3 = new Node<Character>('c',n4);
        Node<Character> n2 = new Node<Character>('b',n3);
        Node<Character> n1 = new Node<Character>('a',n2);

        System.out.println(isInList(n1, 'c'));
        System.out.println(isInList(n1, 'e'));

        System.out.println(length(n1));
        System.out.println(length(n3));

        System.out.println(countVal(n1, 'a'));
        System.out.println(countVal(n1, 'b'));

        System.out.println(min(n1));
        System.out.println(min(n3));
        
        
    }
}
