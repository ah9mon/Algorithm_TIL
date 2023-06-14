// for input
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class CupHolder {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int aNumberOfSeats = Integer.parseInt(br.readLine());
        String seats = br.readLine();
        int count = 0;

        for (int i = 0; i < aNumberOfSeats; i++) {
            // seats[i] == "S"면 왼쪽에 컵홀더 하나 + 1
            if (seats.charAt(i) == 'S') {
                count ++;
            } else {
                // seats[i] == "L"면 왼쪽에 컵홀터 하나 + 1 and i + 1
                count ++;
                i ++;
            }
        }

        // 맨끝에는 항상 컵홀더 하나 둘수 있으니까 i + 1
        count ++;

        // 좌석수 < 컵홀더 수 -> 좌석수
        if (count > aNumberOfSeats) {
            System.out.println(aNumberOfSeats);
        } else {
            System.out.println(count);
        }
    }
}
