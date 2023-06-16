import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class ColorPaper {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][] white = new int[100][100];
        int numberOfBlackPaper = Integer.parseInt(br.readLine());
        for (int i = 0; i < numberOfBlackPaper; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int blackX = Integer.parseInt(st.nextToken()); // 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리
            int blackY = Integer.parseInt(st.nextToken()); // 색종이의 오른쪽 변과 도화지의 오른쪽 변 사이의 거리
            for (int y = blackY; y < blackY + 10; y++) {
                for (int x = blackX; x < blackX + 10; x ++) {
                    if (white[y][x] == 0) white[y][x] = 1;
                }
            }
        }

        int blackArea = 0;
        for (int row = 0; row < 100; row ++) {
            int sum = IntStream.of(white[row]).sum();
            blackArea += sum;
        }
        System.out.println(blackArea);
    }
}
