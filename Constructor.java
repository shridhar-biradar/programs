class Demo{
    private int a;
    private int b;
    public Demo(int a, int b){
        this.a=a;
        this.b=b;
    }
    void disp(){
        System.out.println(a);
        System.out.println(b);
    }
}

class Constructor{
    public static void main(String[] args) {
        Demo d1=new Demo(12,34);
        d1.disp();
    }
}