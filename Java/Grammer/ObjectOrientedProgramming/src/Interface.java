//interface Predator {
//    String getFood();
//}

abstract class Predator extends Animal {
    abstract String getFood();

    void printFood() {
        System.out.printf("my food is %s\n", getFood());
    }

    static int LEG_COUNT = 4;
    static int speed() {
        return LEG_COUNT * 30;

    }
}

class Tiger extends Predator implements Barkable {
    public void bark() {
        System.out.println("어흥");
    }
    public String getFood() {
        return "apple";
    }
}

class Lion extends Predator implements Barkable{
    public void bark() {
        System.out.println("으르렁");
    }

    public String getFood() {
        return "banana";
    }
}

class ZooKeeper extends Animal {
    void feed(Predator predator) {
        System.out.println("feed " + predator.getFood());
    }

//    void feed(Lion lion) {
//        System.out.println("feed banana");
//    }

}
public class Interface {
    public static void main(String[] args) {
        ZooKeeper me = new ZooKeeper();
        Tiger tiger = new Tiger();
        Lion lion = new Lion();
        me.feed(tiger);
        me.feed(lion);
    }

}
