from time import time
import random
from math import ceil
def brute_force(a , b , length):
    ans = [0]* ( 2*length )
    c = -1
    index = -1
    ans_carry = 0
    inner_carry = 0
    for dig_b in reversed(b):
        dig_int_b = int(dig_b)
        inner_carry = 0 
        ans_carry = 0
        for dig_a in reversed(a):
            dig_int_a = int(dig_a)
            dig_result = (dig_int_a * dig_int_b) + inner_carry
            inner_carry = dig_result // 10
            dig_result = dig_result % 10
            ans_result = ans[index] + dig_result + ans_carry
            ans_carry = ans_result // 10
            ans_result = ans_result % 10
            ans[index] = ans_result
            index = index - 1
        ans[index] = inner_carry + ans_carry
        index = c - 1
        c = c - 1
    ans[0] = inner_carry + ans_carry            
    return ans

def zero_pad(int_string, num_zeros):
    for i in range (num_zeros):          
        int_string = int_string + '0'
    return int_string



def big_int_add(a,b):
    if a == '':
        a = '0'
    if b == '':
        b = '0'
    length_a = len(a)
    length_b = len(b)
    n = max(length_a, length_b) + 1
    result = ['']*n
    carry = 0
    for i in range(-1, -1*n ,-1):
        try:
            add_digits = int(a[i]) + int(b[i]) + carry
            carry = add_digits // 10
            result[i] = str(add_digits % 10)
        except:
            if length_a > length_b:
                add_digits = int(a[i]) + carry
                carry = add_digits // 10
                result[i] = str(add_digits % 10)
            else:
                add_digits = int(b[i]) + carry
                carry = add_digits // 10
                result[i] = str(add_digits % 10)
    final_string = ""
    if carry == 0:
        result = result[1:]        
        return final_string.join(result)
    else:
        result[0] = str(carry)
        return final_string.join(result)

def big_int_minus(a,b):
    if (a == b):
        return '0'
    if a == '':
        a = '0'
    if b == '':
        b = '0'
    length_a = len(a)
    length_b = len(b)
    n = 0
    check_big_a = True
    if length_a > length_b:
        n = length_a
    elif length_a < length_b:
        n = length_b
        check_big_a = False
    else:
        n = length_a
        for i in range (length_a):
            if a[i] == b[i]:
                continue
            elif b[i] > a[i]:
                check_big_a = False
                break 
            else:
                break
    carry = 0
    result = ['']*n
    if (check_big_a):
        for i in range(-1, -1*n - 1,-1):
            try:
                sub_digits = int(a[i]) - carry - int(b[i]) 
                if sub_digits < 0:
                    sub_digits = sub_digits + 10
                    carry = 1
                else:
                    carry = 0
                result[i] = str(sub_digits)
            except:
                    sub_digits = int(a[i]) - carry
                    if sub_digits < 0:
                        sub_digits = sub_digits + 10
                        carry = 1
                    else:
                        carry = 0
                    result[i] = str(sub_digits)
    else:
        for i in range(-1, -1*n - 1,-1):
            try:
                sub_digits = int(b[i]) - carry - int(a[i]) 
                if sub_digits < 0:
                    sub_digits = sub_digits + 10
                    carry = 1
                else:
                    carry = 0
                result[i] = str(sub_digits)
            except:
                sub_digits = int(b[i]) - carry
                if sub_digits < 0:
                    sub_digits = sub_digits + 10
                    carry = 1
                else:
                    carry = 0
                result[i] = str(sub_digits)
    
    final_string = ""
    for i in range(len(result)):
        if i == len(result) - 1 and result[i] == '0':
            return '0'
        if result[i] != '0' and result[i] != '':       
            return final_string.join(result[i:])

def karatsuba_multiply(x,y):
    if len(x) == 1 or len(y) == 1:
        if x == "" or y == "":
            return '0'
        else:
            return str(int(x)* int(y))
    else:
        n = max(len(x), len(y))
        m = (n // 2)
        minus_m = m * -1 
        a = x[:minus_m]
        b = x[minus_m:]
        c = y[:minus_m]
        d = y[minus_m:]
        e = karatsuba_multiply(a,c)
        f = karatsuba_multiply(b,d)
        g = karatsuba_multiply(big_int_add(a,b), big_int_add(c,d))
        A = zero_pad(e, (2*m))
        B = big_int_minus(big_int_minus(g,f), e)
        B = zero_pad(B, m)
        result = big_int_add(big_int_add(A,B),f)
        return result

def plot():
    digit_list = [999, 1999, 2999, 3999, 4999, 5999, 6999, 7999, 8999, 9999]
    dq_list = []
    for i in range (len(digit_list)):
        temp_sum = 0
        print(digit_list[i] + 1)
        for j in range (3):
            digit = digit_list[i]
            x = random.randrange((10**digit),(10**digit+1))
            y = random.randrange((10**digit),(10**digit+1))
            t = time()
            ans_dq = karatsuba_multiply( str(x),str(y))
            #ans_dq = brute_force(str(x), str(y),len(str(x))) #uncomment this to print times for brute force and comment upper line
            rt = time()
            dt = (rt - t) * 1000
            temp_sum = temp_sum + dt
        print(temp_sum/3)
        dq_list.append(temp_sum/3)
    print(dq_list)


def main():
    check = True
    while(check):
        b_or_d = input("Enter 'B' for Brute-force and 'D' for divide-conquer: \n")
        first_int = input('Enter n digit integer: \n')
        second_int = input ('Second n digit integer: \n')
        if (len(first_int) != len(second_int)):
            print("Both integers should should of n digits\n")
        else:
            check = False

    if b_or_d == 'B':
        ans_bf = brute_force(first_int, second_int, max(len(first_int), len(second_int)))
        if ans_bf[0] == 0:
            ans_bf = ans_bf[1:]
        str_list = [str(i) for i in ans_bf]
        str1 = ""
        str1 = str1.join(str_list)
        print("Answer: ", str1)
    else:
        ans_dq = karatsuba_multiply(first_int,second_int)
        print("Answer: ", ans_dq)

    #Uncomment to see times of each algorithm (default set to karatsuba, uncomment the line in plot function to see times of bruteforce)
    #plot()
   

main()