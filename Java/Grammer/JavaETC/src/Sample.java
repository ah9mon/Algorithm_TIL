import house.*;
import house.person.*;
// 패키지가 다르면 클래스명이 같아도 됨
public class Sample {
    public static void main(String[] args) {
        HouseKim kim = new HouseKim();
        System.out.println(kim.lastname);
        EungYongPark park = new EungYongPark();
    }
}
