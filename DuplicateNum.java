class DuplicateNum{
    public static void main(String[] args) {
        int ar[]={1,2,2,3,4,4,5,7,7,8};
        int n=ar.length;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                if(ar[i]==ar[j]){
                    System.out.println(" Duplicate num is: " + ar[i]);
                }
            }
        }
    }
}