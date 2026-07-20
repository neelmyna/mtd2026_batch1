package employee;

import java.util.Arrays;

public class Employee {
	
	public static void main(String[] args) {
		int array[] = {23, 5, 4, 21, 77, 10, 15};
		System.out.println("Input Array is: ");
		System.out.println(Arrays.toString(array));
		for(int i = 1; i < array.length; i++) {
			int element = array[i];
		    int j = i - 1;
		    while (j >= 0 && element < array[j]) {
			    array[j+1] = array[j];
			    j--;
		    }
			array[j+1] = element;
		}
		System.out.println("Sorted Array is: ");
		System.out.println(Arrays.toString(array));
	}
}