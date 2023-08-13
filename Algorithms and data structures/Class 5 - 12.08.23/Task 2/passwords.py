with open("source.txt") as source:
    data = source.readline().strip().split()
    amount_of_passwords_to_check = int(data[0])
    amount_of_samples = int(data[1])
    # List of passwords to check.
    passwords_to_check = []
    for _ in range(amount_of_passwords_to_check):
        passwords_to_check.append(source.readline().strip().split())
    # List of sample passwords.
    sample_passwords = []
    for _ in range(amount_of_samples):
        sample_passwords.append(source.readline().strip().split())
    # This compares the check passwords to sample
    # passwords and assigns the absolute difference index
    result = {}
    for password in passwords_to_check:
        absolute_values = {}
        for sample_password in sample_passwords:
            absolute_indexes = []
            for index, value in enumerate(sample_password[1:][:-1]):
                test_password_integer = int(password[1:][index])
                sample_password_integer = int(value)
                absolute_value = abs(
                    test_password_integer-sample_password_integer)
                absolute_indexes.append(absolute_value)
            absolute_values[sample_password[0]] = sum(absolute_indexes)

        result[password[0]] = absolute_values
    # This sorts the sample passwords by their difference index, lowest to highest
    sorted_result = {}
    for key, value in result.items():
        sorted_result[key] = sorted(value.items(), key=lambda x: x[1])
    # This keeps the lowest difference values and removes all others.
    end_result = {}
    for test_key, passwords in sorted_result.items():
        result = []
        for sample_index, password, in enumerate(passwords):
            if sample_index == 0:
                first_value = passwords[0][1]
                result.append(password)
            else:
                if password[1] == result[0][1]:
                    result.append(password)
                else:
                    continue
        end_result[test_key] = dict(result)
    # This sorts the values by sample password length, longest to shortest.
    decending_sort = {}
    for key, value in end_result.items():
        decending_sort[key] = list(sorted(
            value.items(), key=lambda x: len(x[0]), reverse=True))
    # This is to access the strength of a sample password.
    sample_password_strengths = {}
    for values in sample_passwords:
        sample_password_strengths[values[0]] = values[-1]
    # This is to write the valid sample passwords to file
    valid_sample_passwords = []
    for values in decending_sort.items():
        valid_sample_passwords.append([value[0] for value in values[1]])

with open("result.txt", "w") as output:
    for index in range(len(passwords_to_check)):
        output.write(
            f"{list(decending_sort)[index]} "
            f"{sample_password_strengths[decending_sort[
                ''.join(passwords_to_check[index][:1])][index][0]]} "
            f"{decending_sort[list(decending_sort)[index]][0][1]}\n")
        for password in valid_sample_passwords[index]:
            output.write(f"{password}\n")
