"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from personal.views import (
    home_view,
    about_view,
    aims_and_obj_view,
    our_constitution_view,
    form_test_view,
    subscribe_view,
    subscribe_warning_view,
    contact_view,
    membership_view,
    governing_board_view,
    founding_trustees_view,
    appointed_trustees_view,
    ambassadors_view,
    associate_membership_view,
    project_facilitators_view,
    volunteers_view,
    donate_view,
    pay_view,
    process_pay_view,
    testpage_view,
    finaltest_view,
)

from account.views import (
    login_view,
    signup_view,
    forgot_password_view,
    dashboard_view,
    logout_view,
    account_view,
    must_authenticate_view,
    all_post_screen_view,
    all_project_screen_view,
    all_outreach_screen_view,
    all_slider_screen_view,
    all_testimonials_screen_view,
    all_contacts_screen_view,
    detail_contact_view,
    contact_delete_view,
    all_subscribe_screen_view,
    detail_subscribe_view,
    subscribe_delete_view,
    account_update_success_view,
    all_users_screen_view,
    users_delete_view,
    detail_users_view,
    all_trustee_screen_view,
    my_trustee_screen_view
)

from blog.views import (
    blog_screen_view,
    blog_comment_view,
    blog_comment_reply_view,
)

from project.views import (
    projects_view,
    projects_category_view,
)

from outreach.views import (
    outreach_view,
)

from slider.views import (
    slider_view,
)

from testimonials.views import (
    testimonials_screen_view,
)

urlpatterns = [
    path('admin/clearcache/', include('clearcache.urls')),
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('form_test', form_test_view, name="form_test"),
    path('contact', contact_view, name="contact"),
    path('subscribe', subscribe_view, name="subscribe"),
    path('already_subscribed', subscribe_warning_view, name="already_subscribed"),
    path('blog/', include('blog.urls', 'blog')),
    path('project/', include('project.urls', 'project')),
    path('outreach/', include('outreach.urls', 'outreach')),
    path('slider/', include('slider.urls', 'slider')),
    path('testimonials/', include('testimonials.urls', 'testimonials')),
    path('trustees/', include('trustees.urls', 'trustees')),
    path('about', about_view, name="about"),
    path('aims_and_obj', aims_and_obj_view, name="aims_and_obj"),
    path('our_constitution', our_constitution_view, name="our_constitution"),
    path('membership', membership_view, name="membership"),
    path('governing_board', governing_board_view, name="governing_board"),
    path('founding_trustees', founding_trustees_view, name="founding_trustees"),
    path('appointed_trustees', appointed_trustees_view, name="appointed_trustees"),
    path('ambassadors', ambassadors_view, name="ambassadors"),
    path('associate_membership', associate_membership_view, name="associate_membership"),
    path('project_facilitators', project_facilitators_view, name="project_facilitators"),
    path('volunteers', volunteers_view, name="volunteers"),
    path('donate', donate_view, name="donate"),
    path('make_payment', pay_view, name="make_payment"),
    path('process_pay', process_pay_view, name="process_pay"),
    path('blog', blog_screen_view, name="blog"),
    path('blog_comment', blog_comment_view, name="blog_comment"),
    path('blog_comment_reply', blog_comment_reply_view, name="blog_comment_reply"),
    path('login', login_view, name="login"),
    path('signup', signup_view, name="signup"),
    path('forgot-password', forgot_password_view, name="forgot-password"),
    path('dashboard', dashboard_view, name="dashboard"),
    path('account', account_view, name="account"),
    path('account_update_success', account_update_success_view, name="account_update_success"),
    path('must_authenticate', must_authenticate_view, name="must_authenticate"),
    path('logout/', logout_view, name="logout"),
    path('all_post', all_post_screen_view, name="all_post"),
    path('all_project', all_project_screen_view, name="all_project"),
    path('all_outreach', all_outreach_screen_view, name="all_outreach"),
    path('all_slider', all_slider_screen_view, name="all_slider"),
    path('all_testimony', all_testimonials_screen_view, name="all_testimony"),
    path('all_contact', all_contacts_screen_view, name="all_contact"),
    path('all_users', all_users_screen_view, name="all_users"),
    path('all_trustee', all_trustee_screen_view, name="all_trustee"),
    path('my_trustee', my_trustee_screen_view, name="my_trustee"),
    path('<id>/delete_users', users_delete_view, name="delete_users"),
    path('<id>/detail_user', detail_users_view, name="detail_user"),
    path('<id>/detail_contact', detail_contact_view, name="detail_contact"),
    path('<id>/delete_contact', contact_delete_view, name="delete_contact"),
    path('all_subscribers', all_subscribe_screen_view, name="all_subscribers"),
    path('<id>/detail_subscribe', detail_subscribe_view, name="detail_subscribe"),
    path('<id>/delete_subscribe', subscribe_delete_view, name="delete_subscribe"),
    path('projects', projects_view, name="projects"),
    path('projects_category', projects_category_view, name="projects_category"),
    path('outreach', outreach_view, name="outreach"),
    path('slider', slider_view, name="slider"),
    path('testimonials', testimonials_screen_view, name="testimonials"),
    path('testpage', testpage_view, name="testpage"),
    path('finaltest', finaltest_view, name="finaltest"),





    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)