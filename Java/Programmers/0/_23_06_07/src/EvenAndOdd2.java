
public class EvenAndOdd2 {
    public int solution(int n) {
        int rlt = 0;
        for (int i = 1; i <= n; i++) {
            if (n % 2 == 0 && i % 2 == 0) {
                rlt += Math.pow(i,2);
            } else if (n % 2 == 1 && i % 2 == 1) {
                rlt += i;
            }
        }
        return rlt;
    }
}
