public class MixString {
    public StringBuilder solution(String str1, String str2) {
        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < (str1.length() + str2.length()); i++) {
            int index = i / 2;
            // i 가 홀수면
            if (i % 2 == 1) {
                answer.append(str2.charAt(index));
            } else {
                answer.append(str1.charAt(index));
            }
        }
        return answer;
    }
}
