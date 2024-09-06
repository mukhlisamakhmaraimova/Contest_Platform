import subprocess
from django.shortcuts import render
from .models import Masala, Test_case
from .forms import Checker
from django.contrib.auth.decorators import login_required
from .forms import Checker
# Create your views here.



def Tasks(request):
    data = Masala.objects.all()
    return render(request, 'masalalar/masalalar.html', {'tasks': data})

@login_required()


def Task(request, id):
    task = Masala.objects.get(id=id)
    return render(request, 'masalalar/masala.html', {'task': task})


def Result(request, id):
    task = Masala.objects.get(id=id)
    if request.method == 'POST':
        code = request.POST['code']
        tests = list(Test_case.objects.filter(task__id=id))
        print(tests)
        count = 0
        for i in range(len(tests)):
            try:
                result = subprocess.run(["python", "-c", code], input=tests[i].example_input, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
                status = 'Runtime Error'
                if result.returncode == 0:
                    result_text = result.stdout[:-1]
                    a = [result_text, task.example_output]
                    print(a)
                    if tests[i].example_output.strip() == result_text:
                        count += 1
                    else:
                        status = f'Wrong Answer Test-{i+1}'
                        break
                else:
                    result_text = result.stderr
                    status = 'Compiler Error'
                    break
            except subprocess.TimeoutExpired:
                result_text = "Code exucution timed out (5 seconds)"
                break
        if count == len(tests):
            status = 'Accepted'
        return render(request, 'masalalar/natija.html', {'task':task, 'code': code, 'result': result_text, 'status': status})
    return render(request, 'masalalar/masala.html', {'task': task})