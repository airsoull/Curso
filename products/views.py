from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Product, Category
from .forms import ProductForm


class ProductList(ListView):
	model = Product

product_list = ProductList.as_view()


class ProductListByCategory(ProductList):
	
	def dispatch(self, request, slug):
		self.category = get_object_or_404(Category, slug=slug)
		return super(ProductListByCategory, self).dispatch(request=request, slug=slug)

	def get_context_data(self, object_list):
		context = super(ProductListByCategory, self).get_context_data(object_list=object_list)
		context['category'] = self.category
		return context

	def get_queryset(self):
		return super(ProductListByCategory, self).get_queryset().filter(category=self.category)


product_list_by_category = ProductListByCategory.as_view()


class ProductDetail(DetailView):
	model = Product

product_detail = ProductDetail.as_view()


class ProductCreate(CreateView):
	form_class = ProductForm
	template_name = 'products/form_product.html'

	@method_decorator(login_required)
	def dispatch(self, request):
		return super(ProductCreate, self).dispatch(request=request)

product_create = ProductCreate.as_view()


class ProductUpdate(UpdateView):
	model = Product
	form_class = ProductForm
	template_name = 'products/form_product.html'

product_update = ProductUpdate.as_view()