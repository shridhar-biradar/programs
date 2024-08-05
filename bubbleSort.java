
import java.util.Scanner;

class bubbleSort{
    public static void arraySorting(int[] arr){
        for(int i=0;i<arr.length;i++){
            for(int j=i+1;j<arr.length;j++){
                if(arr[i]>arr[j]){
                    int temp= arr[i];
                    arr[i]=arr[j];
                    arr[j]=temp;
                }
            }
        }
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
    }
    public static void main(String[] args) {
    Scanner sc=new Scanner(System.in);
        System.out.println("enter array size:           ");
        int n=sc.nextInt();
        int[] arr=new int[n];
        System.out.println("enter element of array:");
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        System.out.println(" elements of array are:");
        arraySorting(arr);
    }
}
