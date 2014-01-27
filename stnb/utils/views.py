# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from stnb.utils.utils import get_all_language_codes

class MultiTranslationFormView(TemplateView):
    model = None
    shared_form_class = None
    translation_form_class = None
    success_url = None

    def get_object(self):
        raise NotImplemented("get_object must be implemented in the sub-class")

    def post(self, request, *args, **kwargs):
        obj = self.get_object()

        form = self.get_shared_form(obj)
        trans_forms = self.get_translation_forms(obj)

        forms_valid = True
        if form.is_valid() is False:
            forms_valid = False
        for tform in trans_forms:
            if tform.has_changed() is True and tform.is_valid() is False:
                forms_valid = False

        if forms_valid:
            return self.forms_valid(form, trans_forms)
        else:
            return self.forms_invalid(form, trans_forms)
    
    def get_context_data(self, **kwargs):
        context = super(MultiTranslationFormView, self).\
                get_context_data(**kwargs)
        
        obj = self.get_object()

        form = self.get_shared_form(obj)
        trans_forms = self.get_translation_forms(obj)

        context.update({ 'object': obj,
                         'form': form, 'trans_forms': trans_forms })

        return context

    def get_success_url(self):
        if self.success_url:
            url = self.success_url % self.get_object().__dict__
        else:
            try:
                url = self.get_object().get_absolute_url()
            except AttributeError:
                raise ImproperlyConfigured(
                    "No URL to redirect to.  Either provide a url or define"
                    " a get_absolute_url method on the Model.")
        return url

    def forms_valid(self, form, trans_forms):
        obj = form.save()
        for tform in trans_forms:
            if tform.has_changed():
                trans = tform.save()
                if trans.master_id is None:
                    trans.master_id = obj.pk
                    trans.save()
        print self.request.path
        url = self.get_success_url()
        return HttpResponseRedirect(url)

    def forms_invalid(self, form, trans_forms):
        # FIXME: Remove Xerrada specific stuff out of here.
        return ''
        #return self.render_to_response(self.get_context_data(xerrada_id=form.instance.pk, seminari_slug=form.instance.seminari().slug))

    def get_shared_form_class(self):
        return self.shared_form_class

    def get_translation_form_class(self):
        return self.translation_form_class

    def get_shared_form(self, shared_obj):
        form_args = { }
        if self.request.method in ('POST', 'PUT'):
            form_args.update({ 'data': self.request.POST,
                               'files': self.request.FILES })

        form = self.get_shared_form_class()(instance=shared_obj, **form_args)
        return form

    def get_translation_forms(self, shared_obj):
        trans_forms = [ ]

        form_args = { }
        if self.request.method in ('POST', 'PUT'):
            form_args.update({ 'data': self.request.POST,
                               'files': self.request.FILES })

        for lang in get_all_language_codes():
            trans = list(shared_obj.translations.filter(language_code=lang))
            if len(trans) == 0:
                trans_form = self.get_translation_form_class()(
                                 initial={'language_code':lang},
                                 prefix='trans_'+lang,
                                 **form_args)
            else:
                trans_form = self.get_translation_form_class()(
                                 instance=trans[0],
                                 prefix='trans_'+lang,
                                 **form_args)
            trans_forms.append(trans_form)

        return trans_forms


