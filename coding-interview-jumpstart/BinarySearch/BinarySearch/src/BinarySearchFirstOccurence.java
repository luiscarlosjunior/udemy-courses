
public class BinarySearchFirstOccurence {
	public static int firstOccurrence(int[] array, int target) {
		int lo = 0;
		int hi = array.length - 1;
		while (lo < hi) {
			int mid = (lo + hi) / 2;
			if(target > array[mid]) {
				lo = mid + 1;
			} else {
				hi = mid;
			}
		}

		if(array[lo] == target) {
			return lo;
		} else {
			return -1;
		}
	}
	
	public static int lastOccurrence(int[] array, int target) {
		int lo = 0;
		int hi = array.length - 1;
		while (lo < hi) {
			int mid = (lo + hi + 1) / 2;
			if(target < array[mid]) {
				hi = mid - 1;
			} else {
				lo = mid;
			}
		}

		if(array[lo] == target) {
			return lo;
		} else {
			return -1;
		}
	}
	
	public static int numberOfOccurences(int[] array, int target) {
		int first = firstOccurrence(array, target);
		int last = lastOccurrence(array, target);
		if(first > 0) {
			return last - first + 1;
		}
		return 0;
	}
	
}
