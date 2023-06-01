import java.util.Scanner;
import java.io.IOException;
import java.io.FileWriter;
import java.io.PrintWriter;
public class Pract4 {
    // 사용자 입력 받고 리턴하는 메소드
    static String ConsoleIn() {
        Scanner sc = new Scanner(System.in);
        String userInput = sc.nextLine();
        System.out.println();
        return userInput;
    }

    // 파일 입력 메소드
    static void FileWrite (String userInput, String file) throws IOException {
        PrintWriter pw = new PrintWriter(new FileWriter(String.format("%s",file), true));
        pw.println(userInput);
        pw.close();
        System.out.print("\n 파일 수정 완료!");
    }

    public static void main(String[] args) throws IOException{
        System.out.println("수정하고 싶은 파일명을 입력하세요 : ");
        String fileName = Pract4.ConsoleIn();
        System.out.println("추가하고 싶은 내용을 입력하세요 : ");
        String userInput = Pract4.ConsoleIn();
        Pract4.FileWrite(userInput, fileName);
    }
}
