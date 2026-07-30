from hashlib import new
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import uuid
from .models import User, comment, listing, bids, selled


def index(request):
    if request.method == "POST":
        ub = request.POST["boolean"]
        ui = request.POST["id"]
        listings = listing.objects.get(id=ui, fav=ub)
        if listings.fav == False:
            listings.fav = True
            listings.save()
        elif listings.fav == True:
            listings.fav = False
            listings.save()
        dt = listing.objects.filter(user=request.user, fav=True)
        return render(request, "auctions/watchlist.html", {
            "dt": dt
        })

    else:
        dt = listing.objects.all
        return render(request, "auctions/index.html", {
            "dt": dt
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required(login_url='login')
def creat(request):
    if request.method == "POST":
        tit = request.POST["title"]
        bid = request.POST["bid"]
        des = request.POST["des"]
        img = request.POST["url"]
        ctg = request.POST["ctg"]
        if tit and bid and des and ctg:
            listings = listing()
            listings.t = tit
            listings.description = des
            listings.start_bid = bid
            listings.current = bid
            listings.ctg = ctg
            listings.img = img
            listings.user = request.user
            listings.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/creat.html")


def categories(request):
    ctgg = request.POST["ctg"]
    if ctgg:
        dt = listing.objects.filter(ctg=ctgg)
        return render(request, "auctions/categories.html", {
            "dt": dt,
            "ctg": ctgg
        })
    else:
        return render(request, "auctions/categories.html", {
            "dt": "it didnt work",
        })


@login_required(login_url='login')
def watchlist(request):
    if request.method == "POST":
        ub = request.POST["boolean"]
        ui = request.POST["id"]
        listings = listing.objects.get(id=ui, fav=ub)
        if listings and listings.fav == True:
            listings.fav = False
            listings.save()
            return render(request, "auctions/watchlist.html")
        else:
            return render(request, "auctions/watchlist.html")

    else:
        dt = listing.objects.filter(fav=True)
        return render(request, "auctions/watchlist.html", {
            "dt": dt
        })


@login_required(login_url='login')
def listings(request):
    if request.method == "POST" and "bid-v" in request.POST:
        id = request.POST.get("foreign")
        dt = listing.objects.filter(id=id)
        for i in dt:
            id = i
        new = request.POST.get("new")
        cu = request.POST.get("hide")
        if new > cu:
            bidss = bids()
            bidss.bid = new
            bidss.listings = id
            bidss.userbid = request.user
            bidss.save()
            lld = request.POST["foreign"]
            listings = listing.objects.get(id=lld)
            listings.current = new
            listings.save()
            dt = listing.objects.filter(id=lld)
            dc = comment.objects.filter(listingcmnt=id)
            return render(request, "auctions/listing.html", {
                "data": dt,
                "dc": dc
            })
        else:
            lld = request.POST.get("foreign")
            dt = listing.objects.filter(id=lld)
            return render(request, "auctions/listing.html", {
                "data": dt,
                "error": "bid should be heigher then current bid"
            })

    elif request.method == "POST" and "comment-v" in request.POST:
        id = request.POST.get("cf")
        ck = request.POST['csrfmiddlewaretoken']
        dt = listing.objects.filter(id=id)
        for i in dt:
            id = i
        cm = request.POST.get("cmnt")
        check = comment.objects.filter(chk=ck)
        for i in check:
            check = i.chk

        if check != ck:
            cmntt = comment()
            cmntt.chk = ck
            cmntt.cmnt = cm
            cmntt.listingcmnt = id
            cmntt.usercmnt = request.user
            cmntt.save()
        dc = comment.objects.filter(listingcmnt=id)

        return render(request, "auctions/listing.html", {
            "data": dt,
            "dc": dc
        })
    else:
        id = request.GET["id"]
        dt = listing.objects.filter(id=id)
        dc = comment.objects.filter(listingcmnt=id)
        return render(request, "auctions/listing.html", {
            "data": dt,
            "dc": dc
        })


@login_required(login_url='login')
def my_listing(request):
    if request.method == "POST" and "sell" in request.POST:
        s = request.POST["ls"]
        ffl = listing.objects.filter(id=s)
        for i in ffl:
            us = i.user
            st = i.start_bid
            cb = i.current
        b = request.POST["buyer"]
        fs = bids.objects.filter(bid=b)
        for i in fs:
            fs = i.userbid
        tit = request.POST["tit"]
        dis = request.POST["dis"]
        im = request.POST["im"]
        if cb > st:
            sold = selled()
            sold.t = tit
            sold.description = dis
            sold.img = im
            sold.salle_price = b
            sold.touser = fs
            sold.salles = us
            sold.save()
            dele = listing.objects.get(id=s)
            dele.delete()
        dli = listing.objects.filter(user=request.user)
        return render(request, "auctions/my_listing.html", {
            "dt": dli
        })
    elif request.method == "POST" and "delete" in request.POST:
        d = request.POST["d"]
        dele = listing.objects.get(id=d)
        dele.delete()
        dli = listing.objects.filter(user=request.user)
        return render(request, "auctions/my_listing.html", {
            "dt": dli
        })
    else:
        dt = listing.objects.filter(user=request.user)
        return render(request, "auctions/my_listing.html", {
            "dt": dt
        })


@login_required(login_url='login')
def salles(request):
    ss = selled.objects.filter(salles=request.user)
    bb = selled.objects.filter(touser=request.user)
    return render(request, "auctions/salles.html", {
        "ds": ss,
        "db": bb
    })
