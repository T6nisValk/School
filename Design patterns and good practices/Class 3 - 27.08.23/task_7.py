def fibonacci(n):
    result = []
    if n < 3:
        for num in range(n):
            result.append(num)
        return result
    else:
        result = [0, 1]
        # n-2 because there are already 2 values in result.
        for num in range(n - 2):
            result.append(result[num] + result[num + 1])
        return result


print(fibonacci(int(input("Enter the length of fibonacci sequence you want: "))))
