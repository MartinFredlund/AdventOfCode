import java.util.*;
import java.io.File;

public class Dive {
    public static void main(String[] args){
        try {
            Scanner sc = new Scanner(new File("input.txt"));
            int horizon = 0;
            int depth = 0;
            while(sc.hasNext()){
                String[] nextLine = sc.nextLine().split(" ");
                switch (nextLine[0]) {
                    case "forward":
                        horizon += Integer.parseInt(nextLine[1]);
                        break;
                    case "down":
                        depth += Integer.parseInt(nextLine[1]);
                        break;
                    case "up":
                        depth -= Integer.parseInt(nextLine[1]);
                        break;
                    default:
                        break;
                }
            }
            System.out.println(horizon*depth);
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}
