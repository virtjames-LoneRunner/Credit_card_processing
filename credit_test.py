#credit = input("Number: ")



def parse_number(credit):
    digits_input = []
    for digit in credit:
        digits_input.append(int(digit))
    
    return digits_input 
    

def check_card(digits_input):
    mastercard_second = [1, 2, 3, 4, 5]
    odd_total = 0
    odd_list = []

    even_total = 0
    even_list = []
    even_list2 = []
    even_list3 = []

    odd_counter = -1
    even_counter = -2

    if len(digits_input) == 16 and digits_input[0] == 4:
        while odd_counter != -17:
            odd_list.append(digits_input[odd_counter])
            odd_total = digits_input[odd_counter]
            odd_counter -= 2
        while even_counter != -18:
            even_list.append(digits_input[even_counter])
            even_counter -= 2
        for x in even_list:
            x = x * 2
            even_list2.append(x)

        for x in even_list2:
            if x >= 10:
                even_list3.append(x % 10)
                even_list3.append(int(x / 10))
            else:
                even_list3.append(x)

        for number in even_list3:
            even_total += number

        final_list = odd_list + even_list3

        total = 0
        for x in final_list:
            total += x

        
        if total % 10 == 0:
            return "VISA"
        
        else:
            return "INVALID"

    elif len(digits_input) == 16 and digits_input[0] == 5 and digits_input[1] in mastercard_second:
        while odd_counter != -17:
            odd_list.append(digits_input[odd_counter])
            odd_total = digits_input[odd_counter]
            odd_counter -= 2
        while even_counter != -18:
            even_list.append(digits_input[even_counter])
            even_counter -= 2
        for x in even_list:
            x = x * 2
            even_list2.append(x)

        for x in even_list2:
            if x >= 10:
                even_list3.append(x % 10)
                even_list3.append(int(x / 10))
            else:
                even_list3.append(x)

        for number in even_list3:
            even_total += number

        final_list = odd_list + even_list3

        total = 0
        for x in final_list:
            total += x

        
        if total % 10 == 0:
            return "MASTERCARD"
        
        else:
            return "INVALID"
        

    elif len(digits_input) == 13 and digits_input[0] == 4:
        while odd_counter != -15:
            odd_list.append(digits_input[odd_counter])
            odd_total = digits_input[odd_counter]
            odd_counter -= 2
        while even_counter != -14:
            even_list.append(digits_input[even_counter])
            even_counter -= 2
        for x in even_list:
            x = x * 2
            even_list2.append(x)

        for x in even_list2:
            if x >= 10:
                even_list3.append(x % 10)
                even_list3.append(int(x / 10))
            else:
                even_list3.append(x)

        for number in even_list3:
            even_total += number

        final_list = odd_list + even_list3

        total = 0
        for x in final_list:
            total += x

        
        if total % 10 == 0:
            return "VISA"
        
        else:
            return "INVALID"
        

    elif len(digits_input) == 15:
        while odd_counter != -17:
            odd_list.append(digits_input[odd_counter])
            odd_total = digits_input[odd_counter]
            odd_counter -= 2
        while even_counter != -16:
            even_list.append(digits_input[even_counter])
            even_counter -= 2
        for x in even_list:
            x = x * 2
            even_list2.append(x)

        for x in even_list2:
            if x >= 10:
                even_list3.append(x % 10)
                even_list3.append(int(x / 10))
            else:
                even_list3.append(x)

        for number in even_list3:
            even_total += number

        final_list = odd_list + even_list3

        total = 0
        for x in final_list:
            total += x

        
        if total % 10 == 0:
            return "AMERICAN EXPRESS"
        
        else:
            return "INVALID"

    else:
        return "INVALID"
        
#digits = parse_number("2223000048400011")

#print(check_card(digits))