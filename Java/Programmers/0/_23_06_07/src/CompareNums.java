public class CompareNums {
    public int solution(int a, int b) {
        String string_a = String.valueOf(a);
        int n1 = Integer.parseInt(string_a + b);
        int n2 = 2 * a * b;
        return Math.max(n1,n2);
    }
}
