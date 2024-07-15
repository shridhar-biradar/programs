public class reverseString {
    public static void main(String[] args) {
        String s1=" hello";
        String s2="";
        int n= s1.length();
        for(int i=n-1;i>0;i--){
            s2=s2 + s1.charAt(i);
        }
        System.out.println(s2);
    }

}
