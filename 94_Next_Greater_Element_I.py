class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        result = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if j != len(nums2) - 1:
                        for k in range(j + 1, len(nums2)):
                            if nums2[k] > nums2[j]:
                                result.append(nums2[k])
                                break
                    if len(result) < i + 1:
                        result.append(-1)

        return result