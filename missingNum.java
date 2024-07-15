public class missingNum {
    public static void main(String[] args) {
        int arr[]={1,2,3,4,5,6,8};
        int n=arr.length;
        int sum_nat_num=((n+1)*(n+2))/2;
        int sum=0;
        for(int i=0;i<n;i++){
            sum+=arr[i];
        }
        int miss_ele=0;
        miss_ele=sum_nat_num-sum;
        System.out.println(miss_ele);
    }
}
