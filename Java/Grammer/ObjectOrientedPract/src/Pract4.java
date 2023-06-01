import java.util.ArrayList;
import java.util.Arrays;

import java.util.Arrays;
import java.util.ArrayList;

public class Pract4 {
    public static void main(String[] args) {
        int[] data = {1,3,5,7,9};
        Calculator cal = new Calculator();
        float result = cal.avg(data);
        System.out.println("Arrays ver : " + result);

        ArrayList<Integer> data2 = new ArrayList<>(Arrays.asList(1,3,5,7,9));
        Calculator cal2 = new Calculator();
        float result2 = cal.avg(data2);
        System.out.println("ArrayList ver : " + result2);
    }
}
