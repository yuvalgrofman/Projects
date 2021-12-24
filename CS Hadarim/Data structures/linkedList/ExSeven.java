package linkedList;

public class ExSeven {


    /**
     * 
     * @param <T> the type of the nodes
     * @param node1 first node in first linked list
     * @param node2 first node in second linked list 
     * @return if one list is subList of the other list 
     * O(n) + O(n) = O(n)
     * where n is the length of the longer list 
     */
    public static <T> boolean isListInlist(Node<T> node1, Node<T> node2) {

        return isSubList(node1, node2) || isSubList(node2, node1);
    }

    /**
     * 
     * @param <T> the type of the nodes
     * @param node1 first node in one linked list 
     * @param node2 first node in second linked list
     * @return if first linked list is subList of list 2
     * O(m+n)=O(2n)=O(n)
     * where n is the length of the longer list and m is the length of the shorter one 
     */
    public static <T> boolean isSubList(Node<T> node1, Node<T> node2){

        while (node1 != null) {

            if (node2 == null)
                return false; 
            
            while (node2 != null) {
                
                if (node1.getValue() == node2.getValue()){
                    node2 = node2.getNext();
                    break;
                }

                node2 = node2.getNext();
            }

            node1 = node1.getNext();
        }

        return true;
    }

    /**
     * 
     * @param node first node in linked list of chars
     * @param c1 arbitrary char
     * @param c2 arbitrary char
     * prints all of the subseries that start with c1 and end with c2
     */
    public static void printAllSubLists(Node<Character> node, char c1, char c2) {

        Node<Character> first = node; 

        while (node != null) {

            Node<Character> node2 = node; 
            
            while (node2 != null) {
                
                if (node.getValue() == c1 && node2.getValue() == c2)
                    printBetweenNodes(node, node2);
                
                node2 = node2.getNext();
            }

            node = node.getNext();
        }
    }

    /**
     * 
     * @param node1 a node in linked list of chars
     * @param node2 another node in linked list of chars
     * assumes that node2 is on the linked list at or after node1's spot
     * and prints all the values of the nodes in between including node1 and node2
     * O(n) when n is distance between nodes
     */
    public static void printBetweenNodes(Node<Character> node1, Node<Character> node2) {
        
        while (node1 != node2) {
            System.out.print(node1.getValue());
            node1 = node1.getNext();
        }

        System.out.println(node2.getValue());
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

        Node<Integer> e5 = new Node<Integer>(3);
        Node<Integer> e4 = new Node<Integer>(1, e5);
        Node<Integer> e3 = new Node<Integer>(1, e4);
        Node<Integer> e2 = new Node<Integer>(2, e3);
        Node<Integer> e1 = new Node<Integer>(1, e2);

        System.out.println(isListInlist(e1, n1));
        System.out.println(isListInlist(e4, n1));
        System.out.println(isListInlist(n3, n1));
        System.out.println(isListInlist(e3, e1));

        Node<Character> k5 = new Node<Character>('1');
        Node<Character> k4 = new Node<Character>('3', k5);
        Node<Character> k3 = new Node<Character>('1', k4);
        Node<Character> k2 = new Node<Character>('2', k3);
        Node<Character> k1 = new Node<Character>('1', k2);

        printAllSubLists(k1, '1', '1');

        Node<Character> f10 = new Node<Character>('w');
        Node<Character> f9 = new Node<Character>('y', f10);
        Node<Character> f8 = new Node<Character>('a', f9);
        Node<Character> f7 = new Node<Character>('a', f8);
        Node<Character> f6 = new Node<Character>('t', f7);
        Node<Character> f5 = new Node<Character>('t', f6);
        Node<Character> f4 = new Node<Character>('a', f5);
        Node<Character> f3 = new Node<Character>('z', f4);
        Node<Character> f2 = new Node<Character>('d', f3);
        Node<Character> f1 = new Node<Character>('a', f2);

        printAllSubLists(f1, 'a', 'a');
    }

}
