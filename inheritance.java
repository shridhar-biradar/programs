class human{
    int age;
    void sleep(){
        age=22;
        System.out.println("human nead good  sleep");
        System.out.println(age);
    }
}
class student extends human{

}

public class inheritance {
    public static void main(String[] args) {
        student  s1=new student();
        s1.sleep();
    }
}
