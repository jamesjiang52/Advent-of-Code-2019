def main():
    range_passwords = (125730, 579382)
    count = 0
    for i in range(*range_passwords):
        password = str(i)
        for j in range(len(password) - 1):
            if password[j] == password[j + 1]:
                break
        else:
            continue
        
        if list(password) == sorted(list(password)):
            count += 1
            
    print(count)
    


if __name__ == "__main__":
    main()
