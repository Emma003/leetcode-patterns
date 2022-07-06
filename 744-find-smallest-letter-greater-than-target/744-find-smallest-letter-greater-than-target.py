class Solution:
    def nextGreatestLetter(self, arr: List[str], key: str) -> str:
          if key >= arr[-1] or key<arr[0]:
            return arr[0]

          l, r = 0, len(arr)-1

          while (l<=r):
            mid = (l+r)//2

            if key>=arr[mid]:
              l=mid+1
            else:
              r=mid-1

          # TODO: Write your code here
          return arr[l]