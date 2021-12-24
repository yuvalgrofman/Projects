package linkedList;

public class Point {

	private int xPos; // the x position of the point
	private int yPos; // the y position of the point
	
	public Point(int xPos, int yPos) {
		this.xPos = xPos;
		this.yPos = yPos;
	}

	public int getxPos() {
		return xPos;
	}

	public void setxPos(int xPos) {
		this.xPos = xPos;
	}

	public int getyPos() {
		return yPos;
	}

	public void setyPos(int yPos) {
		this.yPos = yPos;
	}


	public String toString() {
		return "Point [xPos=" + xPos + ", yPos=" + yPos + "]";
	}
	
	
	
}
