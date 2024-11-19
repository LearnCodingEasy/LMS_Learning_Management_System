# 📂 استيراد وظيفة path من Django لإنشاء مسارات URL
from django.urls import path

# 📦 استيراد ملف api الذي يحتوي على الدوال المطلوبة
from . import api

# 🛣️ تعريف مسارات التطبيق
urlpatterns = [
    # 📝 مسار لجلب جميع الدورات
    # 🏁 المسار الأساسي يوجه إلى دالة courses_list
    path("courses_list/", api.courses_list, name="courses_list"),
    # 📝 مسار لجلب الدورات المعروضة في الواجهة الأمامية
    # 🏠 مسار جلب الدورات الأمامية
    # path("get_frontpage_courses/", api.get_frontpage_courses),
    # 🏷️ مسار لجلب جميع الفئات
    # 🏷️ مسار جلب الفئات
    path("categories_list/", api.categories_list, name="categories_list"),
    # 👤 مسار لجلب الدورات التي أنشأها مستخدم معين باستخدام معرف المستخدم
    # 🧑‍🏫 مسار جلب الدورات الخاصة بمؤلف
    # path("get_author_courses/<int:user_id>/", api.get_author_courses),
    # 🆕 مسار لإنشاء دورة جديدة
    # ➕ مسار إنشاء دورة
    # path("create/", api.create_course),
    # 🔍 مسار لجلب تفاصيل دورة معينة باستخدام الـ Slug
    # 🔍 مسار جلب تفاصيل الدورة
    path("<slug:slug>/", api.get_course, name="get_course"),
    path("course_detail/<uuid:pk>/", api.course_detail, name="course_detail"),
    # 💬 مسار لإضافة تعليق على درس معين باستخدام Slug الدورة و Slug الدرس
    # 💬 مسار إضافة تعليق
    # path("<slug:course_slug>/<slug:lesson_slug>/", api.add_comment),
    # 🗨️ مسار لجلب التعليقات المرتبطة بدورة ودرس معينين
    # 📝 مسار جلب التعليقات
    # path("<slug:course_slug>/<slug:lesson_slug>/get-comments/", api.get_comments),
    # ❓ مسار لجلب الاختبار المرتبط بدرس معين
    # 🧩 مسار جلب الاختبار
    # path("<slug:course_slug>/<slug:lesson_slug>/get-quiz/", api.get_quiz),
]
