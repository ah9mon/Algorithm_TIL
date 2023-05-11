public class DataTypeStringBuffer {
    public static void main(String[] args) {
        /*
        StringBuffer sb = new StringBuffer();
        sb.append("hello");
        sb.append(" ");
        sb.append("jump to java");
        String result = sb.toString();
        System.out.println(result);

        String result2 = "";
        result2 += "hello";
        result2 += " ";
        result2 += "jump to java";
        System.out.println(result2);
        */

        /*
        String은 immutable하다 -> 한번 생성하면 그 값 변경불가 -> trim,toUpperCase 등의 메서드를 보면
        문자열이 변경되는 것 같지만 해당 메서드 수행시 또 다른 String 객체를 생성해서 리턴할 뿐임
        반면 StringBuffer는 mutable함
        문자열 변경 작업 많을 때는 StringBuffer 사용하자
         */


        /*
        StringBuffer sb2 = new StringBuffer();
        sb2.append("jump to java");
        sb2.insert(0,"hello ");
        System.out.println(sb2.toString());
        System.out.println(sb2.substring(0,4));
        */



    }
}
