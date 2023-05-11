public class DataTypeArray {
    public static void main(String[] args) {
        int[] odds = {1,2,3,4,5};
        String[] weeks = new String[7];
        weeks[0] = "monday";
        weeks[1] = "화";
        weeks[2] = "수";
        weeks[3] = "목";
        weeks[4] = "금";
        weeks[5] = "토";
        weeks[6] = "일";
        for (int i=0; i < weeks.length; i++) {
            System.out.println(weeks[i]);
        }

    }
}
