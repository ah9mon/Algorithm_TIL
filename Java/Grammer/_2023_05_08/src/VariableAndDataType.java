public class VariableAndDataType {
    /*
    변수 이름 규칙
    1. 변수명은 숫자로 시작할 수 없음
    2. _ 와 $ 이외의 특수문자는 사용할 수 없다
    3. 자바의 키워드는 변수명으로 사용할 수 없다 (int, class, return 등)

    - 변수명 앞의 int, String 등은 변수의 자료형을 뜻함
     */
    public static void main(String[] args) {
        /*
        int a;
        String b;
        a = 1;
        b = "hello java";
        */
        int a = 1; // 선언과 동기에 값을 대입
        String b = "안녕 자바";
        System.out.println(a);
        System.out.println(b);

    }
}
