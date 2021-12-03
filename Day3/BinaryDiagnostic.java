import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;

public class BinaryDiagnostic {

    public static void main(String[] args) throws FileNotFoundException{
        Scanner sc = new Scanner(new File("input.txt"));
        int[] input = {0,0,0,0,0,0,0,0,0,0,0,0};
        while(sc.hasNextLine()){
            String b= sc.next();
            for(int i = 0; i < 12; i++){
                if(b.charAt(i) == '1'){
                    input[i]++;
                }
                else{
                    input[i]--;
                }
            }
        }
        int binaryPos = 1;
        int gamma = 0;
        int epsilon = 0;
        for(int i = 11; i >= 0; i--){
            if(input[i] >= 0){
                gamma += binaryPos;
            }
            else{
                epsilon += binaryPos;
            }
            binaryPos = binaryPos * 2;
        }
        System.out.println(gamma * epsilon);
    }
}