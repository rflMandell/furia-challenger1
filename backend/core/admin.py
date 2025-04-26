from django.contrib import admin
from .models import Message
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'chat', 'user', 'content', 'created_at', 'is_highlighted']
    list_filter = ('is_highlighted',)
    search_fields = ('content', 'user__username')
    
    def get_list_display(self, request):
        """ 
        Add uma marcacao para um visual diferente nas mensagens que estarao marcadas como highlight 
        """
        result = super().get_list_display(request)
        return result
    
    def is_highlighted_colored(self, obj):
        if obj.is_highlighted:
            return "Highlighted"
        return "Normal"
    is_highlighted_colored.short_description = "Highlight Status"
    is_highlighted_colored.admin_order_field = 'is_highlighted'
    
    def message_color(self, obj):
        if obj.is_highlighted:
            return '<span style="color: green;">' + obj.content + '</span>'
        return obj.content
    message_color.allow_tags = True
    message_color.short_description = 'Message'
    
#regitra a classe admin
admin.site.register(Message, MessageAdmin)