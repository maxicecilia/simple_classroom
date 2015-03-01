# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View
from simple_classroom.apps.bibliography.models import Book, GroupCategory


class BibliographyView(View):
    template_name = 'bibliography/default.html'

    def get(self, request, *args, **kwargs):
        result = list()
        categories = GroupCategory.objects.all()
        for category in categories:
            result.append({
                'category': category,
                'books': category.book_set.filter(subject=request.site.subject),
            })
        return render_to_response(
            self.template_name,
            RequestContext(self.request, {
                'bibliography': result,
            })
        )
