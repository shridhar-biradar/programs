import java.util.Scanner;
public class lowerBound {
    public static int FindLowerBound(int arr[],int target){
        int low=0,high=arr.length;
        int result=-1;
        while(low<=high){
            int mid=low+(high-low)/2;
            if(arr[mid]==target){
                result=mid;
                high=mid-1;
            }
            else if(arr[mid]>target){
                high=mid-1;
            }
            else{
                low=mid+1;
            }
        }
        return  result;
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter size of array element:");
        int n=sc.nextInt();
        int arr[]=new int[n];
        System.out.println("enter the array elements:");
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        System.out.println("enter the target element:");
        int target=sc.nextInt();
        
        int result=FindLowerBound(arr,target);

        if(result==-1){
            System.out.println("elements not found in array");
        }
        else{
            System.out.println("element found in array at index :" + result);
        }
    }
}
