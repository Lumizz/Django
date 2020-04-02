def prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title):
    import pickle
    pclass = 3
    sex = 0
    sibsp = 0
    parch = 0
    fare = 10
    embarked = 1
    title = 0
    x = [[pclass,sex,age,sibsp,parch,fare,embarked,title]]
    randomforest = pickle.load(open('titanic_model.sav','rb'))
    predictions = randomforest.predict(x)
    if predictions == 1:
        predictions = 'Survived'
    elif predictions == 0:
        predictions = 'Not Survived'
    else:
        predictions = 'Error'
    return predictions
