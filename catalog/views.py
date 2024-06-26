from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        products = Product.objects.all()

        for product in products:
            versions = Version.objects.filter(product=product)
            active_versions = versions.filter(is_current=True)
            if active_versions:
                product.active_version = active_versions.last().name
            else:
                product.active_version = 'Нет активной версии'

        context_data['object_list'] = products
        return context_data

class ContactPageView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        product = self.get_object()

        versions = Version.objects.filter(product=product)
        active_versions = versions.filter(is_current=True).last()
        if active_versions:
            product.active_version = active_versions.name
        else:
            product.active_version = 'Нет активной версии'

        context_data['version'] = product.active_version
        context_data['version_list'] = versions

        return context_data


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']

        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
