from django.urls import include, path

urlpatterns = [
    path('', include('anmelde_tool.event.urls')),
    path('', include('anmelde_tool.registration.urls')),
    path('', include('anmelde_tool.event.summary.urls')),
    path('choices/', include('anmelde_tool.event.choices.urls')),
    path('cash/', include('anmelde_tool.event.cash.urls')),
    path('', include('anmelde_tool.event.file_generator.urls')),
    path('', include('anmelde_tool.event.email.urls')),
    path('', include('anmelde_tool.attributes.urls'))
]
