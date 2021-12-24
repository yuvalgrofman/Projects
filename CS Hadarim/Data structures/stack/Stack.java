package stack;

import linkedList.Node;

public class Stack <T>
{
	private Node<T> first;

	public Stack ()
	{
		this.first=null;
	}

	// returns true if the structure is empty, otherwise, returns false
	public boolean isEmpty()
	{
		return this.first==null;
	}

	// receives a value and insert it into the structure

	public void push(T x)
	{
		this.first=new Node<T>(x, this.first);
	}

	// removes the firest value from the structure.
// returns the value that was removed 

	public T pop()
	{
		T x=this.first.getValue();
		this.first=this.first.getNext();
		return x;
	}

// returns the first value from the structure, without removing it

	public T top()
	{
		return  this.first.getValue();
	}

	// returns a String containing all the values in the structure 
	// according to their removal order	
	public String toString()
    {
        String str = "[";
        Node<T> pos = this.first;
        while (pos != null) {
            str = str + pos.getValue().toString();
            if (pos.getNext() != null)
                str = str + " , ";
            pos = pos.getNext();
        }

        str = str + "]";
        return str;
    }
}