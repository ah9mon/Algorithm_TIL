import java.util.HashMap;

public class DataTypePract10 {
    enum CoffeeMenu{
        AMERICANO,
        ICEAMERICANO,
        CAFELATTE
    }

    static void printCoffeePrice(CoffeeMenu type) {
        HashMap<CoffeeMenu,Integer> priceMap = new HashMap<>();
        priceMap.put(CoffeeMenu.AMERICANO, 3000);
        priceMap.put(CoffeeMenu.ICEAMERICANO, 4000);
        priceMap.put(CoffeeMenu.CAFELATTE, 5000);
        int price = priceMap.get(type);
        System.out.println(String.format("가격은 %d원 입니다.", price));
    }

    public static void main(String[] args) {
        printCoffeePrice(CoffeeMenu.AMERICANO);
        printCoffeePrice(CoffeeMenu.ICEAMERICANO);
        printCoffeePrice(CoffeeMenu.CAFELATTE);


    }
}
