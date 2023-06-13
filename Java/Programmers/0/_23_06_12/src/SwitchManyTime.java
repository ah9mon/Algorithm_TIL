public class SwitchManyTime {
    public String solution(String my_string, int[][] queries) {
        String[] charValues = my_string.split("");
        for (int[] query:queries) {
            for (int i = 0; i <= (int) (query[1]-query[0])/2; i++) {
                String temp = charValues[query[0] + i];
                charValues[query[0] + i] = charValues[query[1] - i];
                charValues[query[1] - i] = temp;
            }
        }
        return String.join("",charValues);
    }
}
