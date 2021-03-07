def deleteSameNum(num):
    num.sort()
    last = num[-1]
    for i in range(len(num) - 2, -1, -1):
        if last == num[i]:
            del num[i]  # 删除后位置i处的元素后，其后一个相同的元素又补到了i位置
        else:
            last = num[i]
    return num


if __name__ == "__main__":
    num = [1, 1, 1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14]
    print(deleteSameNum(num))