class Calculator1 {
    static int result = 0;

    static int add(int num) {
        result += num;
        return result;
    }

    static int sub(int num) {
        result -= num;
        return result;
    }
}
class Calculator2 {
    static int result = 0;

    static int add(int num) {
        result += num;
        return result;
    }
}
public class ObjectOriented {
    public static void main(String[] args) {
        System.out.println(Calculator1.add(3));
        System.out.println(Calculator2.add(4));

        Calculator1 cal1 = new Calculator1();
        System.out.println(cal1.add(100));
        System.out.println(cal1.sub(3));
    }

}
