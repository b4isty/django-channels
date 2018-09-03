from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.generic import DetailView, ListView


from .models import Thread, ChatMessage


class InboxView(LoginRequiredMixin, ListView):
    template_name = 'chat/inbox.html'
    def get_queryset(self):
        return Thread.objects.by_user(self.request.user)