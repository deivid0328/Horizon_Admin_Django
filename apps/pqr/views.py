from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PQRForm
from .models import PQR


def landing_login(request):
    if request.method == "POST":
        email = (request.POST.get("email") or "").strip().lower()
        password = request.POST.get("password") or ""
        errors = []

        if not email:
            errors.append("El correo electrónico es obligatorio.")
        else:
            try:
                validate_email(email)
            except ValidationError:
                errors.append("Ingresa un correo electrónico válido.")

        if not password:
            errors.append("La contraseña es obligatoria.")

        if errors:
            return render(request, "landing_login.html", {"errors": errors, "email": email})

        user_model = get_user_model()
        username = email.split("@", 1)[0]
        user, _ = user_model.objects.get_or_create(email=email, defaults={"username": username})
        user.username = username
        user.set_password(password)
        user.save(update_fields=["username", "password"])

        login(request, user)
        next_url = request.GET.get("next") or "pqr_list"
        return redirect(next_url)

    return render(request, "landing_login.html")


@login_required(login_url="landing_login")
def pqr_list(request):
    pqr = PQR.objects.all()
    return render(request, "pqr/pqr_list.html", {"pqr": pqr})


@login_required(login_url="landing_login")
def pqr_create(request):
    form = PQRForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("pqr_list")
    return render(request, "pqr/pqr_create.html", {"form": form})


@login_required(login_url="landing_login")
def pqr_detail(request, id):
    pqr = get_object_or_404(PQR, id=id)
    return render(request, "pqr/pqr_detail.html", {"pqr": pqr})


@login_required(login_url="landing_login")
def pqr_delete(request, id):
    pqr = get_object_or_404(PQR, id=id)
    pqr.delete()
    return redirect("pqr_list")