interface  A{
     void show();
}
class B implements  A{
    public void show()
    {
        System.out.println(" Interface is  implimented in class B");
    }
 }

public class  interface123{
    public static void main(String[] args){
        B obj=new B();
        obj.show();

       
    }
}