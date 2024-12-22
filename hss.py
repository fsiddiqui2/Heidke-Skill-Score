import sklearn.metrics
def HSS(pred, true):
    mat = metrics.confusion_matrix(true, pred, labels=[1,0])
    a, b, c, d = (mat[0][0], mat[0][1], mat[1][0], mat[1][1])
    skill_score = 2*(a*d - b*c) / ((a+c)*(c+d) + (a+b)*(b+d))
    return skill_score
