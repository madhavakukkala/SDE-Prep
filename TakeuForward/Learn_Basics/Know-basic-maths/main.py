import math
class MathProblems():

    def count_all_digits_of_a_number(self,n):
        # n = self.n
        count =int(math.log10(n) + 1)
        print(f"The number {n} has {count} digits")
        
    def reverse_number(self,n):
        temp = n
        reverse = 0
        while temp>0:
            digit = temp%10
            reverse = reverse *10 + digit
            temp//=10
        print(reverse)
        
    def palindrome(self,n):
        temp = n
        reverse = 0
        while temp>0:
            digit = temp%10
            reverse = reverse *10 + digit
            temp//=10
        if n == reverse:
            print(f"{reverse} >> Yes , Palindrome")
        else:
            print(f"{reverse} >> No , Not a Palindrome")

    def gcd(self,a,b):
        while a%b != 0:
            remainder = a%b
            a = b
            b = remainder

        print(b)


    def armstrong(self,n):
        count = 0
        temp = n

        while temp>0:
            temp//=10
            count+=1

        temp = n
        total = 0

        while temp>0:
            total = total + math.pow((temp%10), count)
            temp//=10

        if n == total:
            print(f"{n} is armstrong")
        else:
            print(f"{n} is not armstrong")

        
    def divisors(self,n):
        all_divisors = []
        i = 1
        while i**2 <= n:

            if n%i == 0:
                all_divisors.append(i)
            if i!=n//i:
                all_divisors.append(n//i)
            
            i+=1
        all_divisors.sort()

        print(sorted(all_divisors))

    
    def prime_check(self, n):
        if n <= 1:
            print("Not prime")
            return

        i = 2

        while i * i <= n:
            if n % i == 0:
                print("Not prime")
                return
            i += 1

        print("Prime")

         



problems = MathProblems()

# problems.count_all_digits_of_a_number(6789098765678)
# problems.reverse_number(7407)
# problems.palindrome(4554)
# problems.gcd(12,9)
# problems.armstrong(371)
# problems.divisors(36)
# problems.prime_check(7)





