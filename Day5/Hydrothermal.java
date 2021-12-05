import java.util.*;
import java.awt.Point;
import java.io.File;
import java.io.FileNotFoundException;
public class Hydrothermal {
    public static void main(String[] args) throws FileNotFoundException{
        Scanner sc = new Scanner(new File("input.txt"));
        ArrayList<Point[]> input = new ArrayList<>();
        int[][] result = new int[1000][1000];
        while(sc.hasNextLine()){
            String[] nextLine = sc.nextLine().replace(" -> ", ",").split(",");
            Point[] cord = {new Point(Integer.parseInt(nextLine[0]), Integer.parseInt(nextLine[1])), new Point(Integer.parseInt(nextLine[2]), Integer.parseInt(nextLine[3]))};
            input.add(cord);
        }
        for(Point[] pair: input){
            if(pair[0].x == pair[1].x){
                for(int i = Math.min(pair[0].y, pair[1].y); i < Math.max(pair[0].y, pair[1].y)+1; i++){
                    result[pair[0].x][i]++;
                }
            }
            if(pair[0].y == pair[1].y){
                for(int i = Math.min(pair[0].x, pair[1].x); i < Math.max(pair[0].x, pair[1].x)+1; i++){
                    result[i][pair[0].y]++;
                }
            }
        }
        int sum = 0;
        for(int i = 0; i < result.length; i++){
            for(int z = 0; z < result[i].length; z++){
                if(result[i][z] > 1){
                    sum++;
                }
            }
        }
        
        System.out.println(sum);
    }
}
 