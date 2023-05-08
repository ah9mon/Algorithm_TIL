import java.lang.reflect.Array;
import java.util.*;


public class DataTypeString {
    public static void main(String[] args) {
        String a = "Hangyeol Eom"; // literal 표기
        String b = "a";
        String c = "123";
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        String d = new String("Hangyeol Eom");
        System.out.println(d);
        /*
        new 라는 키워드는 객체를 만들 때 사용
        하지만 보통 문자열을 표현할 때 가급적 리터럴 표기
        -> 가독성 증가, 컴파일 시 최적화에 도움

        리터럴 표기법은 문자열을 JVM의 intern pool 이라는 메모리 공간에 저장하고 다음에 다시 동일한 문자열이 선언될때
        cache 된 문자열을 리턴함
        이와 달리 두번째 (new) 방식은 항상 새로운 String 객체를 만든다
        */

        // equal 두개의 문자열이 동일한지를 비교하여 결과값을 리턴
        String firstName = "Hangyeol";
        String lastName = "Eom" ;
        String fullName = "Hangyeol Eom";
        System.out.println(fullName.equals(firstName)); //false
        System.out.println(fullName.equals(firstName + " " + lastName)); // true

        // indexOf 문자열에서 특정 문자열이 시작되는 위치(인덱스)를 리턴
        System.out.println(fullName.indexOf("Eom")); // 9

        // charAt 문자열에서 특정 위치의 문자를 리턴
        System.out.println(fullName.charAt(9)); // E

        // replaceAll 특정 문자열을 다른 문자열로 바꿀때 사용
        System.out.println(fullName.replaceAll("Eom", "Choi"));

        // substring 문자열 중 특정 부분을 뽑아낼 때 사용
        System.out.println(fullName.substring(9,12)); // Eom

        // toUpperCase 문자열을 모두 대문자로 변경
        System.out.println(fullName.toUpperCase());

        // split 문자열을 특정 구분자로 나누어 문자열 배열로 리턴하는 메서드
        String[] names = fullName.split(" ");
        System.out.println(Arrays.toString(names));

        // 문자열 포멧팅
        System.out.println(String.format("hi, %s", firstName));
        int day = 8;
        System.out.println(String.format("hi, %s today is %dth", firstName, day));

        System.out.printf("hi, %s today is %dth", firstName, day); // String.format 메서드 없이 가능
    }
}
