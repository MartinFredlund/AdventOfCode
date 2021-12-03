import java.util.*;
import jdk.jshell.spi.ExecutionControl.ResolutionException;
import java.io.File;
import java.io.FileNotFoundException;

public class LifeSupportRating {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(new File("input.txt"));
        ArrayList oxygen = new ArrayList<String>();
        ArrayList co2 = new ArrayList<String>();
        while(sc.hasNextLine()){
            String temp = sc.nextLine();
            if(temp.charAt(0) == '1'){
                oxygen.add(temp);
            }else{
                co2.add(temp);
            }
        }
        if(!(oxygen.size() > co2.size())){
            ArrayList temp = oxygen;
            oxygen = co2;
            co2 = temp;
        }
        System.out.println(value(oxygen, true)* value(co2, false));
    }

    private static int value(ArrayList<String> input, Boolean mostCommon){
        int pos = 1;
        ArrayList listWithOne = new ArrayList<String>();
        ArrayList listWithZero = new ArrayList<String>();
        while(input.size() != 1){
            for (String line : input) {
                if(line.charAt(pos) == '1'){
                    listWithOne.add(line);
                }
                else{
                    listWithZero.add(line);
                }
            }
            input.clear();
            if(mostCommon){
                if(listWithOne.size() >= listWithZero.size()){
                    input.addAll(listWithOne);
                }
                else{
                    input.addAll(listWithZero);
                }
            }else{
                if(listWithOne.size() < listWithZero.size()){
                    input.addAll(listWithOne);
                }
                else{
                    input.addAll(listWithZero);
                }
            }
            listWithOne.clear();
            listWithZero.clear();
            pos++;
        }
        int result = 0;
        int binaryPos = 1; 
        for(int i = 11; i >= 0; i--){
            if(input.get(0).charAt(i) == '1'){
                result += binaryPos;
            }
            binaryPos = binaryPos * 2;
        }
        return result;
    }
}
