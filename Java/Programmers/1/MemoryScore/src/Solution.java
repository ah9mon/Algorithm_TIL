import java.util.Arrays;
import java.util.ArrayList;
class Solution {
    public ArrayList<Integer> solution(String[] name, int[] yearning, String[][] photo) {
        ArrayList<Integer> answer = new ArrayList();
        // photo안의 사람명단 하나씩 꺼내서 반복문 돌리기
        for (String[] peopleInPhoto:photo) {
            // 사진속 추억 점수를 매길 count 선언 및 초기화
            int count = 0;
            // name의 사람 수 만큼 반복문 돌리기 i == 인덱스
            for (int i=0; i < name.length; i++) {
                // 사진 속에 name[i] 가 있으면 count += yearning[i]
                if (Arrays.asList(peopleInPhoto).contains(name[i])) {
                    count += yearning[i];
                }
            }
            // 반복문 끝나면 count를 answer안에 추가
            answer.add(count);
        }
        return answer;
    }
}
