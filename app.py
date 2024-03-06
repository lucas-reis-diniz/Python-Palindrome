def Palindrome():
    def catchUserNumber():
        number1 = input("Enter a number: ")

        return int(number1)

    x = catchUserNumber()
    def transformPalindrome():
        palindrome_stg = str(x)
        palindrome_stg_inverse = palindrome_stg[::-1]

        numero_inverse = int(palindrome_stg_inverse)

        return int(numero_inverse)

    x_inverse = transformPalindrome()

    print(f'{x_inverse}, so your number is reversed')

    def checkPalindrome():
        if x == x_inverse:
            print("The number is palindrome")
        else:
            print("The number is not a palindrome")

    checkPalindrome()
Palindrome()