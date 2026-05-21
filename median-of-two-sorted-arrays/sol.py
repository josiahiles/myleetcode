class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        zip = self.merge(nums1, nums2)
        n = len(zip)
        if len(zip) % 2 == 1:
            return zip[(n // 2)]
        else:
            return (zip[n // 2 - 1] + zip[n // 2]) * 0.5

    def merge(self, w, u):
        v = []
        i = 0
        j = 0
        while i < len(w) or j < len(u):
            if j == len(u) or i < len(w) and w[i] <= u[j]:
                v.append(w[i])
                i += 1
            else:
                v.append(u[j])
                j += 1
        return v
