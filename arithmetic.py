def sum_strings(arr1, arr2):
    try:
        # Converting strings to array of int's
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

    # Checking if there is any carry out
    if carry > 0:
        result.insert(0, carry)
    return result


def mul_strings(arr1, arr2):

    if arr1 == "" and arr2 == "":
        return []

    try:
        # Edge case if for example if arr1 = "000" we dont want the output to be [0,0,0]
        # but distinct number: [0]
        if int(arr1) == 0 or int(arr2) == 0:
            return [0]
    except Exception:
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

    # for example arr1 = "" and arr2 = "4321" -> [4, 3, 2, 1]
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

        # zero wrap on the right of current_result k times
        for i in range(k):
            current_result.insert(0, 0)

        for it2 in range(len(num2)-1, -1, -1):
            current_num2 = num2[it2]
            current_sum = current_num1 * current_num2 + carry
            current_result.insert(0, current_sum % 10)
            carry = int(current_sum / 10)
        if carry > 0:
            current_result.insert(0, carry)
        results.append(current_result)

        k += 1

    final_result = []
    # calculate all the sums from all the iterations
    for item in results:
        final_result = sum_strings(final_result, item)
    return final_result


