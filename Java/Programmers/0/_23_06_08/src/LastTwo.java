import java.util.ArrayList;
import java.util.Arrays;

public class LastTwo {
    public int[] solution(int[] num_list) {
        int lastNum1 = num_list[num_list.length - 1];
        int lastNum2 = num_list[num_list.length - 2];
        int newNum = ( lastNum1 > lastNum2 ) ? (lastNum1 - lastNum2) : lastNum1 * 2;

        int[] answer = new int[num_list.length + 1];
        for (int i = 0; i < num_list.length + 1; i++) {
            if (i == num_list.length) {
                answer[i] = newNum;
            } else {
                answer[i] = num_list[i];
            }
        }
        return answer;
    }
}
