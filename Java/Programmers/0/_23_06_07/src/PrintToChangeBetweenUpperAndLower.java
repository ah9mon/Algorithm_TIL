import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class PrintToChangeBetweenUpperAndLower {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringBuilder rlt = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            char charValue = str.charAt(i);

            // str[i] 가 대문자이면
            if (Character.isUpperCase(charValue)) {
                // 소문자로
                charValue = Character.toLowerCase(charValue);
            } else {
                // str[i] 가 소문자면
                // 대문자로
                charValue = Character.toUpperCase(charValue);
            }
            // StringBuilder에 추가
            rlt.append(charValue);
        }
        System.out.println(rlt);
    }
}
