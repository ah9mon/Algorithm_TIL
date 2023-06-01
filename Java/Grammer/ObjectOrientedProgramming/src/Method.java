public class Method {
    int sum(int a, int b) {
        return a+b;
    }

    public static void main(String[] args) {
        int a = 3;
        int b= 4;
        Method method = new Method();
        int c = method.sum(a,b);
        System.out.println(c);
    }
}
