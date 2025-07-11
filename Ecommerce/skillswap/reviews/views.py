from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def add_review(request, username):
    target_user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.reviewee = target_user
            review.save()
            return redirect('accounts:profile')
    else:
        form = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form': form, 'target_user': target_user})