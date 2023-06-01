import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class List {
    public static void main(String[] args) {
//        ArrayList<String> pitches = new ArrayList<>();
//        pitches.add("138");
//        pitches.add("129");
//        pitches.add("142");
//        for (int i = 0; i < pitches.size(); i++) {
//            System.out.println(pitches.get(i));
//        }
//        System.out.println(pitches);
//        System.out.println(pitches.contains("142"));
//        System.out.println(pitches.remove("142"));
//        System.out.println(pitches.remove(0));
//        for (int i = 0; i < pitches.size(); i++) {
//            System.out.println(pitches.get(i));
//        }
        String[] data = {"3","2","1","4"};
        ArrayList<String> pitches = new ArrayList<>(Arrays.asList(data));
//        System.out.println(pitches);
//        String rlt = "";
//        for (int i = 0; i < pitches.size(); i++) {
//            rlt += pitches.get(i);
//            rlt += " ";
//        }
//        rlt = rlt.substring(0, rlt.length() - 1);
//        System.out.println(rlt);
//        String rlt2 = String.join(" ", pitches);
//        System.out.println(rlt2);
        pitches.sort(Comparator.naturalOrder()); //오름차순 정렬
        System.out.println(pitches);
        pitches.sort(Comparator.reverseOrder());
        System.out.println(pitches);
    }
}
