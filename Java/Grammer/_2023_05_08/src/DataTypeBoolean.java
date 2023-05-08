public class DataTypeBoolean {
    public static void main(String[] args) {
        boolean isSuccess = true;
        boolean isTest = false;

        System.out.println(2 > 1); // true
        System.out.println(1==2); // false
        System.out.println(3%2==1); // true
        System.out.println("3".equals("2")); // false

        if (isSuccess) {
            System.out.println("성공");
        }

        int i = 3;
        boolean isOdd = i%2 == 1;
        System.out.println(isOdd); // true
    }
}
