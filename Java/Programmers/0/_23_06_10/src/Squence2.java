import java.util.ArrayList;

public class Squence2 {
    public int[] solution(int[] arr,int[][] queries) {
        int[] answer  = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int[] query = queries[i];
            int minNumOverK = 1000001;
            for (int j = query[0]; j <= query[1]; j++) {
                if (arr[j] > query[2] && arr[j] < minNumOverK) minNumOverK = arr[j];
            }
            answer[i] = minNumOverK==1000001 ? -1 : minNumOverK;
        }
        return answer;
    }
}
