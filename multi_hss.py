def multi_hss(matrix):
    matrix = tuple([tuple(row) for row in matrix])
    matrices_by_class =[[[],[]] for row in matrix]
    
    for i in range(len(matrix)):
        TP = matrix[i][i]

        FP = [row[i] for row in matrix]
        del FP[i]
        FP = sum(FP)

        FN = list(matrix[i])
        del FN[i]
        FN = sum(FN)

        TN = [list(row) for row in matrix]
        del TN[i]
        for row in TN: del row[i]
        add = 0
        for row in TN: add += sum(row)
        TN = add
        matrices_by_class[i] = [[TP, FN],
                                [FP, TN]]

    scores = []
    for i, mat in enumerate(matrices_by_class):
        a, b, c, d = (mat[0][0], mat[0][1], mat[1][0], mat[1][1])
        scores.append(2 * (a*d - b*c) / ((a+c)*(c+d) + (a+b)*(b+d)))

    return scores
