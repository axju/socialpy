from django.contrib import admin
from django.contrib import auth
from socialpy.server.data.models import Category, Post, PostOn#, PostCategory

class PostOnInline(admin.TabularInline):
    fields = ('created', 'network')
    readonly_fields = ['network', 'created']
    model = PostOn
    can_delete = False
    extra = 0

    def has_add_permission(self, request):
        return False

#class PostCategoryInline(admin.TabularInline):
#    model = PostCategory
#    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'admin_posts_new', 'admin_posts_total')

    def admin_posts_total(self, obj):
        return obj.posts.all().count()
    admin_posts_total.short_description = 'Posts total'

    def admin_posts_new(self, obj):
        return obj.posts.filter(status='new').count()
    admin_posts_new.short_description = 'Posts new'

class PostAdmin(admin.ModelAdmin):
    fields = ('status', 'created', 'text', 'image', 'categorys')
    readonly_fields = ['created']
    inlines = [PostOnInline, ]

    list_display = ('__str__', 'status', 'post_on', 'created', 'admin_categorys', 'check_text', 'check_image')
    list_filter = ('status', 'categorys')

    def check_text(self, obj):
        return obj.text != ''
    check_text.boolean = True
    check_text.short_description = 'Text'

    def check_image(self, obj):
        return obj.image.name != ''
    check_image.boolean = True
    check_image.short_description = 'Image'

    def post_on(self, obj):
        return [item.network for item in obj.poston.all()]
    post_on.short_description = 'Post On'

    def admin_categorys(self, obj):
        return [item.name for item in obj.categorys.all()]
    admin_categorys.short_description = 'Categorys'

admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post, PostAdmin)
