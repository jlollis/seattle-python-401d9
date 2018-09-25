from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator
from django.conf import settings
from .models import Review


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def review_list_view(request):
    reviews_query = get_list_or_404(Review)
    paginator = Paginator(reviews_query, 20)

    page = request.GET.get('page')
    reviews = paginator.get_page(page)

    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/review_list.html', context)


def review_detail_view(request, pk):
    context = {
        'review': get_object_or_404(Review, id=pk),
    }

    return render(request, 'reviews/review_detail.html', context)
