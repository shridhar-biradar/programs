class  Reversing{
    public static String stringReversing(String str){
        str=str.trim();
        String words[]=str.split("\\s+");
        StringBuilder ans=new StringBuilder();
        for(int i=words.length-1;i>=0;i--){
            ans.append(words[i]);
            if(i!=0){
                ans.append(" ");
            }

        }
        return ans.toString();
    }
    public static void main(String[] args) {
        String str="          have   a   good day   ";
        String result=stringReversing(str);
        System.out.println(result);
    }
}
