from django.contrib import admin
from .models import Activity

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id','user','activity_type','duration_in_minutes','distance_in_kilometers','calories_burned_display')
    list_filter = ('user', 'activity_type','date')
    search_fields = ('user__username', 'activity_type')
    ordering = ('-date',)
    date_hierarchy = 'date'

    def duration_in_minutes(self, obj):
        return f'{obj.duration} mins'
    duration_in_minutes.short_description = 'Duration (mins)'

    def distance_in_kilometers(self, obj):
        return f'{obj.distance} km' if obj.distance else 'N/A'
    distance_in_kilometers.short_description = 'Distance (km)'

    def calories_burned_display(self, obj):
        return f'{obj.calories_burned} cal' if obj.calories_burned is not None else 'N/A'
    calories_burned_display.short_description = 'Calories Burned'

fieldsets = (
    (None, {'fields': ('user', 'activity_type', 'duration', 'distance', 'calories_burned')}),
    ('Date', {'fields': ('date',)}),
)    

admin.site.register(Activity, ActivityAdmin)