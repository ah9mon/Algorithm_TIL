import java.util.IntSummaryStatistics;
public class Multi {
    public int solution(int[] num_list) {
        int sum = sum(num_list);
        int multi = multiply(num_list);
        return (multi < sum) ? 1:0;
    }
    private static int sum(int[] num_list) {
        int sum = 0;
        for (int i = 0; i < num_list.length; i++) {
            sum += num_list[i];
        }
        return sum*sum;
    }

    private static int multiply(int[] num_list) {
        int multi = 1;
        for (int i = 0; i < num_list.length; i++) {
            multi *= num_list[i];
        }
        return multi;
    }
}
