import java.util.HashMap;

public class DataTypePractice {
    public static void main(String[] args) {
        HashMap<String,Integer> grades = new HashMap<>();
        grades.put("국어",80);
        grades.put("영어",75);
        grades.put("수학",55);
//        System.out.println(grades);
        int average = (grades.get("국어") + grades.get("영어") + grades.get("수학"))/3;
        System.out.println(average);
    }

}
