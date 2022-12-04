package Day1;
import java.util.Arrays;
import java.util.Scanner;
import java.io.File;
public class CalorieCountingTop3{
    public static void main(String[] args){
        int amountCal[] = {0,0,0};
        try {
            Scanner sc = new Scanner(new File("input.txt"));
            String line = null;
            int tempCal = 0;
            while(sc.hasNext()){
                if(!(line = sc.nextLine()).isEmpty()){
                    tempCal += Integer.parseInt(line);
                }
                else{
                    for(int k = 0; k < amountCal.length; k++){
                        if(tempCal>amountCal[k]){
                            amountCal[k] = tempCal;
                            k = amountCal.length;
                            Arrays.sort(amountCal);
                        }
                    }

                    tempCal = 0;
                }
            }
            System.out.println(amountCal[0] + amountCal[1] + amountCal[2]);
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}
