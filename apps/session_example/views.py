from django.shortcuts import render  # noqa: F401
from django.views.generic import TemplateView


class SessionExample(TemplateView):
    template_name = "session_example/session.html"

    def get_context_data(self, **kwargs):
        session = self.request.session
        count_of_visits = session.get("count_of_visits", 0)
        count_of_visits += 1
        session["count_of_visits"] = count_of_visits
        kwargs["count_of_visits"] = count_of_visits
        kwargs["session"] = session.session_key
        return kwargs


# Create your views here.
