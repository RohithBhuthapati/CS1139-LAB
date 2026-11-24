s = input()

if len(s) == 10 and s[0:2] == "RJ":
    if s[0].isupper() and s[1].isupper():
        if s[2].isdigit() and s[3].isdigit():
            if s[4].isupper() and s[5].isupper():
                if s[6:].isdigit():
                    print("True")
                else:
                    print("False")
            else:
                print("False")
        else:
            print("False")
    else:
        print("False")
else:
    print("False")