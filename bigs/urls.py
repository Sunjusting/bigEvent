from django.conf.urls import url
from bigs import views as bigs_views

urlpatterns = [
    url(r'^$',bigs_views.index,name="bigs-index"),
    url(r'^add/$',bigs_views.add,name="bigs-add"),
    url(r'^(\d+)/edit/$',bigs_views.edit,name="bigs-edit"),
    url(r'^show/(\d+)/$',bigs_views.show,name="bigs-show"),
    url(r'^references/$',bigs_views.references,name="bigs-references"),
    url(r'^addRefs/$',bigs_views.addRefs,name="bigs-addRefs"),

]
