import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;
public class BingoLastCard {
    public static void main(String[] args) throws FileNotFoundException{
        Scanner sc = new Scanner(new File("input.txt"));
        String[] rNumbers = sc.nextLine().split(",");

        ArrayList<String[][]> boards = new ArrayList();
        while(sc.hasNext()){
            sc.nextLine();
            String[][] newBoard = new String[5][5];
            for(int i = 0; i < 5; i++){
                String after = sc.nextLine().trim().replaceAll(" +", " ");
                newBoard[i] = after.split(" ");
            }
            boards.add(newBoard);
        }
        ArrayList<String[][]> newBoards = new ArrayList();
        for(int i = 0; i < rNumbers.length; i++){

            System.out.println("rNumber" + i);
            for(int z = 0; z < boards.size(); z++){

                String[][] board = boards.get(z);
                Boolean found = false; 
                for(int x = 0; x < 5; x++){
                    for(int y = 0; y < 5; y++){

                        if(board[x][y].equals(rNumbers[i])){
                            board[x][y] = "x";
                            boards.set(z, board);
                            check(newBoards, boards, board, x, y, rNumbers[i]);
                            found = true;
                            for(int q = 0; q < 5; q++){
                                for(int e = 0; e < 5; e++){
                                    System.out.print(board[q][e] + " ");
                                }
                                System.out.println("");
                            }
                            System.out.println("------------------");
                        }
                    }
                }
                if(!found){
                    newBoards.add(board);
                }
            }
            boards.clear();
            boards.addAll(newBoards);
            newBoards.clear();
        }
    }
    private static void check(ArrayList<String[][]> newBoards, ArrayList<String[][]> boards, String[][] board, int x, int y, String nbr){
        int amountX = 0;
        int amountY = 0;
        for(int i = 0; i < 5; i++){
            if(board[x][i].equals("x")){
                amountX ++;
            }
            if(board[i][y].equals("x")){
                amountY ++;
            }
        }
        if(amountX == 5 || amountY == 5){
            if(boards.size() == 1){
                int boardSum = 0;
                for(int i = 0; i < 5; i++){
                    for(int z = 0; z < 5; z++){
                        if(!board[i][z].equals("x")){
                            boardSum += Integer.parseInt(board[i][z]);
                        }
                    }
                }
                System.out.println(boardSum * Integer.parseInt(nbr));
                System.exit(0);
            }
        }else{
            newBoards.add(board);
        }
    }
}
