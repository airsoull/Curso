from django.conf.urls import patterns, url

urlpatterns = patterns('products.views',
	url(r'^create/$', 'product_create', name='product_create'),
	url(r'^update/(?P<pk>\d+)/$', 'product_update', name='product_update'),
	url(r'^$', 'product_list', name='product_list'),
	url(r'^(?P<pk>\d+)-(?P<slug>[\w-]+)/$', 'product_detail', name='product_detail'),
	url(r'^(?P<slug>[\w-]+)/$', 'product_list_by_category', name='product_list_by_category'),
)