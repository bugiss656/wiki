from django.shortcuts import render, redirect
from django.contrib import messages
import re
import random


from . import util


def index(request):

    context = {
        "entries": util.list_entries()
    }

    return render(request, "encyclopedia/index.html", context)



def entryPage(request, title):
    entry = util.get_entry(title)

    if entry == None:
        return redirect("pageNotFound")
    else:
        context = {
            "title": title,
            "entry": util.convert_to_html(entry)
        }

        return render(request, "encyclopedia/entryPage.html", context)



def pageNotFound(request):
    return render(request, "encyclopedia/pageNotFound.html")



def searchEntry(request):

    if request.method == 'POST':
        search_query = request.POST['input'].casefold()

        entries = [entry.casefold() for entry in (util.list_entries())]

        if search_query in entries:
            return redirect('entry', title=search_query)
        else:
            search_results = [entry for entry in entries if entry.find(search_query) != -1]

            context = {
                'results': search_results
            }

            return render(request, "encyclopedia/searchResults.html", context)

    return render(request, "encyclopedia/searchResults.html")



def newPage(request):

    if request.method == "POST":
        page_title = request.POST['title']
        page_body = request.POST['body']

        if page_title == '' or page_body == '':
            messages.warning(request, f"Fill all the inputs.")

            return render(request, "encyclopedia/newPage.html")
        else:
            entries = [entry.casefold() for entry in util.list_entries()]

            if page_title.casefold() in entries:
                messages.warning(request, f"Provided title page already exist.")

                return render(request, "encyclopedia/newPage.html")
            else:
                util.save_entry(page_title, page_body)

                return redirect('entry', title=page_title)

    return render(request, "encyclopedia/newPage.html")



def editPage(request, title):

    page_title = title
    page_body = util.get_entry(title)

    context = {
        "title": page_title.capitalize(),
        "body": page_body.replace('\r\n', '')
    }

    return render(request, "encyclopedia/editPage.html", context)



def saveChanges(request):

    if request.method == "POST":
        page_title = request.POST['title']
        page_body = request.POST['body']

        util.save_entry(page_title, page_body)

        return redirect('entry', title=page_title)

    return render(request, "encyclopedia/editPage.html")



def randomPage(request):

    entries = [entry for entry in util.list_entries()]
    random_entry = random.choice(entries)

    return redirect('entry', title=random_entry)
