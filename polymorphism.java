class  Aeroplane{
    void takeoff(){
        System.out.println("parent aeroplane");
    }
    void fly(){
        System.out.println("Aeroplane if flying");
    }
}

class  cargoPlane extends Aeroplane{  //parent class method over ride by chaild class method
    void takeoff(){
        System.out.println("cargoplane takeoff");
    }
    void fly(){
        System.out.println("cargoplane fly");
    }
}
class  passengerplane extends Aeroplane{  // parent class method over ride by chaild class method
    void takeoff(){
        System.out.println("passengerplane takeoff");
    }
    void fly(){
        System.out.println("passwnger plane fly");
    }
 }
 class airport{
    public  void poly(Aeroplane ref){
        ref.takeoff();
        ref.fly();
        System.out.println("-----------");
    }
 }

class polymorphism{
    public static void main(String[] args) {
        cargoPlane cp=new cargoPlane();
        
        passengerplane pp=new passengerplane();
        
       airport a=new airport();
        a.poly(cp);
        a.poly(pp);
    }
}