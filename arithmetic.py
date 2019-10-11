def sum_strings(arr1, arr2):
    try:
        num1 = [int(i) for i in arr1]
        num2 = [int(i) for i in arr2]
    except Exception:
        raise Exception("Cannot convert your string to array of int")

    it1 = len(num1)-1
    it2 = len(num2)-1
    carry = 0
    result = []
    while it1 >= 0 or it2 >= 0:
        current_num1 = num1[it1] if it1 >= 0 else 0
        current_num2 = num2[it2] if it2 >= 0 else 0
        current_sum = current_num1 + current_num2 + carry
        carry = int(current_sum / 10)
        result.insert(0, current_sum % 10)
        it1 -= 1
        it2 -= 1
    if carry > 0:
        result.insert(0, carry)
    return result


def mul_strings(arr1, arr2):
    if arr1 == "" and arr2 == "":
        return []

    try:
        if int(arr1) == 0 or int(arr2) == 0:
            return [0]
    except:
        pass

    num1 = []
    num2 = []

    try:
        if arr1 != "":
            num1 = [int(i) for i in arr1]
        if arr2 != "":
            num2 = [int(i) for i in arr2]
    except TypeError:
        raise TypeError("Cannot convert your string to array of int")

    if arr1 == "":
        return num2
    elif arr2 == "":
        return num1

    k = 0
    results = [[]]
    for it1 in range(len(num1) - 1, -1, -1):
        current_num1 = num1[it1]
        carry = 0
        current_result = []
        # zero pad on the right k times
        for i in range(k):
            current_result.insert(0, 0)
        for it2 in range(len(num2)-1, -1, -1):
            current_num2 = num2[it2]
            x = current_num1 * current_num2 + carry
            current_result.insert(0, x % 10)
            carry = int(x / 10)
        if carry > 0:
            current_result.insert(0, carry)
        results.append(current_result)
        k += 1

    final_result = []
    for item in results:
        final_result = sum_strings(final_result, item)
    return final_result


