from django.http import HttpResponse

from .generator import generate_users


def response(request):
    amount = int(request.GET.get('amount', 100))
    generator_object = generate_users(amount)
    user_list = [f'{el.name} {el.email}' for el in generator_object]
    result = '<br>'.join(user_list)
    return HttpResponse(result)
