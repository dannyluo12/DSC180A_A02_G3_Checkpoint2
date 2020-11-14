def model(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix[0])        
    # transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] 

    # reverse each row if clockwise

    for i in range(n):
        matrix[i].reverse()

    # reverse each column if counter-clockwise
    '''
    for i in range(n):
        for k in range(n//2):
            print(k,i)
            matrix[k][i],matrix[n-k-1][i]=matrix[n-k-1][i],matrix[k][i]
    '''
    return matrix

def main():
    model()


if __name__ == '__main__':
    main()