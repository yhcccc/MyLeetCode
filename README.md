# MyLeetCode
@yhcc
in python3
##### EAST -> MEDIUM -> HARD

----------------------------------------
* Sum problem: 1,15,16,18. 
* Backtrack: 39&40,46&47
See <https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)>  
* Linked list: 2,19,21,24,61  
* Stack: 20,22,71,  
* **StrStr(KMP\BM\Sunday algorithm): 28**  
* Divide and conquer;Binary search: 32,33,34(BoundaryOpt),35(easy),53,74  
Boundary problem:<https://blog.csdn.net/u011523762/article/details/50878613>  
```
int search4(int array[], int n, int v)
{
    int left, right, middle;
    left = -1, right = n;
    while (left + 1 != right)
    {
        middle = left + （right － left) / 2;
        if (array[middle] < v)
        {
            left = middle;
        }
        else
        {
            right = middle;
        }
    }
    if (right >= n || array[right] != v)
    {
        right = -1;
    }
    return right;
}
```
* Sliding window method(Two pointer): 3,11,  
* Gragh: 56,  
* **Dynamic planing vs Recursion: 5(LongestCommonSubstring),22,32,50,55,62&63,64,70**  
* Interesting or Special problem: 5(Manacher's),6,11,12&13,17,29(BitOperation),31,36,48,54&59,55,853  
