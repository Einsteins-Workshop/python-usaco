number_of_tests = int(input("GIVE ME A NUMBER OF TESTS."))
for x in range(number_of_tests):
    print(x)
    number = int(input("GIVE ME A NUMBER."))
    if number >= 5:
        for y in range(2, number+1):
            print(y)
            digits = str(y)
            if digits[0] <= '4':
                answer = 0
                print(answer)
            elif digits[0] >= '5':
                answer = 10
                print(answer)


    print(f"All done with loop {1} YAAAAAAAAAAAAAYYYYYYYYYYYYYYY!")