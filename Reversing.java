
// import java.lang.reflect.AnnotatedArrayType;

class  Reversing{
    public static String reversingString(String str){
        str=str.trim();
        String word[]=str.split("\\s+");
        StringBuilder ans=new StringBuilder();
        for(int i=word.length-1;i>=0;i--){
            ans.append(word[i]);
            if(i!=0){
                ans.append(" ");
            }
        }
        return ans.toString();
    }
    public static void main(String[] args) {
       String str="  have    a   nice     day   ";
       String result=reversingString(str);
       System.out.println(result);
    }
}
