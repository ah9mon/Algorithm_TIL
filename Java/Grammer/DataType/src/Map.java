
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Map {
    public static void main(String[] args) {
        HashMap<String,String> map = new HashMap<>();
        map.put("people", "사람");
        map.put("baseball", "야구");
        System.out.println(map.get("people"));
        System.out.println(map.get("baseball"));
        System.out.println(map.get("women"));
        System.out.println(map.getOrDefault("java", "자바"));
        System.out.println(map.containsKey("java"));
        System.out.println(map.containsKey("people"));
        System.out.println(map.containsKey("men"));
        System.out.println(map.remove("people"));
        System.out.println(map.size());
        map.put("bigfather", "대부");
        System.out.println(map.keySet());
        List<String> keyList = new ArrayList<>(map.keySet());
        System.out.println(keyList);
    }
}
