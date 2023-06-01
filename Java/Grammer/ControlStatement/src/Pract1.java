public class Pract1 {
    public static void main(String[] args) {
        int sum = 0;
        int i = 0;
        while (i<1000) {
            i++;
            if (i%3 == 0) {
                sum += i;
            }
        }
        System.out.println(sum);
    }
}
