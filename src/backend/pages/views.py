from typing import Any, Dict
from django.views.generic import TemplateView

from .context import services, about_us, cases



class HomePageView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['services'] = services
        context['about_us'] = about_us

        context['cases'] = cases


        return context
    
