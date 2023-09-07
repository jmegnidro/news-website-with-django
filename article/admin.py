from django.contrib import admin
from .models import Article, Category
# Register your models here.


from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'status', 'author', 'category')
    list_filter = ('status', 'category', 'author', 'date_published')
    search_fields = ('title', 'content', 'author__username', 'category__name')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-date_published',)
    date_hierarchy = 'date_published'
    readonly_fields = ('date_published', 'last_updated')

    class Media:
        css = {
            'all': ('path_to_your_custom_css.css',)
        }
        js = ('path_to_your_custom_js.js',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

