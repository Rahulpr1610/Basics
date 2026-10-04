class NumberCheck:

    @staticmethod
    def is_even(num):
        if num % 2 == 0 :
            print("Even")
        else:
            print("Odd")

    @staticmethod
    def is_positive(num):
        if num >= 0:
            print("Positive")
        else:
            print("Negative")


NumberCheck.is_even(4)
NumberCheck.is_positive(-2)