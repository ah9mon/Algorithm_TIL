public class ControlNum1 {
    public int solution(int n, String control) {
        return ControlNumber(n, control);
    }

    private static int ControlNumber(int n, String code) {
        for (int i = 0; i < code.length(); i++) {
            char charValue = code.charAt(i);
            if (charValue == 'w') {
                n += 1;
            } else if (charValue == 's') {
                n -= 1;
            } else if (charValue == 'd') {
                n += 10;
            } else if (charValue == 'a') {
                n -= 10;
            }
        }
        return n;
    }
}
