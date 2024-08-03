
import java.util.Scanner;

public class binarySearch {
    public static int findElement(int arr[],int target){
        int low=0,high=arr.length;
        while(low<=high){
            int mid=low+(high-low)/2;
            if(arr[mid]== target){
                return  mid;
            }
            else if(arr[mid]<target){
                low=mid+1;
            }
            else{
                high=mid-1;
            }
            
        }
        return  0;
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the size of array: ");
        int n=sc.nextInt();
        int arr[]=new int[n];
        System.out.println("enter elements of array:");
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }

        System.out.println("enter target element:");
        int target=sc.nextInt();
        int result=findElement(arr,target);
        // char[] resu;
        
        System.out.println(" element present at index :"+result);
    }
}
