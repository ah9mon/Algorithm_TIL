import java.util.ArrayList;

public class MakeString5 {
    public ArrayList<Integer> solution(String[] intStrs, int k, int s, int l) {
        ArrayList<Integer> answer = new ArrayList<>();
        for (String num:intStrs) {
            int slicedNum = Integer.parseInt(num.substring(s, s+l));
            if (slicedNum > k) answer.add(slicedNum);
        }
        return answer;
    }
}
