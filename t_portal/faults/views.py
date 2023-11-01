from django.shortcuts import render


def tfaults(request):
    return render(request, 'faults/tFaults.html')


def taccounts(request):
    return render(request, 'faults/tAccounts.html')
