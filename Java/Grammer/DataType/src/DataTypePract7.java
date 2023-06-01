import java.util.Arrays;
import java.util.ArrayList;

public class DataTypePract7 {
    public static void main(String[] args) {
        ArrayList<String> words = new ArrayList<>(Arrays.asList("Life","is","too","short"));
        System.out.println(String.join(" ",words));
    }
}
