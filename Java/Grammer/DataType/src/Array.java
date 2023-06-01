public class Array {
    public static void main(String[] args) {
        int[] odds = {1,3,5,7,9};
        String[] weeks = {"월", "화","수", "목", "금", "토", "일"};
        String[] week2 = new String[7];
        week2[0] = "월";
        week2[1] = "화";
        week2[2] = "수";
        week2[3] = "목";
        week2[4] = "금";
        week2[5] = "토";
        week2[6] = "일";
        for (int i = 0; i < weeks.length; i ++) {
            System.out.println(week2[i]);
        }


    }
}
