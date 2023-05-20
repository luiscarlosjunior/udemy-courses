
public class BinarySearch {
	
	public static int search(int[] array, int target) {
		int lo = 0;
		int hi = array.length - 1;
		
		while(lo <= hi) {
			int mid = (lo + hi) / 2;
			if(target > array[mid]) {
				lo = mid + 1;
			} else if (target < array[mid]) {
				hi = mid + 1;
			} else {
				return mid;
			}
		}
		return -1;		
	}
	
	public static void main(String args[])
	{
		int[] array = {1,2,3,4,5,6,7,8,9};
		int index = search(array, 9);
		System.out.println(index);
	}
	
}
