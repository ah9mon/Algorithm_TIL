interface Barkable {
    void bark();
}

//interface BarkablePredator extends Predator,Barkable {
//
//}
class Bouncer {
    void barkAnimal (Barkable animal) {
        animal.bark();
    }
}

public class Polymorphism {
    public static void main(String[] args) {
        Tiger tiger = new Tiger();
        Lion lion = new Lion();

        Bouncer bouncer = new Bouncer();
        bouncer.barkAnimal(tiger);
        bouncer.barkAnimal(lion);
    }
}
