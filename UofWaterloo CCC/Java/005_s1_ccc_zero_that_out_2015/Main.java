//Problem S1: Zero That Out (2015 UofWaterloo CCC)

import java.util.*;

class Main
{
  public static void main(String[] args)
  {
    int numOfInts = 0;
    List<Integer> ints = new ArrayList();
    int sumOfInts = 0;

    Scanner obj = new Scanner(System.in);

    numOfInts = Integer.parseInt(obj.nextLine());
    numOfInts = clamp(numOfInts, 0, 100);

    for(int i = 0; i < numOfInts; i++)
    {
      int currentInt = Integer.parseInt(obj.nextLine());

      if (currentInt == 0)
      {
        if(ints.size() > 0)
          ints.remove(ints.size() - 1);
      }
      else
      {
        ints.add(currentInt);
      }
    }

    for(int i = 0; i < ints.size(); i++)
    {
      sumOfInts += ints.get(i);
    }
    System.out.println(sumOfInts);
  }

  public static int clamp(int value, int minValue, int maxValue)
  {
    value = value < minValue ? minValue : value;
    value = value > maxValue ? maxValue : value;
    return value;
  }
}