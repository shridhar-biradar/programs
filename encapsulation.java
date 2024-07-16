class Student{
    private int age;
    private String name;

    void setAge(int age){
        this.age=age;
    }
    void setName(String name){
        this.name=name;
    }
    int getAge(){
        return age;
    }
    String getName(){
        return name;
    }
}

public class encapsulation {

    public static void main(String[] args) {
       Student obj=new Student();
       obj.setAge(23);
       obj.setName("Shridhar");
       System.out.println(obj.getAge());
       System.out.println(obj.getName());

    }
}