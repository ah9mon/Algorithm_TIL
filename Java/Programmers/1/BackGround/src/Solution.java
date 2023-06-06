class Solution {
    public int[] solution(String[] wallpaper) {
        int[] answer = new int[4];
        int minCol = 50;
        int minRow = 50;
        int maxCol = 0;
        int maxRow = 0;
        for (int i = 0; i < wallpaper.length; i++) {
            for (int j = 0; j < wallpaper[i].length(); j++) {
                if (wallpaper[i].charAt(j) == '#') {
                    if (minCol > j) minCol = j;
                    if (maxCol < j) maxCol = j;
                    if (minRow > i) minRow = i;
                    if (maxRow < i) maxRow = i;
                }
            }
        }
        answer[0] = minRow;
        answer[1] = minCol;
        answer[2] = maxRow+1;
        answer[3] = maxCol+1;
        return answer;
    }
}
