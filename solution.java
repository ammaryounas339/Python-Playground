import java.util.Scanner;
public class solution {
    public static void main(String args[]){
        
        solution s1 = new solution();
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    int b = sc.nextInt();
       Thread t1= new Thread(new Runnable(){

        public void run() {
         
            if (a>=100 && a<=200){
                System.out.println("a in range");
            }
            else{
                System.out.println("a not in range");
            }
        
            if (b>=100 && b<=200){
                System.out.println("b in range");
            }
            else{
                System.out.println("b not in range");
            }
    }
});
t1.start();

}
}