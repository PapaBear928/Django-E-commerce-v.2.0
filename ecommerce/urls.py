import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('ecommerce.apps.store.urls', namespace='store')),
	path('cart/', include('ecommerce.apps.cart.urls', namespace='cart')),
	path('payment/', include('ecommerce.apps.payment.urls', namespace='payment')),
	path('account/', include('ecommerce.apps.account.urls', namespace='account')),
	path('orders/', include('ecommerce.apps.orders.urls', namespace='orders')),
	path('blog/', include('ecommerce.apps.blog.urls', namespace='blog')),
	path('__debug__/', include('debug_toolbar.urls')),
	path('api/schema/', SpectacularAPIView.as_view(), name='api_schema'),
	path('api/docs/', SpectacularSwaggerView.as_view(url_name='api_schema'),name='api_docs'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
