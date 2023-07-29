
def dec_to_bin(d):
    while True:
        if d <= 0:
            print("Bad number.")
            break
        else:
            binary = ""
            while True:
                r = d % 2
                if r == 1:
                    binary = f"1{binary}"
                else:
                    binary = f"0{binary}"
                d = d // 2
                if d != 0:
                    continue
                else:
                    print(binary)
                    break
        break


dec_to_bin(5)
