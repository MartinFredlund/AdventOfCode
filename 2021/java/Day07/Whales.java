import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.File;
public class Whales {
    public static void main(String[] args) throws FileNotFoundException{
        Scanner sc = new Scanner(new File("input.txt"));
        String[] input = sc.nextLine().split(",");
        int[] fuel = new int[1500];
        int pos = -1;
        for(String i : input){
            for(int x = 0; x<1500; x++){
                fuel[x] += Math.abs(x-Integer.parseInt(i));
            }
        }
        int fuelUsed = fuel[0]; 
        for(int i = 1; i<1500; i++){
            if(fuelUsed > fuel[i]){
                fuelUsed = fuel[i];
                pos = i;
            }
        }
        System.out.println(pos + ": " + fuelUsed);

    }
}