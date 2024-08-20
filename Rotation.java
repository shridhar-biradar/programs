
public class Rotation {
    
        public static void main(String[] args) {
        

            int arr[][]={
                {1,2,3},
                {3,4,5},
                {6,7,8}
            };
            
              int i;     
              int m=arr.length;
              int n=arr[0].length;
              System.out.println(" transpoce matrix  values");
              for( i=0; i<m;i++){
                for(int j=i;j<n;j++){
                    System.out.print(arr[j][i] + " ");
                }
                System.out.println(" ");
              }

              
        }             
    
}
