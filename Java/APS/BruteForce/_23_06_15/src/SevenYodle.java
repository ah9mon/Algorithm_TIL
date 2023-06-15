import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class SevenYodle {
    // index = 0~9 중 합이 100이 되는 7명 찾기
    static boolean answer = false; // 정답 출력 1번만 하기 위해

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] heights = new int[9];
        for (int i = 0; i < 9; i++) {
            heights[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(heights);
//        System.out.println(Arrays.toString(heights));

        boolean[] index = new boolean[9];
//        System.out.println(Arrays.toString(index));
        findSeven(heights, index, 0, 0, 0);
    }
    private static void findSeven(int[] height, boolean[] index, int nowIndex, int sum, int count) {

        if (answer) { // 정답 출력 이미 되었으면 종료
            return;
        } else if (count == 7) { // 7명 키를 더했을때
            if (sum == 100) { // 합이 100이면
                // 출력
                for (int i = 0; i < 9; i++) {
                    if (index[i] == true) System.out.println(height[i]);
                }
                answer = true;
            }
            return;
        } else if (count < 7 && sum > 100) { // 이미 100 넘어 버리면
            return;
        } else if (nowIndex == 9) { // 끝까지 갓는데 7명아니면
            return;
        } else {
            index[nowIndex] = true; // nowIndex번째 난쟁이를 일곱난쟁이에 포함
            findSeven(height, index, nowIndex+1, sum+height[nowIndex], count + 1);
            index[nowIndex] = false; // nowIndex번째 난쟁이를 일곱난쟁이에 포함하지 않고 넘어가기
            findSeven(height, index, nowIndex+1, sum, count);
        }
    }
}