def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("I am inside finally block")

main()


# even if return statement is executed in try or 
# except block, finally block will be executed 