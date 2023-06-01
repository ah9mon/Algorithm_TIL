import java.util.Arrays;
import java.util.ArrayList;
import java.util.HashSet;
public class DataTypePract9 {
    public static void main(String[] args) {
        ArrayList<Integer> numbers = new ArrayList<>(Arrays.asList(1,1,1,1,1,1,2,3,3,3,4,4,5));
        HashSet<Integer> numSet = new HashSet<>(numbers);
        System.out.println(numSet);
    }
}
