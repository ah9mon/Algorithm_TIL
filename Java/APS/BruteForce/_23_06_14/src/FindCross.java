import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class FindCross {
    public static void main(String[] args) throws IOException{
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());

            // 격자판의 크기
            int row =  Integer.parseInt(st.nextToken());
            int col = Integer.parseInt(st.nextToken());

            // 격자판
            String[] arr = new String[row];
            for (int i = 0; i < row; i ++) {
                arr[i] = br.readLine();
                if( (i == 0 || i == row - 1 ) && (arr[i].charAt(0) == '*' || arr[i].charAt(col-1) == '*')) {
                    System.out.println(-1);
                    return;
                }
            }
            findCross(row,col,arr);
    }

    private static void findCross(int row, int col, String[] arr) {
        boolean flag = true;
        int[][] visited = new int[row][col];
        int count = 0; // 십자가 개수
        ArrayList<String> crossInfomations = new ArrayList<>(); // 십가자 정보 담은 리스트
        int[] dx = {1,0,-1,0};
        int[] dy = {0,1,0,-1};

        for (int r = 1; r < row-1; r ++ ) {
            for (int c = 1; c < col-1; c ++) {
                // 십자가 탐색
                if (arr[r].charAt(c) == '*') {
                    int l = Math.min(row-r-1, col-c-1); // 십자가 길이
                    while (true) {
                        int aNumOfLine = 0;
                        for (int i = 0; i < 4; i ++) {
                            int nx = c, ny = r;
                            for (int len = l; len > 0; len--) {
                                nx += dx[i];
                                ny += dy[i];
                                if (0 <= nx && nx < col && 0 <= ny && ny < row && arr[ny].charAt(nx) == '*' ) {
                                    // 범위조건, '*' 인지 확인

                                    if (len == 1) aNumOfLine += 1;
                                }
                            }
                        }
                        if (aNumOfLine == 4) {
                            // 길이가 l인 십자가 되면

                            // 십자가 있는 곳 체크
                            for (int cRow = r - l; cRow <= r + l; cRow++ ) {
                                for (int cCol = c - l; cCol <= c + l; cCol++ ) {
                                    if (visited[cRow][cCol] == 0) visited[cRow][cCol] = 1;
                                }
                            }

                            count += l; // 십자가 개수 카운트
                            // 십자가 정보 추가
                            for (int j = l; j > 0; j --) {
                                String crossInfo = String.format("%d %d %d", r+1,c+1,j);
                                crossInfomations.add(crossInfo);
                            }
                            break;

                        } else {
                            l --; // 길이가 l - 1 인 십자가 탐색을 위해
                            if (l == 0) break;
                        }
                    }
                }
            }
        }

        // 남은 * 있는지 확인
        int dotCount = 0;
        for (int fRow = 0; fRow < row; fRow++) {
            for (int fCol = 0; fCol < col; fCol++) {
                char now = arr[fRow].charAt(fCol);
                if (now == '*' && visited[fRow][fCol] != 1) {
                    // *인데 십자가에 포함안되면
                    flag = false;
                } else if (now == '.') {
                    dotCount ++;
                }
            }
        }

        if (dotCount == row*col) flag = false;

        if (flag) {
            System.out.println(count);
            for (int j = 0; j < count; j ++) {
                System.out.println(crossInfomations.get(j));
            }
        } else {
            System.out.println(-1);
        }
    }
}
