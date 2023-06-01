public class MineralCalculator {
    int value = 0;

    public void add(Mineral mineral) {
        this.value += mineral.getPrice();
    }

    public int getValue() {
        return this.value;
    }
}
