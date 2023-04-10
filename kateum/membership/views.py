# from datetime import time
#
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# import stripe
# from django.conf import settings
# from django.views.decorators.csrf import csrf_exempt
#
#
# # Create your views here.
#
# # stripe.api_key = "sk_test_51JcAnkLClbNcoX7MggiGXmcL5xHeMa91ciudfBaFwjWL7JzFOsrLepHfZXhvR7hKopQZGTO2NBedZFFa22pT8Xy900sxnFYk8a"
#
#
# def membership(request):
#     return render(request, "membership/membership.html")
#
# def cards(request):
#     return render(request, "membership/cards.html")
#
# def checkout(request):
#     # prices = stripe.Price.list(
#     #     lookup_keys=[request.form['lookup_key']],
#     #     expand=['data.product']
#     # )
#
#     checkout_session = stripe.checkout.Session.create(
#
#         line_items=[
#             {
#                 'price': 'price_1MsR7dLClbNcoX7Mfvz16tAD',
#                 'quantity': 1,
#
#             },
#             # {
#             #     'price': 'price_1MsR8KLClbNcoX7MiLAJ5rU5',
#             #     'quantity': 1,
#             # }
#         ],
#         mode='subscription',
#         success_url='http://127.0.0.1:8000',
#         cancel_url='http://127.0.0.1:8000',
#     )
#     return redirect(checkout_session.url, code=303)
#
#
# @login_required(login_url="login")
# def product_page(login_url='login'):
#     stripe.api_key = settings.STRIPE_SECRET_KEY
#     if request.method == 'POST':
#         checkout_session = stripe.checkout.Session.create(
#             payment_method_types = ['card'],
#             line_items=[
#                 {
#                     'price': 'price_1MsR7dLClbNcoX7Mfvz16tAD',
#                     'quantity': 1,
#
#                 },
#             ],
#             mode='subscription',
#             success_url=settings.REDIRECT_DOMAIN +
#                         '/success.html?session_id={CHECKOUT_SESSION_ID}',
#             cancel_url=settings.REDIRECT_DOMAIN + '/payment_cancelled.html',
#         )
#         return redirect(checkout_session.url, code=303)
#     return render(request, 'user_payment/product_page.html')
#
#
# def payment_successful(request):
# 	stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
# 	checkout_session_id = request.GET.get('session_id', None)
# 	session = stripe.checkout.Session.retrieve(checkout_session_id)
# 	customer = stripe.Customer.retrieve(session.customer)
# 	user_id = request.user.user_id
# 	user_payment = UserPayment.objects.get(app_user=user_id)
# 	user_payment.stripe_checkout_id = checkout_session_id
# 	user_payment.save()
# 	return render(request, 'user_payment/payment_successful.html', {'customer': customer})
#
#
# def payment_cancelled(request):
# 	stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
# 	return render(request, 'user_payment/payment_cancelled.html')
#
#
# @csrf_exempt
# def stripe_webhook(request):
# 	stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
# 	time.sleep(10)
# 	payload = request.body
# 	signature_header = request.META['HTTP_STRIPE_SIGNATURE']
# 	event = None
# 	try:
# 		event = stripe.Webhook.construct_event(
# 			payload, signature_header, settings.STRIPE_WEBHOOK_SECRET_TEST
# 		)
# 	except ValueError as e:
# 		return HttpResponse(status=400)
# 	except stripe.error.SignatureVerificationError as e:
# 		return HttpResponse(status=400)
# 	if event['type'] == 'checkout.session.completed':
# 		session = event['data']['object']
# 		session_id = session.get('id', None)
# 		time.sleep(15)
# 		user_payment = UserPayment.objects.get(stripe_checkout_id=session_id)
# 		user_payment.payment_bool = True
# 		user_payment.save()
#     return HttpResponse(status=200)
#
#
