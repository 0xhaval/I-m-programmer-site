from django.shortcuts import render
from . import models

def material(request):
    data1 = models.FirstSatage.objects.all()
    data2 = models.SecondStage.objects.all()
    data3 = models.ThirdStage.objects.all()
    data4 = models.ForthStage.objects.all()
    return render(request, 'material.html', {'object1': data1,
                                            'object2': data2,
                                            'object3': data3,
                                            'object4': data4
                                            })

def mat_resource(request):
    data1 = models.FirstSatage.objects.all()
    data2 = models.SecondStage.objects.all()
    data3 = models.ThirdStage.objects.all()
    data4 = models.ForthStage.objects.all()
    return render(request, 'resources.html', {'object1': data1,
                                            'object2': data2,
                                            'object3': data3,
                                            'object4': data4
                                            })


def mat_course(request):
    data1 = models.FirstSatage.objects.all()
    data2 = models.SecondStage.objects.all()
    data3 = models.ThirdStage.objects.all()
    data4 = models.ForthStage.objects.all()
    return render(request, 'courses.html', {'object1': data1,
                                            'object2': data2,
                                            'object3': data3,
                                            'object4': data4
                                            })

