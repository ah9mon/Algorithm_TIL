class HouseDog extends Dog {
    // 생성자 규칙
    // 1. 클래스명과 메서드명이 동일
    // 2. 리턴타입을 정의하지 않는다 (void도 사용하지 않음)
    HouseDog(String name) {
        this.setName(name);
    }
    // 생성자 오버로딩
    HouseDog(int type) {
        if (type==1) {
            this.setName("yorkshire");
        } else if (type == 2) {
            this.setName("bulldog");
        }
    }
    void sleep(){
        System.out.println(this.name + "zzz in house");
    }

    void sleep(int hour) {
        System.out.println(this.name + "zzz in house for" + hour + "hour");
    }
}

public class Constructor {
    public static void main(String[] args) {
        HouseDog dog = new HouseDog("honni");
//        dog.setName("훈이");
        System.out.println(dog.name);
        HouseDog dog2 = new HouseDog(1);
        System.out.println(dog2.name);
    }
}
