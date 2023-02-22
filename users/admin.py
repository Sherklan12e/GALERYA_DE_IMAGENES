from django.contrib import admin
from .models import User, Image
from .models import Visit

class VisitAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    list_display = ('id', 'user', 'timestamp')
    list_filter = ('user',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(user=request.user)
        return qs

    def changelist_view(self, request, extra_context=None):
        total_visits = self.get_queryset(request).count()
        context = {
            'total_visits': total_visits,
        }
        if extra_context is not None:
            context.update(extra_context)
        return super().changelist_view(request, context)

admin.site.register(Visit, VisitAdmin)
admin.site.register(User)
admin.site.register(Image)

