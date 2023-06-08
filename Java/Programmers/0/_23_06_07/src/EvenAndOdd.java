import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
public class EvenAndOdd {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        if (n%2 == 1) {
            System.out.printf("%d is odd", n);
        } else {
            System.out.printf("%d is even", n);
        }
    }
}
