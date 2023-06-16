import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class CroatiaAlpha {
    public static void main(String[] args) throws IOException {
        String[] data = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
        ArrayList alphabets = new ArrayList<>(Arrays.asList(data));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine();
        int n = word.length();

        int countAlphabet = 0;
        for (int i = 0; i < n; i++) {
            int index = i;
            StringBuilder sub = new StringBuilder();
            while (true) {
                sub.append(word.charAt(index));
                // 알파벳 리스트에 포함이면 (start - end)만큼 카운트하고 반복문 종료
                if (alphabets.contains(sub.toString())) {
                    countAlphabet += 1;
                    i = index;
                    break;
                } else if ((index - i + 1) == 3) {
                    // sub의 길이가 3인데도 포함 아니면 처음 알바벳 하나만 카운트하고 넘어가기
                    countAlphabet += 1;
                    break;
                } else {
                    index += 1;

                    // end가 index 범위 초과하면
                    if (index > word.length() - 1) {
                        countAlphabet += (index - i);
                        System.out.println(countAlphabet);
                        return;
                    }
                }
            }
        }
        System.out.println(countAlphabet);
    }
}