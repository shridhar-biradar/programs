
import java.util.Arrays;


public class selectionSort {

   public static void SelectionSorting(int arr[]){
    for(int i=0;i<arr.length;i++){
        int min_idx=i;
        for(int j=i+1;j<arr.length;j++){
            if(arr[j]<arr[min_idx]){
                min_idx=j;
            }
        }
        if(min_idx!=i ){
            int temp=arr[min_idx];
            arr[min_idx]=arr[i];
            arr[i]=temp;
        }
    }
}
 
   
    
    public static void main(String[] args) {
    int arr[]={20,10,15,40,30,50,1};
    SelectionSorting(arr);
    System.out.println(Arrays.toString(arr));
    }
}

