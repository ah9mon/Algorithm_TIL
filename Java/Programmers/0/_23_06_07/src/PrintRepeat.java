import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class PrintRepeat {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String str = st.nextToken();
        int n = Integer.parseInt(st.nextToken());

        // String 사이의 + 연산을 하면서 새로운 String 객체가 생성되는 낭비 방지하고자 StringBuilder 사용
        StringBuilder rlt = new StringBuilder();
        for (int i = 0; i < n; i++) {
            rlt.append(str);
        }
        System.out.println(rlt);
    }
}
