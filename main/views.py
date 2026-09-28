from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
import requests

from .forms import OrderForm
from .models import Order


BOT_TOKEN = "8727572112:AAE2IbXDTICsNattqDelU-JJXLDMpYx-aVA"
CHAT_ID = "7832864166"


def home(request):
    return render(request, "main/home.html")


@csrf_exempt
def send_order(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "POST kerak"},
            status=405
        )

    try:

        data = json.loads(request.body)

        # Mijoz ma'lumotlari
        name = data.get("name", "")
        phone = data.get("phone", "")
        address = data.get("address", "")

        # Buyurtma ma'lumotlari
        items = data.get("items", [])
        total = data.get("total", 0)

        # Telegram xabari
        message = "🍔 YANGI BUYURTMA!\n\n"

        message += f"👤 Ism: {name}\n"
        message += f"📞 Telefon: {phone}\n"
        message += f"📍 Manzil: {address}\n\n"

        message += "🛒 BUYURTMA:\n\n"

        for item in items:

            message += (
                f"🍴 {item['name']}\n"
                f"📦 Soni: {item['qty']}\n"
                f"💵 Narxi: {item['price']:,} so'm\n\n"
            )

        message += f"💰 Jami: {total:,} so'm"

        # Telegram API
        url = (
            f"https://api.telegram.org/"
            f"bot{BOT_TOKEN}/sendMessage"
        )

        response = requests.post(
            url,
            json={
                "chat_id": CHAT_ID,
                "text": message
            },
            timeout=10
        )

        if not response.ok:

            return JsonResponse({
                "success": False,
                "error": response.text
            }, status=400)

        return JsonResponse({
            "success": True
        })

    except Exception as e:

        return JsonResponse({
            "success": False,
            "error": str(e)
        }, status=400)


def checkout(request):

    if request.method == "POST":

        form = OrderForm(request.POST)

        if form.is_valid():

            order = form.save()

            return redirect("success")

    else:

        form = OrderForm()

    return render(
        request,
        "checkout.html",
        {
            "form": form
        }
    )


def success(request):
    return render(request, "main/success.html")