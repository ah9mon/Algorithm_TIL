import java.util.ArrayList;
import java.util.Collections;

public class MakeArray {
    public ArrayList<Integer> solution(int l, int r) {
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i = l; i <= r; i++) {
            String num = String.valueOf(i);
            for (int j = 0; j < num.length(); j++) {
                char value = num.charAt(j);
                if (value != '0' && value != '5') break;
                if (j == num.length() - 1) answer.add(i);
            }
        }
        if (answer.isEmpty()) {
            answer.add(-1);
        } else {
            Collections.sort(answer);
        }
        return answer;
    }
}
