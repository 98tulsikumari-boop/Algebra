class Calculate:
    def __init__(self, *args):
        self.a = args[0]
        self.b = args[1]

    def show(self):
        print(f"a = {self.a}, b = {self.b}")
      
class Two_Var(Calculate):  # Inheritance
    def __init__(self, *args):
        super().__init__(*args)
        self.d = args[2]
        self.e = args[3]
        self.f = args[4]
        self.g = args[5]
        self.h = args[6]
        self.i = args[7]
        self.j = args[8]
        self.k = args[9]
        self.l = args[10]
        self.m = args[11]
        self.n = args[12]
        self.o = args[13]
        self.p = args[14]
        self.q = args[15]
        self.r = args[16]
        self.s = args[17]     

    def show_d(self):
        print(f"(a + b)**2 = {self.d}")

    def show_e(self):
        print(f"(a - b)**2 = {self.e}")

    def show_f(self):
        print(f"(a**2 + b**2) = {self.f}")

    def show_g(self):
        print(f"(a**2 - b**2) = {self.g}")

    def show_h(self):
        print(f"(a + b)**3 = {self.h}")

    def show_i(self):
        print(f"(a - b)**3 = {self.i}")

    def show_j(self):
        print(f"(a**3 + b**3) = {self.j}")

    def show_k(self):
        print(f"(a**3 - b**3) = {self.k}")

    def show_l(self):
        print(f"(a**4 - b**4) = {self.l}")

    def show_m(self):
        print(f"(a**4 + b**4) = {self.m}")

    def show_n(self):
        print(f"(a + b)**4 = {self.n}")

    def show_o(self):
        print(f"(a - b)**4 = {self.o}")

    def show_p(self):
        print(f"(a - b)**5 = {self.p}")

    def show_q(self):
        print(f"(a + b)**5 = {self.q}")

    def show_r(self):
        print(f"(a + b)**2 + (a - b)**2 = {self.r}")

    def show_s(self):
        print(f"(a + b)**2 - (a - b)**2 = {self.s}")

class Three_Var(Calculate):  # Inheritance
    def __init__(self, a,b,c,t,u):
        super().__init__(a,b)
        self.c = c
        self.t = t
        self.u = u

    def show(self):  # Polymorphism in action (Method overriding)
        print(f"a = {self.a}\nb = {self.b}\nc = {self.c}")

    def show_t(self):
        print(f"a**2 + b**2 + c**2 - a*b -b*c -c*a = {self.t}")

    def show_u(self):
        print(f"a**3 + b**3 + c**3 - 3*a*b*c = {self.u}")

# -----Main-------
if __name__ =="__main__":
    nums: list = []
    a: float = 0
    b: float = 0

    while True:
        print("\n---Welcome to basics of Algebra---")
        print("\n1. Insert First & Second Variables")
        print("2. Display Formula for Two Variables")
        print("3. Insert Third Variable")
        print("4. Display Formula for Three Variables")
        print("5. Exiting the Program\n")

        ch: int = int(input("Select your choice between (1-5): "))

        if ch == 1:
            a: float = float(input("Enter a value of a: "))
            b: float = float(input("Enter a value of b: "))
            d: float = (a + b)**2                  # == (a**2 + 2*a*b + b**2)
            e: float = (a - b)**2                  # == (a**2 - 2*a*b + b**2)
            f: float = (a**2 + b**2)               # == ((a + b)**2 - 2*a*b)
            g: float = (a**2 - b**2)               # == (a - b)*(a + b)
            h: float = (a + b)**3                  # == (a**3 + 3*a**2*b + 3*a*b**2 + b**3)
            i: float = (a - b)**3                  # == (a**3 - 3*a**2*b + 3*a*b**2 - b**3)
            j: float = (a**3 + b**3)               # == (a + b)*(a**2 - a*b + b**2)
            k: float = (a**3 - b**3)               # == (a - b)*(a**2 + a*b + b**2)
            l: float = (a**4 - b**4)               # == (a - b)*(a + b)*(a**2 + b**2)
            m: float = (a**4 + b**4)               # == (a + b)**4 - 4*a*b + 2*(a**2)*(b**2) 
            n: float = (a + b)**4                  # == (a**4 + 4*a**3*b + 6*a**2*b**2 + 4*a*b**3 + b**4)
            o: float = (a - b)**4                  # == (a**4 - 4*a**3*b + 6*a**2*b**2 - 4*a*b**3 + b**4)
            p: float = (a - b)**5                  # == (a**5 - 5*a**4*b + 10*a**3*b**2 - 10*a**2*b**3 + 5*a*b**4 - b**5)
            q: float = (a + b)**5                  # == (a**5 + 5*a**4*b + 10*a**3*b**2 + 10*a**2*b**3 + 5*a*b**4 + b**5)
            r: float = (a + b)**2 + (a - b)**2     # == 2*(a**2 + b**2)
            s: float = (a + b)**2 - (a - b)**2     # == 4*a*b

            two_var = Two_Var(a,b,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s)
            nums.append(two_var)
            print("\nValues Inserted Successfully")
            for v in nums:
                if isinstance(v, Two_Var):
                    v.show()
            
        elif ch == 2:
            if not nums:
                print("No Records")
            else:
                while True:
                    print("\n---Formulas---")
                    print("-------------------------")
                    print("1. For (a + b)**2 ")
                    print("2. For (a - b)**2 ")
                    print("3. For (a**2 + b**2) ")
                    print("4. For (a**2 - b**2) ")
                    print("5. For (a + b)**3 ")
                    print("6. For (a - b)**3 ")
                    print("7. For (a**3 + b**3) ")
                    print("8. For (a**3 - b**3) ")
                    print("9. For (a**4 - b**4) ")
                    print("10. For (a**4 + b**4) ")
                    print("11. For (a + b)**4 ")
                    print("12. For (a - b)**4 ")
                    print("13. For (a - b)**5 ")
                    print("14. For (a + b)**5 ")
                    print("15. For (a + b)**2 + (a - b)**2 ")
                    print("16. For (a + b)**2 - (a - b)**2")
                    print("17. To Exit\n")

                    choice: int = int(input("Enter your choice: "))

                    if choice == 1:
                        for v in nums:
                            if isinstance(v, Two_Var):
                                v.show_d()

                    elif choice == 2:
                        for v in nums:
                            if isinstance(v, Two_Var):
                                v.show_e()

                    elif choice == 3:
                        for v in nums:
                            if isinstance(v, Two_Var):
                                v.show_f()

                    elif choice == 4:
                        for v in nums:
                            if isinstance(v, Two_Var):
                                v.show_g()

                    elif choice == 5:
                        for v in nums:
                            if isinstance(v, Two_Var):
                                v.show_h()

                    elif choice == 6:
                        for v in nums:
                            if isinstance(v, Two_Var):
                                v.show_i()

                    elif choice == 7:
                        for v in nums:
                            if isinstance(v, Two_Var):
                                v.show_j()

                    elif choice == 8:
                        for v in nums:
                            if isinstance(v, Two_Var):
                                v.show_k()

                    elif choice == 9:
                        for v in nums:
                            if isinstance(v, Two_Var):
                                v.show_l()

                    elif choice == 10:
                        for v in nums:
                            if isinstance(v, Two_Var):
                                v.show_m()

                    elif choice == 11:
                        for v in nums:
                            if isinstance(v, Two_Var):
                                v.show_n()

                    elif choice == 12:
                        for v in nums:
                            if isinstance(v, Two_Var):
                                v.show_o()

                    elif choice == 13:
                        for v in nums:
                            if isinstance(v, Two_Var):
                                v.show_p()

                    elif choice == 14:
                        for v in nums:
                            if isinstance(v, Two_Var):
                                v.show_q()

                    elif choice == 15:
                        for v in nums:
                            if isinstance(v, Two_Var):
                                v.show_r()

                    elif choice == 16:
                        for v in nums:
                            if isinstance(v, Two_Var):
                                v.show_s()

                    elif choice == 17:
                        print(" Exit ")
                        break
                    else:
                        print("Invalid choice! Please Enter valid choice\n")

        elif ch == 3:
            c: float = float(input("Enter value of c: "))
            t: float = a**2 + b**2 + c**2 - a*b -b*c -c*a   # == (1/2)*[(a-b)**2 + (b-c)**2 + (c-a)**2]
            u: float = a**3 + b**3 + c**3 - 3*a*b*c         # == (a+b+c)(a**2 + b**2 + c**2 -a*b - b*c -c*a)
            three_var = Three_Var(a,b,c,t,u)
            nums.append(three_var)
            print("\nThird Variable added Successfully")
            for v in nums:
                if isinstance(v, Three_Var):
                    v.show()

        elif ch == 4:
            if not nums:
                print("No Records")
            else:
                while True:
                    print("\n---Formulas---")
                    print("-------------------------")
                    print("1. For a**2 + b**2 + c**2 - a*b -b*c -c*a ")
                    print("2. For a**3 + b**3 + c**3 - 3*a*b*c")
                    print("3. To Exit\n")

                    choice: int = int(input("Enter your choice: "))

                    if choice == 1:
                        for v in nums:
                            if isinstance(v, Three_Var):
                                v.show_t()

                    elif choice == 2:
                        for v in nums:
                            if isinstance(v, Three_Var):
                                v.show_u()

                    elif choice == 3:
                        print("Exit")
                        break
                    else:
                        print("Invalid Choice! Please Enter valid choice.\n")

        elif ch == 5:
            print("Exiting the Program")
            break
        else:
            print("Invalid Choice! Please Enter valid choice.\n")

                    

                    

                        


            

                    
            

                

        
            
            

        
