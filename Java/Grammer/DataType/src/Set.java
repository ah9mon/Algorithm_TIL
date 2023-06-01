import java.util.Arrays;
import java.util.HashSet;

public class Set {
    public static void main(String[] args) {
//        HashSet<String> set = new HashSet<>(Arrays.asList("H", "e", "l", "l", "o"));
//        System.out.println(set);
        HashSet<Integer> s1 = new HashSet<>(Arrays.asList(1,2,3,4,5,6));
        HashSet<Integer> s2 = new HashSet<>(Arrays.asList(4,5,6,7,8,9));

        HashSet<Integer> intesection = new HashSet<>(s1);
        intesection.retainAll(s2);
        System.out.println(intesection);

        HashSet<Integer> union = new HashSet<>(s1);
        union.addAll(s2);
        System.out.println(union);

        HashSet<Integer> substract = new HashSet<>(s1);
        substract.removeAll(s2);
        System.out.println(substract);

        HashSet<String> set = new HashSet<>();
        set.add("Jump");
        set.add("to");
        set.add("Java");
        System.out.println(set);

        HashSet<String> set2 = new HashSet<>();
        set2.addAll(Arrays.asList("Jump","to","Java"));
        System.out.println(set2);

        set2.remove("to");
        System.out.println(set2);






    }
}
