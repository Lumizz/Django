from django.shortcuts import render
from . import machine_learning_model
from . import prediction_model

def home(request):
    return render(request,'index.html')


def result(request):
    user_input_age = int(request.GET['age'])
    #prediction = fake_model.fake_predict(user_input_age)
    prediction = prediction_model.prediction_model(1,1,user_input_age,2,1,50,2,1)
    #user_input = machine_learning_model.multiplier(user_input)
    #return render(request,'result.html',{'home_input':user_input})
    return render(request, 'result.html',{'prediction':prediction})
