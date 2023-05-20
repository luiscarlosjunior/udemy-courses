
public class UniqueNumberSolutions {
	public static int bruteForce(int n, int[] array) {
		// Anda por todo o array
		for (int i = 0; i < n; i++) {
			int currentNumber = array[i];
			int counter = 0;
			
			for(int j = 0; j < n; j++) {
				if (array[j] == currentNumber) {
					counter++;
					if(counter > 1) {
						break;
					}
				}
			}
			
			// check whether this is a solution
			if(counter == 1) {
				return currentNumber;
			}
		}
		return -1;
	}

	public static int xor(int n, int[] array) {
		int result = 0;
		for(int i = 0; i < n; i++) {
			result ^= array[i];
		}
		return result;
	}
	
	// 2 solução
	public static int countingArray(int n, int[] array) {
		int maxNumber = 0;
		for(int i = 0; i < n; i++ ) {
			if(array[i] > maxNumber) {
				maxNumber = array[i];
			}
			if(array[i] < 0) {
				return -1;
			}
		}
		
		int[] count = new int[maxNumber + 1];
		for(int i = 0; i < n; i++) {
			int currentNumber = array[i];
			count[currentNumber]++;
		}
		
		for(int i = 0; i < n; i++) {
			int currentNumber = array[i];
			if(count[currentNumber] == 1) {
				return currentNumber;
			}
		}
		return -1; // Invalid array
	}
}
