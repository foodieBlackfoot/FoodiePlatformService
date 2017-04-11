from FoodieApp.models import FoodProvider, Customer

def create_user_by_type(backend, user, response, *args, **kwargs):
    request = backend.strategy.request_data()
    if backend.name == 'facebook':
        avatar = 'http://graph.facebook.com/%s/picture?type=large' % response['id']
    else:
        avatar = ''
    if request['user_type'] == 'food_provider' and not FoodProvider.objects.filter(User_id = user.id):
        FoodProvider.objects.create(User_id = user.id)
    elif request['user_type'] == 'customer' and not Customer.objects.filter(User_id = user.id):
        Customer.objects.create(User_id = user.id, Avatar = avatar)
