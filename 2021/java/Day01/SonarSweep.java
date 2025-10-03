import java.util.Scanner;
import java.io.File;
public class SonarSweep{
    public static void main(String[] args){
        int lastValue;
        int amount = 0;
        try {
            Scanner sc = new Scanner(new File("input.txt"));
            lastValue = sc.nextInt();
            int newValue;
            while(sc.hasNext()){
                newValue = sc.nextInt();
                if(newValue>lastValue){
                    amount++;
                }
                lastValue = newValue;
            }
            System.out.println(amount);
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}