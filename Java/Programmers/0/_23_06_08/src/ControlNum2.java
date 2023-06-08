public class ControlNum2 {
    public StringBuilder solution(int[] numLog) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < numLog.length - 1; i++) {
            int n = numLog[i+1] - numLog[i];
            if (n == 1) {
                sb.append("w");
            } else if (n == -1) {
                sb.append("s");
            } else if (n == 10) {
                sb.append("d");
            } else if (n == -10) {
                sb.append("a");
            }
        }
        return sb;
    }
}
