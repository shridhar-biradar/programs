public class factorial1 {
    
    public static int facto(int n){
        if(n==1 || n==0){
            return 1;
        }
        else
        return n*facto(n-1);
    }
    public static void main(String[] args) {
        int n=4;
        System.out.println(facto(n));
    }
}
