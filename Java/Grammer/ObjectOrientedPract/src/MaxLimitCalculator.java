public class MaxLimitCalculator extends Calculator{
    int getValue() {
        if (this.value > 100) {
            return 100;
        } else {
            return this.value;
        }
    }
}
