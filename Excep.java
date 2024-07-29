public class Excep {
    public static void main(String[] args) {
        int a=6;
        int b=0;
        int result=0;
        try{
             result=a/b;
        }
        catch(Exception e){
            System.out.println(" cannot divisible by zero "+ e);
        }
        System.out.println(result);
        
    }
}
