from django.urls import path

from . import views

urlpatterns = [
    path("assessmonth/", views.assessmonthinfo, name='assessmonth'),
    path("assess/", views.assessinfo, name='assess'),
    path("assessdata/", views.assessdatainfo, name='assessdata'),
    path("attence/", views.attenceinfo, name='attence'),
    path("managermark/", views.managermarkinfo, name='managermark'),
    path("managermarkdata/", views.managermarkdatainfo, name='managermarkdata'),
    path("markname/", views.marknameinfo, name='markname'),
    path("table/", views.tableinfo, name='table'),
    path("download/", views.downloadinfo, name='download'),
    path("compute/", views.computeinfo, name='compute'),
    path("manageruseropen/", views.manageruseropeninfo, name='manageruseropen'),
    path("kpiuseropen/", views.kpiuseropeninfo, name='kpiuseropen'),
    path("manageruserreset/", views.manageruserresetinfo, name='manageruserreset'),
    path("kpiuserreset/", views.kpiuserresetinfo, name='kpiuserreset'),
    path("manageropenreceive/", views.manageropenreceiveinfo, name='manageropenreceive'),
    path("kpiopenreceive/", views.kpiopenreceiveinfo, name='kpiopenreceive'),
    path("", views.index, name='index')
]