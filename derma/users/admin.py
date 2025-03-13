from django.contrib import admin
from .models import QuizResponse

@admin.register(QuizResponse)
class QuizResponseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'user', 
        'primary_skin_concern', 
        'skin_type', 
        'breakout_frequency', 
        'reaction_to_skincare', 
        'redness_inflammation',
        'sunscreen_usage',
        'skin_conditions',
        'after_washing_skin_feel',
        'water_intake',
        'dark_spots_pigmentation',
        'visible_pores',
        'exfoliation_frequency',
        'fine_lines_wrinkles',
        'dairy_processed_food_intake',
        'skincare_routine',
        'submitted_at'
    )
    search_fields = ('user__username', 'primary_skin_concern', 'skin_type', 'reaction_to_skincare')
    list_filter = ('primary_skin_concern', 'skin_type', 'reaction_to_skincare', 'submitted_at')
    ordering = ('-submitted_at',)
    readonly_fields = ('submitted_at',)  # Prevent accidental changes
    date_hierarchy = 'submitted_at'  # Enable date-based filtering
