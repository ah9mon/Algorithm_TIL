import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Caster {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 구역의 크기
        int h = Integer.parseInt(st.nextToken()), w = Integer.parseInt(st.nextToken());

        // 구역
        String[] area = new String[h];
        for (int i = 0; i < h; i++) {
            area[i] = br.readLine();
        }

        weatherForecast(h,w,area);
    }

    private static void weatherForecast(int h, int w, String[] area) {
        int[][] forecast = new int[h][w];
        for (int row = 0; row < h; row++) {
            int count = 0;
            boolean cloud = false;
            for (int col = 0; col < w; col++) {
                if (area[row].charAt(col) == 'c') { // 구름 있으면
                    forecast[row][col] = 0;
                    count = 0;
                    cloud = true;
                } else { // 구름 없으면
                    if (cloud) { // 같은 row 이전 col 에 구름 있었으면
                        count ++;
                        forecast[row][col] = count;
                    } else { // 구름 없었으면
                        forecast[row][col] = -1;
                    }
                }
            }
        }

        for (int j = 0; j < h; j++) {
            String line = Arrays.stream(forecast[j])
                    .mapToObj(String::valueOf)
                    .collect(Collectors.joining(" "));
            System.out.println(line);
        }
    }
}
