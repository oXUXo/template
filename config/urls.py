from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
# from home.sitemaps import PostSitemap

# sitemaps = {
#     'posts': PostSitemap,
# }

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('product/', include('product.urls', namespace='product')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', include('home.urls', namespace='home')),
    path(
        'about/',
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    path(
        "thanks/",
        TemplateView.as_view(template_name="pages/thanks.html"),
        name="thanks",
    ),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
