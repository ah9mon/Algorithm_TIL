public class DataCastAndFinal {
    public static void main(String[] args) {
        String num = "123";
        int n = Integer.parseInt((num));
        System.out.println(n + 7);
        String num1 = String.valueOf(n);
        String num2 = Integer.toString(n);
        System.out.println(num1 + 1);
        System.out.println(num2 + 2);
        String float1 = "123.456";
        double d = Double.parseDouble(float1);
        System.out.println(d);

        int floatToInteger = (int) d;
        System.out.println(floatToInteger);

//        int errortest = Integer.parseInt(float1); // NumberFormatException
//        System.out.println(errortest);


    }
}
