public class CodeProcessing {
    public static String solution1(String code) {
        int mode = 0;
        StringBuilder ret = new StringBuilder();
        for (int i = 0; i < code.length(); i++) {

            char charValue = code.charAt(i);
            if (charValue == '1') {
                mode = ChangeMode(mode);
            } else {
                if (i % 2 == mode) ret.append(charValue);
            }
        }
        String answer = ret.toString();
        return answer.equals("") ? "EMPTY" : answer;
    }
    private static int ChangeMode(int mode) {
        return mode == 0 ? 1:0;
    }

    public static void main(String[] args) {
        String code = "";
        System.out.println("answer : " + solution1(code));
    }
}
