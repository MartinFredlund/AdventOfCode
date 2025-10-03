import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;
public class Lanternfish {
    final static int NBRDAY = 80;
    public static void main(String[] args) throws FileNotFoundException{
        int[] amountLatern = new int[9];
        Scanner sc = new Scanner(new File("input.txt"));
        String[] input = sc.nextLine().split(",");
        for(int i = 0; i < input.length; i++){
            amountLatern[Integer.parseInt(input[i])] ++;
        }
        for(int i = 0; i< NBRDAY; i ++){
            int[] newAmount = new int[9];
            for(int x = 0; x < amountLatern.length; x++){
                if(x == 0){
                    newAmount[6] += amountLatern[0];
                    newAmount[8] += amountLatern[0];
                }else{
                    newAmount[x-1] += amountLatern[x];
                }
            }
            amountLatern = newAmount;
        }
        int result = 0;
        for(int nbr : amountLatern){
            result += nbr;
        }
        System.out.println(result);
    }
}
