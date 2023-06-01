import java.util.Scanner;

public class Pract2 {
    static void LowerToUpper() {
        while (true) {
            // 소문자 입력받기

            System.out.print("소문자로 영문을 입력해주세요 (종료 : ESC입력) : ");
            Scanner sc = new Scanner(System.in);
            String lower = sc.nextLine();
            if (lower.equals("ESC")) {
                break;
            }
            String upper = lower.toUpperCase();
            System.out.printf("\n대문자로 변환 완료 : %s\n",upper);
        }
    }

    public static void main(String[] args) {
        Pract2.LowerToUpper();
    }
}
