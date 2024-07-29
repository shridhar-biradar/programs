public class insertionSort {
    public static void insertionSorting(int[] arr){
        for(int i=1;i<arr.length;i++){
            int j=i;
            while(j>0 && arr[j]<arr[j-1]){
                int temp=arr[j];
                arr[j]=arr[j-1];
                arr[j-1]=temp;
                j--;
            }
        }
      
    }
 public static void main(String[] args) {
    int[] arr={30,10,20,90,50,60};
    System.out.println("array after insertion sort:");
    insertionSorting(arr);
    for(int i=0;i<arr.length;i++){
        System.out.println(arr[j]);
    }
 }   
}
