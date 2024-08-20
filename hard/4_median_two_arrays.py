# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
nums1 = [1, 3]
nums2 = [2]
nums3 = [1, 2]
nums4 = [3, 4]


def two_pointers(arr1, arr2):
    i, j, m1, m2 = 0, 0, 0, 0
    n = len(arr1)
    m = len(arr2)
    for count in range(
        0, (n + m) // 2 + 1
    ):  # ony need to iterate to half due to median definition
        m2 = m1  # m1 is the current median candidate, and m2 will store the previous one.
        print(count, (m1, m2))
        if i < n and j < m:
            if arr1[i] > arr2[j]:
                m1 = arr2[
                    j
                ]  # take smaller value to ensure that the order of smalelst to largest are kept
                j += 1
            else:
                m1 = arr1[i]
                i += 1
        elif i < n:
            m1 = arr1[i]
            i += 1
        else:
            m1 = arr2[j]
            j += 1

    if not (n + m) % 2:
        return float(m1)
    else:
        ans = float(m1) + float(m2)
        return ans / 2.0


print(two_pointers(nums1, nums4))
