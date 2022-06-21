def palindrom(text):
     # = text.split(' ')
    centr = len(text.replace(' ',''))//2
    withowt_space = text.replace(' ','')
    # if withowt_space[:centr] == text[centr:]:
    #     return print('OK')
    return print(f'center{centr}.  t1 - {withowt_space[:centr]} , t2 - {withowt_space[centr+1:]} ')


my_string = input('Enter words or sentences and I will determine if they are a palindrome-->>').lower()




palindrom(my_string)