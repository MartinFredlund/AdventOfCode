package Day1;
import java.util.Scanner;
import java.io.File;
public class CalorieCounting{
    public static void main(String[] args){
        int amountCal = 0;
        try {
            Scanner sc = new Scanner(new File("input.txt"));
            String line = null;
            int tempCal = 0;
            while(sc.hasNext()){
                if(!(line = sc.nextLine()).isEmpty()){
                    tempCal += Integer.parseInt(line);
                }
                else{
                    if(tempCal>amountCal){
                        amountCal = tempCal;
                    }
                    tempCal = 0;
                }
            }
            System.out.println(amountCal);
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}
