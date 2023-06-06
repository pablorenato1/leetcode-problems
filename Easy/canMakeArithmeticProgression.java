package Easy;
// Answer ----------------------------------------------------
import java.util.Arrays;

class Solution {
    boolean oppositeOperation(int number1, int number2) {
        if (number1 == number2 || number1 == -number2) { //The same number, so its ok
            return true;
        } else {
            return false;
        }
    }

    public boolean canMakeArithmeticProgression(int[] arr) {
        Arrays.sort(arr);
        int difBetweenNumber = 0;
        int index = 0;
        do {
            int currentDif = 0;
            if (arr[index] > arr[index+1]) {
                // the current number is bigger than the next one
                currentDif = arr[index] - arr[index+1];
            } else {
                // the next one number is bigger than the current one
                currentDif = arr[index+1] - arr[index];
            }
            if (index == 0) { //If its the firs interaction save it
                difBetweenNumber = currentDif;
            } else if (!oppositeOperation(difBetweenNumber, currentDif)) {
                // Try out if the number
                return false;
            } 
            index += 1;
        } while (index < arr.length-1);
        return true;
    }

    // If you want to test just uncomment the script bellow

    // public static void main(String[] args) { 
    //     int numbers[] = {3,5,1}; // list you want to test
    //     Solution result = new Solution();

    //     System.out.println(result.canMakeArithmeticProgression(numbers));
    // }
}

