
from django.urls import path
from frontend import views
from django.contrib.auth import views as auth_views



app_name = 'frontend'


urlpatterns = [
    path('one/<int:pst>/', views.one, name='one'),
    path('two/<int:pst>/', views.two, name='two'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('activateEmail', views.activateEmail, name='activateEmail'),
    path('register', views.register, name='register'),
    path('login', views.custom_login, name='custom_login'),
    path('logout', views.custom_logout, name='logout'),
    path('confirm_logout', views.confirm_logout, name='confirm_logout'),
    path('edit-profile', views.edit_profile, name='edit_profile'),
    path("password_change", views.password_change, name="password_change"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),
    path('news', views.news, name='news'),
    path('info', views.info, name='info'),
    path('like_post/<int:pk>/', views.like_post, name='like_post'),
    path('base', views.base, name='base'),
    path('profile', views.profile, name='profile'),
    #     PRODUCT CODE ENDS HERE
    path('add-post', views.add_post, name='add_post'),
    path('view-post', views.view_post, name='view_post'),
    path('delete_post/<int:pst_id>', views.delete_post, name='delete_post'),
    path('edit_post/<int:pst_id>', views.edit_post, name='edit_post'),
    path('favourite_post/<int:id>/', views.favourite_post, name='favourite_post'),
     path('post-list', views.post_list, name='post_list'),
     #path('error_404_view', views.error_404_view, name='error_404_view'),
     path('about', views.about, name='about'),
     path('privacy_policy', views.privacy_policy, name='privacy_policy'),
     path('contact-us', views.contact_us, name='contact_us'),
     path('newsletter', views.newsletter, name='newsletter'),
     path('checkout', views.checkout, name='checkout'),
     path('shop', views.shop, name='shop'),
     path('about-us', views.about_us, name='about_us'),
     path('error_404_view', views.error_404_view, name='error_404_view'),
     path('buy_now/<int:pst>/', views.buy_now, name='buy_now'),
     
#     PRODUCT CODE ENDS HERE
    # CART STATRT HERE    
     path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail, name='cart_detail'),
    
    # CART END HERE

    #SEARCH BAR CODE
    path('search', views.search, name='search'),
          # BLOG PAGE STARTS HERE
     path('blog', views.blog, name='blog'),
     path('blog-two/<int:pst>/', views.blog_two, name='blog_two'),
     path('like-blog/<int:pk>/', views.like_blog, name='like_blog'),
     path('add-blog', views.add_blog, name='add_blog'),
     path('view-blog', views.view_blog, name='view_blog'),
     path('delete-blog/<str:pst_id>/', views.delete_blog, name='delete_blog'),
     path('edit-blog/<int:pst_id>/', views.edit_blog, name='edit_blog'),
     path('blog-post/<int:id>/', views.blog_post, name='blog_post'),
     path('blog-list', views.blog_list, name='blog_list'),
     path('result', views.result, name='result'),
     path('faqs', views.faqs, name='faqs'),
     
     
     
          # BLOG PAGE ENDS HERE

          # ORDER CODE START HERE

     path('order', views.order, name='order'),
     path('orderby', views.orderby, name='orderby'),
     path('delete-order/<int:id>/', views.delete_order, name='delete_order'),
     path('single-order/<int:id>/', views.single_order, name='single_order'),
     
     

          # ORDER CODE END HERE
          
          

    ]
    
