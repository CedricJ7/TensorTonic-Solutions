def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    tp = 0
    fp = 0
    fn = 0
    for i in range(len(y_pred)):
        for classe in set(y_true):
            if y_pred[i] == classe and y_true[i] == classe:
                tp+=1
            if y_pred[i] == classe and y_true[i] != classe:
                fp +=1
            if y_pred[i] != classe and y_true[i] == classe:
                fn +=1
    return(float(2*tp/(2*tp+fp+fn)))