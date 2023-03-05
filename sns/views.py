from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from .forms import LoginForm, RegisterForm, ProfileForm, ChangePassword
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from .models import Post, ExtendUser, Comment

# Create your views here.
from django.views.generic import FormView, CreateView, UpdateView, TemplateView


class MainView(View):
    """ Shows the first page after entering the website """
    def get(self, request):
        return render(request, 'main.html')


# class WallView(FormView):
#     template_name = "wall_action.html"
#     form_class = AddPostForm
#     success_url = reverse_lazy("wall")
#
#     def get_context_data(self, **kwargs):
#         posts = Post.objects.order_by("-created_on")
#         context = super(WallView, self).get_context_data(**kwargs)
#         context['posts'] = posts
#         return context
#
#     def form_valid(self, form):
#         body = form.cleaned_data['body']
#         image = form.cleaned_data['image']
#         user = User.objects.get(id=self.request.user.id)
#
#         Post.objects.create(author=user, body=body, image=image)
#         return redirect(self.success_url)


# class WallView(LoginRequiredMixin, View):
class WallView(LoginRequiredMixin ,View):
    """ Shows the wall of the site """
    def get(self, request):
        posts = Post.objects.order_by("-created_on")
        ctx = {'posts': posts}
        return render(request, "wall_action.html", ctx)

    def post(self, request):
        body = request.POST.get("textarea")
        if body:
            user = request.user.id
            author = User.objects.get(pk=user)
            Post.objects.create(author=author, body=body)
            return redirect("/wall/")


class LoginView(FormView):
    """ Lets to log into the social service"""
    form_class = LoginForm
    template_name = "login.html"
    success_url = reverse_lazy("wall")

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['name'],
                            password=form.cleaned_data['pw'])
        if user is not None:
            login(self.request, user)
            return redirect(self.success_url)
        else:
            return redirect(reverse_lazy('login'))


class LogoutView(FormView):
    """ Logs a logged-in person out"""
    def get(self, request):
        logout(request)
        return redirect(reverse("main"))


class RegisterView(FormView):
    """ Registers a new member """
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('wall')

    def form_valid(self, form):
        name = form.cleaned_data['first_name']
        surname = form.cleaned_data['last_name']
        pw = form.cleaned_data['password']
        email = form.cleaned_data['email']
        print(email)
        new_user = User.objects.create_user(username=email,
                                            first_name=name,
                                            last_name=surname,
                                            password=pw,
                                            email=email)

        new_user_extend = ExtendUser.objects.create(user=new_user)
        login(self.request, new_user)
        # return redirect(self.success_url)

        return super().form_valid(form)


class SettingsView(LoginRequiredMixin, View):
    """ Shows settings' view """
    def get(self, request):
        user_id = request.user.id
        user = User.objects.get(pk=user_id)
        return render(request, 'settings_base.html', {"user": user})

    def self(self, request):
        pass


class ProfileView(LoginRequiredMixin, View):
    """ Shows a person's data"""
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        return render(request, 'your_profile.html', {'user': user})


class EditProfileView(LoginRequiredMixin, UpdateView):
    """ Edits a person's data"""
    form_class = ProfileForm
    template_name = "edit_your_profile.html"
    success_url = reverse_lazy('settings')

    def get_object(self, queryset=None):
        return get_object_or_404(User, id=self.request.user.id)


class ChangePasswordView(LoginRequiredMixin, FormView):
    """ Changes password """
    form_class = ChangePassword
    template_name = 'change_password.html'
    success_url = reverse_lazy("settings")

    def form_valid(self, form):
        user = get_object_or_404(User, id=self.request.user.id)
        user.set_password(form.cleaned_data['pw1'])
        user.save()
        update_session_auth_hash(self.request, user)
        return redirect(self.success_url)


class FriendsView(View):
    """ Shows lists of friends and to-be-friends"""
    def get(self, request):
        all_users = User.objects.all()
        user = User.objects.get(pk=request.user.id)
        friends = user.extenduser.friends.all()
        friends_to_be = []
        for person in all_users:
            if person.id != request.user.id:
                if user.extenduser not in person.extenduser.friends.all():
                    friends_to_be.append(person)

        return render(request, 'friends.html', {"friends_to_be": friends_to_be, "friends": friends})


def add_friend_view(request, id_):
    """ Adds a person to friends """
    logged_user = User.objects.get(pk=request.user.id)
    added_user = User.objects.get(pk=id_)
    added_user_extend = ExtendUser.objects.get(user=added_user)
    logged_user.extenduser.friends.add(added_user_extend)

    return redirect("friends")


def delete_friend_view(request, id_):
    """ Deletes a given person from friends """
    logged_user = User.objects.get(pk=request.user.id)
    deleted_user = User.objects.get(pk=id_)
    logged_user_extend = ExtendUser.objects.get(user=logged_user)
    added_user_extend = ExtendUser.objects.get(user=deleted_user)
    logged_user.extenduser.friends.remove(added_user_extend)

    return redirect("friends")


def like_view(request, pk):
    """ Increases or decreases the number of likes """
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect('/wall/')


class CommentView(LoginRequiredMixin, FormView):
    """ Adds a comment to database """
    def get(self, request, id_):
        comments = Comment.objects.filter(post=id_)
        return render(request, 'comment.html', {'comments': comments})

    def post(self, request, id_):
        text = request.POST.get('text')
        if text:
            post = Post.objects.get(id=id_)
            user = User.objects.get(id=request.user.id)
            Comment.objects.create(author=user, content=text, post=post)
            return redirect("wall")
        else:
            error = "Fill out the comment input"
            return render(request, 'comment.html', {'error': error})


def play_view(request):
    return render(request, 'play.html')

