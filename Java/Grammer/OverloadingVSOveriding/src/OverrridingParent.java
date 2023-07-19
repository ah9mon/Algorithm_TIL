public class OverrridingParent {

    String location;
    String name;

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void print() {
        System.out.println(this.name + "은 " + this.location + "의 시간을 사는 중이라 전해");
    }
}
