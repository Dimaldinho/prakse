
def collatz(number):
    try:
        if number%2 == 0:
            return print(number//2)
        else: return print(3 * number + 1)
    except (ValueError,TypeError):
        print("Error")
    

collatz("a")
collatz(10)
collatz(5)