import javafx.collections.FXCollections;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Arrrrrray {
    public ArrayList<String> solution(String my_string) {
        ArrayList<String> answer = new ArrayList<>();
        for (int i = 0; i < my_string.length(); i++) {
            answer.add(my_string.substring(i,my_string.length()));
        }
        Collections.sort(answer);
        return answer;
    }
}
