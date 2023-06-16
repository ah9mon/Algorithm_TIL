import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class CutPaper {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        ArrayList<Integer> checkPointX = new ArrayList<>(); // 잘린 x 부분 리스트
        checkPointX.add(0);
        ArrayList<Integer> checkPointY = new ArrayList<>(); // 절린 y 부분 리스트
        checkPointY.add(0);

        StringTokenizer st1 = new StringTokenizer(br.readLine());
        checkPointX.add(Integer.parseInt(st1.nextToken()));
        checkPointY.add(Integer.parseInt(st1.nextToken()));

        int numberOfLine = Integer.parseInt(br.readLine()); // 자를 점선의 수
        for (int i = 0; i < numberOfLine; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            String code = st2.nextToken();
            if (code.equals("0")) { // 가로 점선이면
                checkPointY.add(Integer.parseInt(st2.nextToken()));
            } else { // 세로 점선이면
                checkPointX.add(Integer.parseInt(st2.nextToken()));
            }
        }

        Collections.sort(checkPointX);
        Collections.sort(checkPointY);

        int longestX = findLongestLine(checkPointX);
        int longestY = findLongestLine(checkPointY);

        System.out.println(longestX * longestY);
     }

     private static int findLongestLine(ArrayList<Integer> checkPoint) {
        int longestLine = 0;
        for (int i = 0; i < checkPoint.size() - 1; i ++) {
            int nowLine = checkPoint.get(i+1) - checkPoint.get(i);
            if (nowLine > longestLine) longestLine = nowLine;
        }
        return longestLine;
     }
}
