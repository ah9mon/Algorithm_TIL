public class OverridingSon extends OverrridingParent{
    String react;

    public String getReact() {
        return react;
    }

    public void setReact(String react) {
        this.react = react;
    }

    public void print() {
        System.out.println(this.name + "은 " + this.location + "의 시간을 사는 중이라 전해" + this.react);
    }
}
