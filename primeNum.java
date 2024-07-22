public class primeNum {
    public static boolean isPrime(int n){
        if(n==0 || n==1){
            return false;
        }
        if(n==2){
            return  true;
        }
        for(int i=2;i<n;i++){
            if(n%2==0){
                return false;
            }
            
        } return true;
    }

    public static void main(String[] args) {
        int n=24;
        System.out.println(isPrime(n));
    }
}
