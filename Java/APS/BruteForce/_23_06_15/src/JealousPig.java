import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class JealousPig {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());

        for (int tc = 0; tc < testCase; tc++) {

            int n = Integer.parseInt(br.readLine()); // 하루에 배달되는 사료의 양

            // 첫날 먹은 사료의 양
            StringTokenizer st = new StringTokenizer(br.readLine());
            long[] meals = new long[6];
            for (int pigNum = 0; pigNum < 6; pigNum++) {
                meals[pigNum] = Long.parseLong(st.nextToken());
            }

            int day = 1;
            long sum = sum(meals);
            while (true) {
                // 식사양 > n -> sout(day)
                if (sum > n) {
                    System.out.println(day);
                    break;
                } else { // 식사양 <= n -> 다음날
                    day ++;
                    sum = sum * 4; // 4배씩 증가함 식사량
                }
            }
        }
    }

    private static long sum(long[] meals) {
        long sum = 0;
        for (int i = 0; i < 6; i++) {
            sum += meals[i];
        }
        return sum;
    }
}
