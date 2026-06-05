
import java.util.ArrayList;
import java.util.List;
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
        for (int i = 1; i * i <= n; i++) {
            if (i * i == n) {
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
    public void Primenumber_check() {
        System.out.println("Enter number: ");
        int n = sc.nextInt();
        boolean isprime = true;
        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                isprime = false;
                break;
            }

        }
        if (isprime)
            System.out.println("Its a primenumber");
        else
            System.out.println("Not a primenumber");

    }

    // Palindrome Number Check
    public void palindrome() {
        System.out.println("Enter number: ");
        int n = sc.nextInt();
        int temp = n;
        int reverse = 0;
        while (n > 0) {
            int digit = n % 10;
            reverse = reverse * 10 + digit;
            n = n / 10;
        }
        if (temp == reverse)
            System.out.println("Palindrome");
        else
            System.out.println("Not a Palindrome");
    }

    // Finding second largest element of an array
    public void getSecondLargest() {
        // code here
        System.out.print("Length of Array: ");
        int length = sc.nextInt();
        int[] arr = new int[length];
        System.out.print("Enter " + length + " elements: ");
        for (int i = 0; i < length; i++)
            arr[i] = sc.nextInt();

        int largest = arr[0];
        int second_largest = -1;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > largest) {
                second_largest = largest;
                largest = arr[i];
            } else if (arr[i] < largest && arr[i] > second_largest) {
                second_largest = arr[i];
            }
        }
        System.out.println(second_largest);
    }

    // Armstrong Number Check
    public void Armstrong() {
        System.out.println("Enter number: ");
        int n = sc.nextInt();
        int temp = n;
        int temp1 = n;
        int count = 0;
        int digit;
        int sum = 0;
        while (n > 0) {
            digit = n % 10;
            count++;
            n = n / 10;
        }
        while (temp > 0) {
            digit = temp % 10;
            sum = sum + (int) Math.pow(digit, count);
            temp = temp / 10;

        }
        if (temp1 == sum)
            System.out.println("Armstrong " + sum);
        else
            System.out.println("Not an Armstrong " + sum);
    }

    // Strong Numbers are the numbers whose sum of factorial of digits is equal to
    // the original number. Given a number, the task is to check if it is a Strong
    // Number or not.
    public void Strongnumber() {
        System.out.print("Enter number: ");
        int n = sc.nextInt();
        int original = n;
        int sum = 0;
        while (n > 0) {
            int factorial = 1;
            int digit = n % 10;
            for (int i = 1; i <= digit; i++) {
                factorial = factorial * i;
            }
            sum += factorial;
            n = n / 10;
        }
        if (original == sum)
            System.out.println("Strong number " + sum);
        else
            System.out.println("Not a Strong Number" + sum);
    }

    // Check Perfect number
    public void checkPerfectNumber() {

        System.out.print("Enter number: ");
        int num = sc.nextInt();
        int divisor = 0;
        int sum = 0;
        for (int i = 1; i < num; i++) {
            if (num % i == 0) {
                divisor = i;
                sum = sum + divisor;

            }
        }
        if (num == sum)
            System.out.println(true);

        else
            System.out.println(false);
    }

    // leetcode problem
    public void suubarray_sum() {
        int[] arr = { 2, 3, -8, 7, -1, 2, 3 };
        int n = arr.length;
        int sum = 0;
        int max = Integer.MIN_VALUE;

        for (int i = 0; i < n; i++) {
            sum = sum + arr[i];

            if (sum > max) {
                max = sum;
            }

            if (sum < 0) {
                sum = 0;
            }
        }

        System.out.println(max);
    }

    // Check if Number is Composite
    public void compositenumber() {
        System.out.print("Enter number: ");
        int n = sc.nextInt();
        boolean is_composite = false;
        if (n <= 1)
            System.out.println("1 is neither composite nor prime");
        else {
            for (int i = 2; i * i < n; i++) {
                if (n % i == 0) {
                    System.out.println("Yes Composite");
                    is_composite = true;
                    break;
                }
            }
            if (is_composite == false)
                System.out.println("Its prime");
        }
    }

    // print composite
    public List<Integer> compositeNumberPrint() {
        System.out.print("Enter number: ");
        int n = sc.nextInt();

        List<Integer> ans = new ArrayList<>();

        for (int i = 4; i <= n; i++) {
            boolean isComposite = false;

            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    isComposite = true;
                    break;
                }
            }

            if (isComposite) {
                ans.add(i);
            }
        }

        return ans;
    }

    // Multiplicateion table
    public void Multiplication_table() {
        System.out.print("Enter number for table: ");
        int n = sc.nextInt();
        for (int i = 1; i <= 10; i++) {
            System.out.println(n + " x " + i + " = " + (n * i));
        }

    }

    // first N odd numbers numbers

    public void N_numbers() {
        System.out.print("Enter number : ");
        int n = sc.nextInt();
        int sum = 0;
        // int num = 0;
        for (int i = 0; i <= n; i++) {
            sum += (2 * i + 1);
        }
        System.out.println("sum: " + sum);
    }

    // Power of a Number (a^b)
    public void powerofnumber() {
        System.out.print("Enter number : ");
        int n = sc.nextInt();
        System.out.print("Enter power : ");
        int p = sc.nextInt();
        int power = (int) Math.pow(n, p);
        System.out.println("Power of (" + n + "^" + p + ") = " + power);

    }

    public void Fibonacci() {
        System.out.print("Enter number : ");
        int n = sc.nextInt();
        int a = 0;
        int b = 1;
        int c = 0;
        // int sum =0;
        if (n <= 1)
            System.out.println(1);
        else {
            for (int i = 2; i <= n; i++) {
                c = a + b;
                a = b;
                b = c;

                // sum += c;
                // System.out.println(c);
            }
            System.out.println(c);
        }

    }

    // second largest factor of a number
    public void secondlargest() {
        System.out.print("Enter number : ");
        int n = sc.nextInt();
        int found = 0;
        int paired_factor = 0;
        for (int i = 2; i * i < n; i++) {
            if (n % i == 0) {
                paired_factor = (int) n / i;
                System.out.println(paired_factor);
                found++;

                if (found == 2) {
                    // System.out.println(paired_factor);
                    // break;
                }
            }
        }
    }

    // Fibonacci till Limit
    public void Fibonacci_tillN() {
        System.out.print("Enter number : ");
        int n = sc.nextInt();
        int a = 0;
        int b = 1;
        int c = 0;

        while (a < n) {
            System.out.print(a + " ");
            c = a + b;
            a = b;
            b = c;

        }

    }

    // Count Digits in a Number
    public void Count_digits() {
        System.out.println("Enter number: ");
        int n = sc.nextInt();
        int count = 0;
        int digit = 0;
        while (n > 0) {
            digit = n % 10;
            count++;
            n = n / 10;
        }
        System.out.println("Number of Digits : " + count);

    }

    // Sum Digits in a Number
    public void Sum_digits() {
        System.out.println("Enter number: ");
        int n = sc.nextInt();
        int digit = 0;
        int sum = 0;
        while (n > 0) {
            digit = n % 10;
            n = n / 10;
            sum += digit;
        }
        System.out.println("sum of Digits : " + sum);

    }

    // Reverse a number
    public void Reverse_number() {
        System.out.println("Enter number: ");
        int n = sc.nextInt();
        int digit = 0;
        int new_digit = 0;
        while (n > 0) {
            digit = n % 10;
            new_digit = new_digit * 10 + digit;
            n = n / 10;
        }
        System.out.println(new_digit);

    }

    // Largest digit in a number
    public void largest_digitofnumber() {
        System.out.println("Enter number: ");
        int n = sc.nextInt();
        int digit = 0;
        int largest = 0;
        while (n > 0) {
            digit = n % 10;
            System.out.println(digit);
            if (digit > largest) {
                largest = digit;
            }
            n = n / 10;
        }
        System.out.println(largest);

    }

    // Smallest digit in a number
    public void smallest_digitofnumber() {
        System.out.println("Enter number: ");
        int n = sc.nextInt();
        int digit = 0;
        int smallest = 9;
        while (n > 0) {
            digit = n % 10;
            System.out.println(digit);
            if (digit < smallest) {
                smallest = digit;
            }
            n = n / 10;
        }
        System.out.println(smallest);

    }

    // Count even and odd digits in a number
    public void even_odd_digits()
    {
        System.out.println("Enter number: ");
        int n = sc.nextInt();
        int digit = 0;
        int even =0;
        int odd =0;
        while (n>0)
            {
            digit = n%10;
            if (digit%2 == 0)
            {
                even = digit
            }
            n = n/10;
        }
        System.out.println();

    }

    // Find Factors of a Number
    public void finding_factors() {
        System.out.print("Enter number : ");
        int n = sc.nextInt();

        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                System.out.println(i);
                if (i != n / i)
                    System.out.println(n / i);
            }
        }

    }

    // Countp Factors of a Number
    public void count_factors() {
        System.out.print("Enter number : ");
        int n = sc.nextInt();
        int divisor = 0;
        int count = 0;

        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                divisor = i;
                count++;
            }
        }

        System.out.println("Total number of Factos are " + count);
    }

    // Print Prime Numbers from 1 to N
    public void prime_numbers_1toN() {
        System.out.print("Enter N: ");
        int n = sc.nextInt();

        for (int i = 2; i <= n; i++) {
            boolean isprime = true;
            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    isprime = false;
                    break;
                }
            }
            if (isprime)
                System.out.println(i);
        }
    }

    // Print Prime Numbers from N to 1
    public void prime_numbers_Nto1() {
        System.out.print("Enter N: ");
        int n = sc.nextInt();

        while (n >= 3) {
            boolean isprime = true;
            for (int j = 2; j < n; j++) {
                if (n % j == 0) {
                    isprime = false;
                    break;
                }
            }
            if (isprime)
                System.out.println(n);
            n--;
        }
    }

    // HCF of 2 numbers
    public void HCF_of2numbers() {
        System.out.print("Enter N: ");
        int n = sc.nextInt();
        int m = sc.nextInt();
        int a = Math.max(m, n);
        int b = Math.min(m, n);
        int remainder;

        while (b != 0) {
            remainder = a % b;
            a = b;
            b = remainder;
        }

        System.out.println(a);

    }

    // LCM of 2 numbers
    public void LCM_of2numbers() {
        System.out.print("Enter N: ");
        int n = sc.nextInt();
        int m = sc.nextInt();
        int a = Math.max(m, n);
        int b = Math.min(m, n);
        int remainder;
        int LCM;

        while (b != 0) {
            remainder = a % b;
            a = b;
            b = remainder;
        }
        int HCF = a;

        LCM = (m * n) / HCF;
        System.out.println(LCM);
    }

    // Print Perfect Squares from 1 to N
    public void perfectsquares_from1toN() {
        System.out.print("Enter N: ");
        int n = sc.nextInt();
        int i = 1;
        while (i * i <= n) {
            System.out.println(i * i);
            i++;
        }

    }

    // Print Armstrong numbers from 1 to N
    public void Armstrong_numbers_from_1_to_N() {
        System.out.print("Enter N: ");
        int N = sc.nextInt();

        for (int n = 1; n <= N; n++) {

            int temp = n;
            int temp1 = n;
            int count = 0;
            int digit = 0;
            int sum = 0;

            // to count digits
            while (temp > 0) {
                digit = temp % 10;
                count++;
                temp = temp / 10;
            }

            while (temp1 > 0) {
                digit = temp1 % 10;
                sum = sum + (int) Math.pow(digit, count);
                temp1 = temp1 / 10;
            }

            if (n == sum)
                System.out.println(n);
        }

    }

    // Print All Strong Numbers from 1 to N
    public void strongnumbersfrom1toN() {
        System.out.println("Enter Number : ");
        int N = sc.nextInt();

        for (int n = 1; n <= N; n++) {
            int original = n;
            int digit = 0;
            int sum = 0;

            while (original > 0) {
                int factorial = 1;
                digit = original % 10;
                for (int i = 1; i <= digit; i++) {
                    factorial *= i;
                }
                sum = sum + factorial;
                original = original / 10;
            }

            if (n == sum)
                System.out.println(n);

        }
    }

    // Digit sum is X
    public void digit_sum_X() {
        System.out.println("Enter digits: ");
        int digits = sc.nextInt();
        System.out.println("Enter sum: ");
        long sum = sc.nextInt();

        for (long i = (long) Math.pow(10, digits - 1); i < (long) ((Math.pow(10, digits))); i++) {
            long temp = i;
            long sums = 0;
            while (temp > 0) {

                sums += temp%10;
                temp/= 10;
            }

            if (sums == sum) {
                System.out.print(i + " " );
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
        // obj.getSecondLargest();
        // obj.Armstrong();
        // obj.Strongnumber();
        // obj.checkPerfectNumber();
        // obj.suubarray_sum();
        // obj.compositenumber();
        // obj.compositenumberprint();
        // obj.Multiplication_table();
        // obj.N_numbers();
        // obj.powerofnumber();
        // obj.Fibonacci();
        // obj.secondlargest();
        // obj.Fibonacci_tillN();
        // obj.Count_digits();
        // obj.Sum_digits();
        // obj.Reverse_number();
        // obj.largest_digitofnumber();
        // obj.smallest_digitofnumber();
        // obj.even_odd_digits();
        // obj.finding_factors();
        // obj.count_factors();
        // obj.prime_numbers_1toN();
        // obj.prime_numbers_Nto1();
        // obj.HCF_of2numbers();
        // obj.LCM_of2numbers();
        // obj.perfectsquares_from1toN();
        // obj.Armstrong_numbers_from_1_to_N();
        // obj.strongnumbersfrom1toN();
        obj.digit_sum_X();

        obj.sc.close();
    }
}
