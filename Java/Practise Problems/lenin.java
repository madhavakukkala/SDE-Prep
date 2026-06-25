public class lenin {

    public static void main(String[] args) {
        int n = 4582;
        int digit = 0;
        int place  = 1;
        int temp = n;
        int reverse = 0;

        while (temp > 0)
        {
            digit = temp%10;
            reverse = reverse + place * digit;
            place*=10;
            System.out.println(reverse);

            temp /= 10;
        }

    }
}