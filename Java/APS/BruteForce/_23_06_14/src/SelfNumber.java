public class SelfNumber {
    public static void main(String[] args) {
        for (int i = 1; i <= 10000; i++) {
            if (!checkNumber(i)) System.out.println(i);
        }
    }

    private static boolean checkNumber(int n) {
        boolean flag = false;
        for (int i = n-1; i > 0; i--) {
            int sum = i;
            String num = String.valueOf(i);
            for (int j = 0; j < num.length(); j++) {
                sum += Character.getNumericValue(num.charAt(j));
            }
            if (sum == n) {
                flag = true;
                break;
            }
        }
        return flag;
    }
}
