import java.util.Scanner;
import java.io.File;
public class SonarSweepWind {
    public static void main(String[] args){
        int value[] = {0,0,0,0};
        int amount = 0;
        try {
            Scanner sc = new Scanner(new File("input.txt"));
            for(int i = 1; i < 3; i++){
                value[i] = sc.nextInt();
            }
            while(sc.hasNext()){
                value = nextValue(sc, value);
                if(value[0] + value[1] + value[2] < value[1] + value[2] + value[3]){
                    amount++;
                }
            }
            System.out.println(amount);
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
    private static int[] nextValue(Scanner sc, int[] value){
        //Move
        for(int i = 0; i<3; i++){
            value[i] = value[i+1];
        }
        value[3] = sc.nextInt();
        return value;
    }
}
