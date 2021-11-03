def main():
    with open('output.txt') as f:
        lines = f.readlines()

        # Defining variables
        ok = 0
        false_pos = 0
        false_neg = 0

        # Getting data
        for line in lines:
            splitted = line.split()
            print(splitted[1] + " ~ " + splitted[3] + " / Expected : " + splitted[6] + " - Computed : " + splitted[9])

            # Processing data
            if splitted[6] == splitted[9]:
                ok += 1
            elif splitted[6] == "true" and splitted[9] == "false":
                false_neg += 1
            elif splitted[6] == "false" and splitted[9] == "true":
                false_pos += 1

        # Computing results
        length = len(lines)
        print()
        print("--------------------------------------------------")
        print()
        print(f"{length} fingerprints have been compared :")
        ratio = (ok / length) * 100
        fp_amount = (false_pos / length) * 100
        fn_amount = (false_neg / length) * 100
        print(f"Ratio is {ratio} %")
        print(f"We have {fp_amount} % false positives")
        print(f"We have {fn_amount} % false negatives")


if __name__ == '__main__':
    main()
