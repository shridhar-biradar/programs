
import java.util.Arrays;



public class anagram {
    public static void main(String[] args) {
        String str1="school master";
        String str2="the classroom";
        str1=str1.replace(" ", "");
        str2=str2.replace(" ","");
        str1=str1.toLowerCase();
        str2=str2.toLowerCase();
        char ar1[]=str1.toCharArray();
        char ar2[]=str2.toCharArray();
        Arrays.sort(ar1);
        Arrays.sort(ar2);
        if(Arrays.equals(ar1,ar2)){
            System.out.println("it is anagram");
        }
        else{
            System.out.println("not anagram");
        }
    }
}
