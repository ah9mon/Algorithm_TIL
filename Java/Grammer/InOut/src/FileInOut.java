import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.io.FileReader;
import java.io.BufferedReader;

public class FileInOut {
//    public static void main(String[] args) throws IOException{
////        FileOutputStream output = new FileOutputStream("./out.txt");
//        FileWriter fw = new FileWriter("./out.txt");
//        for (int i = 1; i < 11; i++) {
//
//            String data = i+" 번째 줄입니다.\n";
////            output.write(data.getBytes());
//            fw.write(data);
//        }
//        fw.close();
//    }
//    public static void main(String[] args) throws IOException{
//        PrintWriter pw = new PrintWriter("./out.txt");
//        for (int i = 1; i < 11; i ++) {
//            String data = i+" 번째 줄입니다람쥐.";
//            pw.println(data);
//        }
//        pw.close();
//    }
//    public static void main(String[] args) throws IOException {
//                FileWriter fw = new FileWriter("./out.txt", true);
//
//                for(int i = 11;i < 21; i++) {
//                    String data = i+" 번째 줄입니다크나이트.\n";
//                    fw.write(data);
//                }
//                fw.close();
//    }
//    public static void main(String[] args) throws IOException{
//        PrintWriter pw = new PrintWriter(new FileWriter("./out.txt", true));
//        for (int i = 21; i < 31; i ++) {
//            String data = i+" 번째 줄입니다익스트라.";
//            pw.println(data);
//        }
//        pw.close();
//    }
    public static void main(String[] args) throws  IOException{
        BufferedReader br = new BufferedReader(new FileReader("./out.txt"));
        while (true) {
            String line = br.readLine();
            if (line == null) break;
            System.out.println(line);
        }
        br.close();
    }
}
