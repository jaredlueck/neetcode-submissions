class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1 if len(nums1) <= len(nums2) else nums2
        B = nums1 if len(nums1) > len(nums2) else nums2
        
        total_length = len(A) + len(B)
        half = total_length // 2
        l, r = 0, len(A)-1
        
        while True:
            i = (l + r) // 2
            j = half - i - 2
            print((i,j))
            print(half)

            # check everything on the combined left side is smaller than everything on the combined right
            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if i + 1 < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if j + 1 < len(B) else float('inf')

            # rightmost element in As left side is bigger than
            # leftmost element in Bs right side so the split is not valid
            # as we went too far in A
            if Aleft > Bright:
                r = i - 1
            elif Aright < Bleft:
                l = i + 1
            else:
                if total_length % 2 == 1:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2




            