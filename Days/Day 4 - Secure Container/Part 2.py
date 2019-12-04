def main():
    range_passwords = (125730, 579382)
    count = 0
    for i in range(*range_passwords):
        password = str(i)
        j = 0
        double = 0
        while j < len(password) - 1:
            if password[j] == password[j + 1]:
                if (j == len(password) - 2) or (password[j + 2] != password[j]):
                    double = 1
                    break
                else:
                    while (j < len(password) - 2) and (password[j + 2] == password[j]):
                        j += 1
                    j += 2
            else:
                j += 1
        if not double:
            continue
        
        if list(password) == sorted(list(password)):
            count += 1
            
    print(count)
    


if __name__ == "__main__":
    main()
