import django_filters
from datetimewidget.widgets import DateTimeWidget

from management_app.models import FesClass

"""
Created by Wenqiang Kuang

Used by exteranl library django-filter, generating a search form.
"""


class ClassFilter(django_filters.FilterSet):
    class Meta:
        model = FesClass

        fields = ('start', 'end', 'class_trainer', )

        widgets = {
            'start': DateTimeWidget(attrs={'id': "start_end"}, usel10n=True,
                                    bootstrap_version=3),
            'end': DateTimeWidget(attrs={'id': "start_end"}, usel10n=True,
                                  bootstrap_version=3),
        }
