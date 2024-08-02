
public class pallindrome {

public static void main(String[] args) {
    String s1="hello";
    String s2="";
    int n=s1.length();
    for(int i=0; i<n;i++){
        s2= s1.charAt(i)+s2;
    }
    if(s2.equals(s1))
    {
        System.out.println("it is pallindrome");
    }
    else
    System.out.println(" not pallindrome  ");
 }
    
}