public class Sample2 {
    public void shouldBeRun() {
        System.out.println("ok thanks.");
    }

    public static void main(String[] args) {
        Sample2 sample = new Sample2();
        int c;
        try {
            c = 4 / 0;
            sample.shouldBeRun();  // 이 코드는 실행되지 않는다.
        } catch (ArithmeticException e) {
            c = -1;
            System.out.println(c);
        } finally {
            sample.shouldBeRun();
        }
    }
}
