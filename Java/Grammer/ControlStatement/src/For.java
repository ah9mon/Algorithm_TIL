import java.util.ArrayList;
import java.util.Arrays;

public class For {
    public static void main(String[] args) {
//        ArrayList<String> numbers = new ArrayList<>(Arrays.asList("one","two","three"));
//        for (int i = 0; i < numbers.size(); i++) {
//            System.out.println(numbers.get(i));
//        }
//        int [] marks = {90,25,67,45,80};
//        for (int i = 0; i < marks.length; i++) {
//            if (marks[i] >= 60) {
//                System.out.println(String.format("%d번 학생은 합격입니다",i+1));
//            } else {
//                System.out.println(String.format("%d번 학생은 불합격입니다",i+1));
//            }
//        }
        int [] marks = {90,25,67,45,80};
        for (int i = 0; i < marks.length; i++) {
            if (marks[i] < 60) {
                continue;
            }
            System.out.println(String.format("축하합니다!! %d번 학생은 합격입니다.",i+1));
        }
    }
}
