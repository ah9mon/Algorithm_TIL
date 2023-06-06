import java.util.HashMap;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        // 등수 - 선수 형태로 hashmap 생성
        HashMap<Integer, String> playerRanking = PlayerRanking(players);

        // 선수 - 등수 형태로 hashmap 생성
        HashMap<String, Integer> mappedPlayer = MappedPlayer(players);

        // 선수가 언급 될 때마다 등수 변경
        for (String name:callings) {
            ChangeRank(playerRanking,mappedPlayer, name);
        }

        // 랭크순으로된 선수 명단 반환
        return Rank(playerRanking, players);
    }

    private static HashMap<String,Integer> MappedPlayer(String[] players) {
        HashMap<String, Integer> map = new HashMap<>();
        for (int i = 0; i < players.length; i++) {
            map.put(players[i], i);
        }
        return map;
    }

    private static HashMap<Integer, String> PlayerRanking (String[] players) {
        HashMap<Integer, String> map = new HashMap<>();
        for (int i = 0; i < players.length; i++) {
            map.put(i, players[i]);
        }
        return map;
    }

    private static void ChangeRank ( HashMap<Integer, String> playerRanking,HashMap<String,Integer> mappedPlayer,String name ) {
        int rank = mappedPlayer.get(name);
        // 앞에 있는 선수 등수 뒤로 밀기
        mappedPlayer.replace(playerRanking.get(rank-1), rank);
        playerRanking.replace(rank, playerRanking.get(rank-1));
        // 불린 선수 등수 앞으로 땡기기
        mappedPlayer.replace(name, rank -1);
        playerRanking.replace(rank-1, name);
    }

    private static String[] Rank(HashMap<Integer, String> playerRanking, String[] players) {
        String[] answer = new String[players.length];
        for (int i=0; i < players.length; i++) {
            answer[i] = playerRanking.get(i);
        }
        return answer;
    }


}
