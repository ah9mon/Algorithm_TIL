import java.util.ArrayList;

public class Calculator {
    int value;

    Calculator() {
        this.value = 0;
    }

    void add(int val) {
        this.value += val;
    }

    boolean isOdd(int num) {
        if (num % 2 == 1) {
            return true;
        } else {
            return false;
        }
    }

    float avg(int[] data) {
        int sum = 0;
        for (int num:data
             ) {
            sum += num;
        }
        return sum/data.length;
    }

    float avg(ArrayList<Integer> data) {
        int sum = 0;
        for (int num:data
             ) {
            sum += num;
        }
        return sum/data.size();
    }

    int getValue() {
        return this.value;
    }
}
