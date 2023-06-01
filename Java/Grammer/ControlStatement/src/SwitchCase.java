public class SwitchCase {
    public static void main(String[] args) {
        int month = 8;
        String monthString = "";
        switch (month) {
            case 1: monthString = "January";
                    break;
            case 10: monthString = "October";
                    break;
            case 8: monthString = "August";
                    break;

        }
        System.out.println(monthString);
    }
}
