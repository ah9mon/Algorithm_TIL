public class FinalTest {
    public static void main(String[] args) {
        final int value = 2;
        final Person person = new Person();
        person.setAge(20);
        person.setName("엄한결");

        System.out.println("value = " + value);
        System.out.println("person_1 = " + person.getName() + " age = " + person.getAge());

//        value = 2; // 컴파일 에러
        person.setAge(10);
        person.setName("최예훈");

        System.out.println("person_2 = " + person.getName() + " age = " + person.getAge());

        final Maxican person2 = new Maxican();
        person2.setName("한결");
        person2.setAge(27);
        person2.speech();
    }
}

