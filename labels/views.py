from django.views.generic import TemplateView


class LabelsIndexView(TemplateView):
    template_name = 'labels/labels_index.html'