import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SuperMario {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int sum = 0;
        for (int i = 0; i < 10; i++) {
            int mushroom = Integer.parseInt(br.readLine());
            if (sum + mushroom > 100) {
                if ( 100 - sum >= sum + mushroom - 100) {
                    sum += mushroom;
                    break;
                } else {
                    break;
                }
            } else {
                sum += mushroom;
            }
        }
        System.out.println(sum);
    }
}
