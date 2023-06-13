import java.util.ArrayList;

public class MakeColahz {
    public ArrayList<Integer> solution(int n) {
        ArrayList<Integer> answer = new ArrayList<>();
        int num = n;
        answer.add(num);
        while (num > 1) {
            num = (num % 2 == 0) ? (num/2) : (3 * num + 1);
            answer.add(num);
        }
        return answer;
    }
}
