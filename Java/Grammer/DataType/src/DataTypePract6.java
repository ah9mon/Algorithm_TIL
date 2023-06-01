import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class DataTypePract6 {
    public static void main(String[] args) {
        ArrayList<Integer> lst = new ArrayList<>(Arrays.asList(1,3,5,4,2));
        System.out.println(lst);
        lst.sort(Comparator.naturalOrder());
        System.out.println(lst);
        lst.sort(Comparator.reverseOrder());
        System.out.println(lst);
    }
}
