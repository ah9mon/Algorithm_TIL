import java.util.ArrayList;
import java.util.Arrays;

public class If {
    public static void main(String[] args) {
//        int money = 2000;
//        boolean hasCard = true;
//        if (money >= 3000 || hasCard) {
//            System.out.println("taxi");
//        } else {
//            System.out.println("walk");
//        }
//        ArrayList<String> pocket = new ArrayList<>();
//        pocket.add("paper");
//        pocket.add("handphone");
//        pocket.add("money");
//
//        if (pocket.contains("money")) {
//            System.out.println("taxi");
//        } else {
//            System.out.println("walk");
//        }
        boolean hasCard = true;
        ArrayList<String> pocket = new ArrayList<>();
        pocket.add("paper");
        pocket.add("airpods");
        if (pocket.contains("money")) {
            System.out.println("택시타고감");
        } else if (hasCard) {
            System.out.println("버스타고감");
        } else {
            System.out.println("걸어감");
        }

    }
}
