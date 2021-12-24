package linkedList;

public class ExEight {

    /**
     * 
     * @param <T> type
     * @param node first node in linked list
     * @param val value of type T
     * @return the amount of nodes in list with value val 
     * if n is the length of the linked list
     * O(n) - because the function iterates over every node in the list exactly once 
     */
    public static <T> int countVal(Node<T> node, T val) {
        
        if (node == null)
            return 0;

        if (node.getValue() == val)
            return 1 + countVal(node.getNext(), val);

        return countVal(node.getNext(), val);
    }

    /**
     * 
     * @param <T> type T
     * @param node first node in linked list
     * @param val value of type T
     * @return true only if their is a node with value val
     */
    public static <T> boolean isInList(Node<T> node, T val){

        if (node == null)
            return false;

        return node.getValue().equals(val) || isInList(node.getNext(), val);
    }


    /**
     * 
     * @param <T> type T
     * @param node first node in linked list
     * @param index index in linked list 
     * @return the node in position index 
     */
    public static <T> Node<T> getInPos(Node<T> node, int index){
        return getInPosStep(node, 0, index);

    }

    /**
     * 
     * @param <T> type T 
     * @param node first Node in linked list
     * @param pos int which represents position of node
     * @param index the index of the node to return 
     * @return node in position index
     */
    public static <T> Node<T> getInPosStep(Node<T> node, int pos, int index){

        if (node == null)
            return null;

        if (index == pos)
            return node;

        return getInPosStep(node.getNext(), pos + 1, index);
    }

    public static void main(String[] args) {

        Node<Integer> n8 = new Node<Integer>(3);
        Node<Integer> n7 = new Node<Integer>(7, n8);
        Node<Integer> n6 = new Node<Integer>(4, n7);
        Node<Integer> n5 = new Node<Integer>(5, n6);
        Node<Integer> n4 = new Node<Integer>(4, n5);
        Node<Integer> n3 = new Node<Integer>(3, n4);
        Node<Integer> n2 = new Node<Integer>(2, n3);
        Node<Integer> n1 = new Node<Integer>(1, n2);

        System.out.println(countVal(n1, 4));        
        System.out.println(countVal(n1, 3));        
        System.out.println(countVal(n1, 5));        

        System.out.println(isInList(n1, 6));
        System.out.println(isInList(n1, 3));
        System.out.println(isInList(n1, 8));

        System.out.println(getInPos(n1, 4));
        System.out.println(getInPos(n1, 5));
        System.out.println(getInPos(n1, 6));
    }

}
