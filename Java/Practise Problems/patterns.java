

class allPattern {

    public void pattern1() {
        int n = 5;
        for (int row = 1; row <= n; row++) {
            for (int col = 1; col <= n; col++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    public void pattern2() {
        int n = 5;
        for (int row = 1; row <= n; row++) {
            for (int col = 1; col <= row; col++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    public void pattern3() {
        int n = 5;
        for (int row = 1; row <= n; row++) {
            for (int col = 1; col <= row; col++) {
                System.out.print(col);
            }
            System.out.println();
        }
    }

    public void pattern4() {
        int n = 5;
        for (int row = 1; row <= n; row++) {
            for (int col = 1; col <= row; col++) {
                System.out.print(row);
            }
            System.out.println();
        }
    }

    public void pattern5() {
        int n = 5;
        for (int row = 0; row < n; row++) {
            for (int col = 1; col <= (n - row); col++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    public void pattern6() {
        int n = 5;
        for (int row = 0; row < n; row++) {
            for (int col = 1; col <= (n - row); col++) {
                System.out.print(col);
            }
            System.out.println();
        }
    }

    public void pattern7() {
        int n = 5;
        for (int row = 1; row <= n; row++) {
            // Spaces loop
            for (int col = 1; col <= (n - row); col++) {
                System.out.print(" ");
            }

            // stars Loop
            for (int col = 1; col <= (2 * row - 1); col++) {
                System.out.print("*");
            }

            System.out.println();
        }
    }

    public void pattern8() {
        int n = 5;
        for (int row = 1; row <= n; row++) {
            // Spaces loop
            for (int col = 1; col <= (row - 1); col++) {
                System.out.print(" ");
            }

            // stars Loop
            for (int col = 1; col <= (2 * n - (2 * row - 1)); col++) {
                System.out.print("*");
            }

            System.out.println();
        }
    }

    public void pattern9() {
        int n = 5;

        // upper
        for (int row = 1; row <= n; row++) {
            // Spaces loop
            for (int col = 1; col <= (n - row); col++) {
                System.out.print(" ");
            }

            // stars Loop
            for (int col = 1; col <= (2 * row - 1); col++) {
                System.out.print("*");
            }

            System.out.println();
        }

        // lower
        for (int row = 1; row <= n; row++) {
            // Spaces loop
            for (int col = 1; col <= (row - 1); col++) {
                System.out.print(" ");
            }

            // stars Loop
            for (int col = 1; col <= (2 * n - (2 * row - 1)); col++) {
                System.out.print("*");
            }

            System.out.println();
        }

    }

    public void pattern10() {
        int n = 5;
        for (int i = 1; i <= 2 * n - 1; i++) {
            int stars = i;
            if (i > n)
                stars = (2 * n - i);
            for (int j = 1; j <= stars; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    public void pattern11() {
        int n = 5;
        int start = 1;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0)
                start = 1;
            else
                start = 0;
            for (int j = 0; j <= i; j++) {
                System.out.print(start + " ");
                start = 1 - start;
            }
            System.out.println();
        }
    }

    public void pattern12() {
        int n = 6;
        for (int i = 1; i <= n; i++) {

            // numbers
            for (int j = 1; j <= i; j++) {
                System.out.print(j);
            }

            // spaces
            for (int j = 1; j <= (2 * n - 2 * (i)); j++) {
                System.out.print(" ");
            }

            // numbers
            for (int j = i; j >= 1; j--) {
                System.out.print(j);
            }
            System.out.println();

        }
    }

    public void pattern13() {
        int n = 5;
        int number = 1;
        for (int i = 1; i <= n; i++) {

            for (int j = 1; j <= i; j++) {
                System.out.print(number + " ");
                number++;
            }
            System.out.println();
        }
    }

    public void pattern14() {
        int n = 5;
        for (int i = 0; i < n; i++) {

            for (char j = 'A'; j <= 'A' + i; j++) {
                System.out.print(j);
            }
            System.out.println();
        }
    }

    public void pattern15() {
        int n = 5;
        for (int i = 1; i <= n; i++) {

            for (char j = 'A'; j < 'A' + (n - (i - 1)); j++) {
                System.out.print(j);
            }
            System.out.println();
        }
    }

    public void pattern16() {
        int n = 5;
        char ch = 'A';
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(ch);

            }
            System.out.println();
            ch++;

        }
    }

    public void pattern17() {
        int n = 5;
        for (int i = 0; i < n; i++) {

            for (int j = 1; j <= n - i - 1; j++) {
                System.out.print(" ");
            }

            char ch = 'A';
            int breaks = (2 * i + 1) / 2;
            for (int j = 1; j <= 2 * i + 1; j++) {
                System.out.print(ch);
                if (j <= breaks) {
                    ch++;
                } else
                    ch--;
            }

            System.out.println();

        }
    }

    public void pattern18() {
        int n = 5;
        for (int i = 0; i < n; i++) {

            for (int j = 1; j <= n - i - 1; j++) {
                System.out.print(" ");
            }

            char ch = 'A';
            int breaks = (2 * i + 1) / 2;
            for (int j = 1; j <= 2 * i + 1; j++) {
                System.out.print(ch);
                if (j <= breaks) {
                    ch++;
                } else
                    ch--;
            }

            System.out.println();

        }
    }

    public void pattern19() {
        int n = 5;

        // outer
        for (int i = 1; i <= n; i++) {
            char ch = (char) (65 + (n - 1));

            // inner
            for (int j = 1; j <= i; j++) {
                System.out.print((char) (ch - i + 1) + " ");
                ch++;
            }

            System.out.println();
        }

    }

    public void pattern20() {
        int n = 5;
        int stars;
        int spaces;

        // outerloop
        for (int i = 1; i <= 2 * n - 1; i++) {
            stars = n - i + 1;
            spaces = 2 * i - 2;
            if (i > n) {
                stars = i - n + 1;
                spaces = 2 * (2 * n - i) - 2;

            }
            // top stars
            // for (int j = 1; j <= n - i + 1; j++) {
            for (int j = 1; j <= stars; j++) {
                System.out.print("*");
            }

            // spaces
            for (int j = 1; j <= spaces; j++) {
                System.out.print(" ");
            }

            // top stars
            // for (int j = 1; j <= n - i + 1; j++) {
            for (int j = 1; j <= stars; j++) {
                System.out.print("*");
            }

            System.out.println();

        }

    }

    public void pattern21() {
        int n = 5;
        int stars;
        int spaces;
        for (int i = 1; i <= 2 * n - 1; i++) {
             if (i <= n) {
            stars = i;
            spaces = 2 * (n - i);
        } else {
            stars = 2 * n - i;
            spaces = 2 * (i - n);
        }
            // top stars
            // for (int j = 1; j <= n - i + 1; j++) {
            for (int j = 1; j <= stars; j++) {
                System.out.print("*");
            }

            // spaces
            for (int j = 1; j <= spaces; j++) {
                System.out.print(" ");
            }

            // top stars
            // for (int j = 1; j <= n - i + 1; j++) {
            for (int j = 1; j <= stars; j++) {
                System.out.print("*");
            }

            System.out.println();

        }
    }

}

public class patterns {
    public static void main(String[] args) {
        allPattern obj = new allPattern();
        obj.pattern1();
        obj.pattern2();
        obj.pattern3();
        obj.pattern4();
        obj.pattern5();
        obj.pattern6();
        obj.pattern7();
        obj.pattern8();
        obj.pattern9();
        obj.pattern10();
        obj.pattern11();
        obj.pattern12();
        obj.pattern13();
        obj.pattern14();
        obj.pattern15();
        obj.pattern16();
        obj.pattern17();
        obj.pattern18();
        obj.pattern19();
        obj.pattern20();
        obj.pattern21();

    }
}
