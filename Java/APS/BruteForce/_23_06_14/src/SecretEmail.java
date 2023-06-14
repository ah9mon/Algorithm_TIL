import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SecretEmail {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String message = br.readLine();

        int[] rowCol = findRowCol(message.length()); // row, col 찾기
        int row = rowCol[0];
        int col = rowCol[1];

        char[][] cipher = encrypt(row,col,message); // 암호화
        decipher(row,col,cipher); // 해독
    }

    private static int[] findRowCol (int n) {
        int maxR = 1;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0 && i <= (n / i)) {
                if (maxR < i) maxR = i;
            } else if (i > n/i) {
                break;
            }
        }
        int[] rowCol = {maxR, n / maxR};
        return rowCol;
    }
    private static char[][] encrypt(int row, int col, String message) {
        char[][] cipher = new char[row][col];
        int index = 0;
        for (int c = 0; c < col; c++) {
            for (int r = 0; r < row; r ++) {
                cipher[r][c] = message.charAt(index);
                index++;
            }
        }
        return cipher;
    }
    private static void decipher(int row, int col, char[][] cipher) {
        StringBuilder sb = new StringBuilder();
        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                sb.append(cipher[r][c]);
            }
        }
        System.out.println(sb);
    }
}
