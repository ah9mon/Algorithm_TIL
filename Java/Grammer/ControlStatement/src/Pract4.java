public class Pract4 {
    public static void main(String[] args) {
        int[] marks = {70,60,55,75,95,90,80,80,85,100};
        int sum = 0;
        for (int mark:marks
             ) {
            sum += mark;
        }
        float average = sum/marks.length;
        System.out.println(average);
    }
}
