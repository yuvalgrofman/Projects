package linkedList;

import java.util.Random;

public class ExSix {

    /**
     * 
     * @param node first node in linked list of Points
     * @return the Point in the Node array with the greatest y
     */
    public static Point maxY(Node<Point> node) {

        Point maxPoint = new Point(0, Integer.MIN_VALUE); 

        while (node != null){

            if (node.getValue().getyPos() >= maxPoint.getyPos()) {
                maxPoint = node.getValue();
            }

            node = node.getNext();
        }

        return maxPoint;
    }

    /**
     * 
     * @param len integer of list to be created
     * @return creates a linked list of integers between -10 and 10 of size len and returns the first element
     */
    public static Node<Point> createPointList(int len){
        Random r = new Random();

        Node<Point> first = new Node<Point>(new Point(r.nextInt(20) - 10, r.nextInt(20) - 10));
        Node<Point> node = first; 

        for (int i = 0; i < len; i++) {

            node.setNext(new Node<Point>(new Point(r.nextInt(20) - 10, r.nextInt(20) - 10)));
            node = node.getNext();
        }

        return first; 
    }

    /**
     *  
     * @param pointNode first node in linked list of points 
     * @return the first node in a linked list of integers which are the x of the points 
     */
    public static Node<Integer> getXVals(Node<Point> pointNode) {

        Node<Integer> first = new Node<Integer>(pointNode.getValue().getxPos());
        Node<Integer> node = first; 

        while (pointNode.getNext() != null) {

            node.setNext(new Node<Integer>(pointNode.getNext().getValue().getxPos()));
            node = node.getNext();            
            pointNode = pointNode.getNext();
        }

        return first; 
    }

    /**
     * 
     * @param node1 linked list of Ints
     * @param node2 Linked list of Ints
     * @return linked list of intersection without repetition
     */
    public static Node<Integer> sameVals(Node<Integer> node1, Node<Integer> node2) {
        
        Node<Integer> first1 = node1;
        Node<Integer> first2 = node2;

        Node<Integer> first = null; 
        Node<Integer> node = null;

        boolean addedFirst = false;
        
        while (node1 != null) {
            int valueToAdd = node1.getValue();
            node2 = first2;

            while (node2 != null) {

                if (node2.getValue() == valueToAdd) {
                    
                    if (!appearsInList(first, valueToAdd)) {

                        if (node == null) {
                            first = new Node<Integer>(valueToAdd);
                            node = first; 

                        } else {
                            node.setNext(new Node<Integer>(valueToAdd));
                            node = node.getNext();

                        }
                    }
                }

                node2 = node2.getNext();
            }

            node1 = node1.getNext();
        }
            
        if (first == null)
            return null;

        return first;
        
    }

    /**
     * 
     * @param node first element of linked list if ints
     * @param n number to check
     * @return true if there is a node with value n
     */
    public static boolean appearsInList(Node<Integer> node, int n){

        while (node != null) {

            if (node.getValue() == n)
                return true;

            node = node.getNext();
        }


        return false;
    }

    public static void main(String[] args) {
        Node<Point> nodeList1 = createPointList(10);
        Node<Point> nodeList2 = createPointList(10);


        System.out.println("node list 1");
        System.out.println();
        ExOne.print(nodeList1);

        System.out.println("node list 2");
        System.out.println();
        ExOne.print(nodeList2);

        Point max1 = maxY(nodeList1);
        System.out.println("print max y point list 1 " + max1.getyPos());
        
        Point max2 = maxY(nodeList2);
        System.out.println("print max y point list 2 " + max2.getyPos());

        System.out.println("x val 1");
        Node<Integer> xVals1 = getXVals(nodeList1);
        ExOne.print(xVals1);
        System.out.println("x val 2");
        Node<Integer> xVals2 = getXVals(nodeList2);
        ExOne.print(xVals2);


        System.out.println("print intersect between x val");
        Node<Integer> intersect = sameVals(xVals1, xVals2);

        if (intersect != null)
            ExOne.print(intersect);



    }

}
