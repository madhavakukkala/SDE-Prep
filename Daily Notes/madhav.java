import java.util.Scanner;

public class madhav {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("a = ");
        int a = sc.nextInt();
        System.out.print("b = ");
        int b = sc.nextInt();

        int result = ((a*a - b*b)/(a-b));
        System.out.println(result);


    }
}