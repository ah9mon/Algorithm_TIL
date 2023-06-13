import java.util.Arrays;
import java.util.HashSet;

public class DiceGame {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        HashSet<Integer> numSet = new HashSet<>(Arrays.asList(a,b,c,d));
        System.out.println(numSet);
        Integer[] numArray = numSet.toArray(new Integer[0]);
        int[] nums = {a,b,c,d};

        if (numArray.length == 1) {
            System.out.println(numArray.length);
            answer = 1111*numArray[0];
        } else if (numArray.length == 2) {
            System.out.println(numArray.length);
            int q = 0,p = 0;
            int count = 0;
            boolean flag = false;
            for (int num1:numArray) {

                // p가 할당 됐으면 q 할당
                if (p != 0) {
                    q = num1;
                    break;
                } else if (q != 0) {
                    p = num1;
                    break;
                }

                // 수가 얼마나 중복 됐는지 카운트
                for (int num2:nums) {
                    if (num1 == num2) {
                        count ++;
                    }
                }
                // 카운트가 1개 이상이면 많이 나온 수 인 p에 num1 할당
                if (count > 1) {
                    p = num1;
                } else {
                    q = num1;
                }

                if (count == 3 || count == 1) {
                    flag = true;
                }
            }
            System.out.println(p);
            System.out.println(q);
            answer = (flag) ? (int) Math.pow(10 * p + q, 2) :(p + q)*Math.abs(p - q);
        } else if (numArray.length == 4) {
            System.out.println(numArray.length);
            int minNum = 7;
            for (int num:nums) {
                if (minNum > num) minNum = num;
            }
            answer = minNum;
        } else if (numArray.length == 3) {
            System.out.println(numArray.length);
            int rlt = 1;
            for (int num1:numArray) {
                int count = 0;
                for (int num:nums) {
                    if (num1 == num) {
                        count ++;
                    }
                }
                if (count == 1) {
                    rlt *= num1;
                }
            }
            answer = rlt;

        }
        return answer;
    }
}
