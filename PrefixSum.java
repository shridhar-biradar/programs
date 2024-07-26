import java.util.*;

public class PrefixSum {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter no of rows:");
        int m=sc.nextInt();
        System.out.println("enter no of column");
        int n=sc.nextInt();

        int arr[][]=new int[m][n];
        System.out.println("enter elements of array");

        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                arr[i][j]=sc.nextInt();
            }
        }
        
        int r1,r2,c1,c2;
        System.out.println("enter value of row1 ");
        r1=sc.nextInt();
        System.out.println("enter value of col 1");
        c1=sc.nextInt();
        System.out.println("enter value of row2");
        r2=sc.nextInt();
        System.out.println("enter value of col2");
        c2=sc.nextInt();
    }
}
