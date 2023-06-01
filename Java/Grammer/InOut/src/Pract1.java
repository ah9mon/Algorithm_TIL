import java.util.Scanner;

public class Pract1 {
    //2개 숫자 입력 받고 그 합을 return하는 method
    static int PlusProgram() {
        int sum = 0;
        for (int i = 0; i < 2; i++) {
            System.out.printf("%d번째 정수 입력 : ",i+1);
            Scanner sc = new Scanner(System.in);
            int num = sc.nextInt();
            sum += num;
            System.out.println("");
        }
        return  sum;
    }

    public static void main(String[] args) {
        int sum = Pract1.PlusProgram();
        System.out.println(sum);
    }
}
