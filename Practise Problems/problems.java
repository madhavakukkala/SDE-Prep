
import java.util.Scanner;

class allproblems {
    Scanner sc = new Scanner(System.in);

    // Find even or Odd
    public void evenorodd() {

        System.out.print("Enter number: ");
        int n = sc.nextInt();

        if (n % 2 == 0)
            System.out.println(n + " is Even.");
        else
            System.out.println(n + "Odd.");

    }

    // Find largest of 3 numbers
    public void Largest0f3() {

        System.out.print("Enter 3 numbers: ");
        int n = sc.nextInt();
        int o = sc.nextInt();
        int p = sc.nextInt();

        if (n > o && n > p)
            System.out.println(n);
        else if (o > p && o > n)
            System.out.println(o);
        else if (p > n && p > o)
            System.out.println(p);

    }

    // Check Leap year
    public void leapyear() {

        System.out.print("Enter year: ");
        int n = sc.nextInt();
        if (n % 4 == 0) {
            if (n % 100 != 0)
                System.out.println("Yes! Its a leap year");
            else {
                if (n % 400 == 0)
                    System.out.println("Yes , Its a leap year");
                else
                    System.out.println("Not a leap year");
            }
        } else
            System.out.println("not a leap year");
    }


    // Perfect Square Check
    public void perfect_square() {

        System.out.print("Enter number : ");
        int n = sc.nextInt();
        boolean isperfectsquare = false;
        for (int i = 1; i*i <= n; i++)
        {
            if (i*i == n) 
            {
                isperfectsquare = true;
                break;
            }

        }

        if (isperfectsquare)
            System.out.println("Perfect Square");
        else
            System.out.println("Not a Perfect Square");
    }


    // Prime number Check
    public void Primenumber_check()
    {
        System.out.println("Enter number: ");
        int n = sc.nextInt();
        boolean isprime = true;
        for (int i=2;i<n;i++)
        {
            if (n%i == 0)
            {
                isprime = false;
                break;
            }
            
        }
        if (isprime)
            System.out.println("Its a primenumber");
        else
            System.out.println("Not a primenumber");

    }


    //Palindrome Number Check
    public void palindrome()
    {
        System.out.println("Enter number: ");
        int n = sc.nextInt();
        int temp = n;
        int reverse = 0;
        while (n>0)
        {
            int digit = n%10;
            reverse = reverse * 10 + digit;
            n=n/10;
        }
        if ( temp == reverse)
            System.out.println("Palindrome");
        else
            System.out.println("Not a Palindrome");
    }
    

    // Finding second largest element of an array
    public void getSecondLargest(int[] arr) {
        // code here
        int largest = arr[0];
        int second_largest = -1;
        for (int i=1; i<arr.length; i++)
        {
            if (arr[i]>largest)
            {
                second_largest = largest;
                largest = arr[i];
            }
            else if (arr[i] < largest)
            {
                second_largest = arr[i]
            }
        }
    }

}

public class problems {

    public static void main(String[] args) {
        allproblems obj = new allproblems();
        // obj.evenorodd();
        // obj.Largest0f3();
        // obj.leapyear();
        // obj.perfect_square();
        // obj.Primenumber_check();
        // obj.palindrome();
        
        obj.sc.close();
    }
}
