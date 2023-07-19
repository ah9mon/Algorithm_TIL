public class Overloading {
    public static void main(String[] args) {
        overloading(1);
        overloading(1,2);
        overloading();
        overloading("Hi");
    }

    static void overloading(int n) {
        System.out.println(n);
    }
    static void overloading(int n, int m) {
        System.out.println(n + m);
    }

    static void overloading() {
        System.out.println("매개변수 없음");
    }

    static void overloading(String word) {
        System.out.println(word);
    }
}
