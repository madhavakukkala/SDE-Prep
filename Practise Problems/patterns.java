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
        for (int row = 0; row <n; row++) {
            for (int col = 1; col <=(n-row); col++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    public void pattern6() {
        int n = 5;
        for (int row = 0; row <n; row++) {
            for (int col = 1; col <=(n-row); col++) {
                System.out.print(col);
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
    }
}
