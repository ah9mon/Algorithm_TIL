public class Pract2 {
    public static void main(String[] args) {
        MaxLimitCalculator cal = new MaxLimitCalculator();
        cal.add(50);
        System.out.println(cal.getValue());
        cal.add(60);
        System.out.println(cal.getValue());
    }
}
