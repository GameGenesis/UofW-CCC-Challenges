import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    private static ArrayList<Integer> villages = new ArrayList<Integer>();
    private static int villageNum;
    private static Scanner input;
    private static float smallestSize = Float.MAX_VALUE;

    public static void main(String[] args) {
        input = new Scanner(System.in);
        villageNum = getIntInput();

        storeVillagesPos();
        getSmallestSize();

        System.out.println(smallestSize);
      }

    private static int getIntInput() {
        return input.nextInt();
      }

    private static void storeVillagesPos() {
        for(int i = 0; i < villageNum; i++) {
            villages.add(input.nextInt());
        }

        Collections.sort(villages);
      }

    private static void getSmallestSize() {
        float sizeLeft = 0f;
        float sizeRight = 0f;
        float size = 0f;

        for(int i = 1; i < villageNum - 1; i++) {
            sizeLeft = villages.get(i) - villages.get(i-1);
            sizeRight = villages.get(i+1) - villages.get(i);
            size = (sizeLeft + sizeRight) / 2f;
            smallestSize = Math.min(size, smallestSize);
        }
        
        smallestSize = round(smallestSize, 1);
      }

    private static float round(float value, int precision) {
        int scale = (int) Math.pow(10, precision);
        return (float) Math.round(value * scale) / scale;
      }
}