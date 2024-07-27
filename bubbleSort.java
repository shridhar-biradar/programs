
import java.util.Scanner;

public class bubbleSort {

    public static int arraySorting(int[] arr){
        // int n;
        for(int i=0;i<arr.length;i++){
            for(int j=i+1;j<arr.length;j++){
                if(arr[i]>arr[j]){
                    int temp=arr[i];
                    arr[i]=arr[j];
                    arr[j]=temp;
                }
            }
        }
        for(int i=0;i<arr.length;i++){
        System.out.print(arr[i]+" ");
    }
    return  0;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter length of arr:");
        int n=sc.nextInt();
        int[] arr=new int[n];
        System.out.println("enter element of arr:");
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        // System.out.println(arraySorting(arr));
        System.out.println("sorted array is :");
        arraySorting(arr);
        // for(int i=0;i<n;i++){
        // System.out.println(arraySorting(arr));
        // }
    }
}
