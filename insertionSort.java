
import java.util.Arrays;

class insertionSort{
    public static void insertionSorting(int arr[])
    {
        int j;
        for(int i=1;i<arr.length;i++){
            j=i;
            while(j>0 && arr[j]<arr[j-1] ){
                int temp=arr[j];
                arr[j]=arr[j-1];
                arr[j-1]=temp;
                j--;
            }
        }
    }
    
    public static void main(String[] args) {
      int arr[]={80,10,50,20,9};
      insertionSorting(arr);
      System.out.println("array after insertion sort is"); 
      System.out.println(Arrays.toString(arr)); 
    }
}