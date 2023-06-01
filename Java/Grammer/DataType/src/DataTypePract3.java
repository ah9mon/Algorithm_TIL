public class DataTypePract3 {
    public static void main(String[] args) {
        String idNum = "881120-1068234";
        String birth = idNum.substring(0,6);
        String id = idNum.substring(7,idNum.length());
        System.out.println(birth);
        System.out.println(id);
        System.out.println(idNum.substring(0));
        System.out.println(idNum.substring(5));
        System.out.println(idNum.substring(7));
    }
}
