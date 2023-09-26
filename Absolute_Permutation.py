import itertools
def absolutePermutation(n, k):
    # Write your code here
    count = 0
    pos = []


    for j in range(n+1):
        pos.append(j)
    if k == 0:
        return pos[1:]

    if (n % 2) or (n%k)==1:
        return [-1]
    if k>n-1:
        return [-1]
    for i in range(1, n - k + 1):
        if pos[i] == pos[i+k] - k:
            pos[i],pos[i+k] = pos[k+i],pos[i]
        elif abs(i - pos[i]) != k:
            return [-1]
    return pos[1:]
    # print(permutations)


'''
    else:
        # Generate all permutations
        permutations = itertools.permutations(pos)

        found = False

        for permutation in permutations:
            count = 0
            for j in range(1,n+1):
                if (abs(permutation[j-1]-j) == k) :
                    # print(abs(permutation[j-1]-j))
                    count+=1
                else:break

            if count == n:
                ans = list(permutation)
                return ans

    return [-1]
'''



print(absolutePermutation(10,0))