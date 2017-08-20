from django.conf.urls import url
from bigs import views as bigs_views

urlpatterns = [
    url(r'^$',bigs_views.index,name="bigs-index"),
    url(r'^add/$',bigs_views.add,name="bigs-add"),
    url(r'^(\d+)/edit/$',bigs_views.edit,name="bigs-edit"),
    url(r'^show/(\d+)/$',bigs_views.show,name="bigs-show"),
    url(r'^references/$',bigs_views.references,name="bigs-references"),
    url(r'^addRef/$',bigs_views.addRef,name="bigs-addRef"),
    url(r'^(\d+)/editRef/$',bigs_views.editRef,name="bigs-edit-ref"),
    url(r'^(\d+)/delRef/$',bigs_views.delRef,name="bigs-del-ref"),
    url(r'^(\d+)/showRef/$',bigs_views.showRef,name="bigs-show-ref"),

]
