public class Vowels {
    public static void main(String[] args) {
        String s1="hello";
        int vowel=0;
        int consonent=0;
        for(int k=0;k<s1.length();k++){
            char c=s1.charAt(k);
            if(c=='a'|| c=='e' || c=='i' || c=='o' || c=='u'){
                vowel++;
            }
            else
             consonent++;
        }
        System.out.println(" number of vowels are:" + vowel);
        System.out.println("number of consonents are: " + consonent);
    }
}
