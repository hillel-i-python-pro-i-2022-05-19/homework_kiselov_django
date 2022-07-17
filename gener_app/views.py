from django.http import HttpResponse
from .generator import gener_users


def response(request):
    amount = int(request.GET.get('amount', 100))
    resp=gener_users(amount)
    user_list=[]
    for el in resp:
        user_list.append(el.name + ' ' +el.email)
    result = '<br>'.join(user_list)
    return HttpResponse(result)
