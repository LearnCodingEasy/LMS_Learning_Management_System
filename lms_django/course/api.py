# 🃏 استيراد وظيفة اختيار أرقام عشوائية
from random import randint

# 👤 استيراد نموذج "المستخدم" من التطبيق
from account.models import User

# 🖼️ استيراد وظيفة "render" لعرض الصفحات
from django.shortcuts import render

# 🔧 استيراد دالة slugify لتحويل النصوص إلى Slug
from django.utils.text import slugify

# JSON لإرجاع استجابات JsonResponse إستيراد
from django.http import JsonResponse

# 🔗 استيراد أدوات Django Rest Framework
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

# 📦 استيراد النماذج والمسلسلات من التطبيق
from .models import Course, Lesson, Comment, Category
from .serializers import (
    CourseListSerializer,
    CourseDetailSerializer,
    LessonListSerializer,
    CommentsSerializer,
    CategorySerializer,
    QuizSerializer,
    UserSerializer,
)

# 🧐 Django كائن يُستخدم لبناء استعلامات معقدة في
from django.db.models import Q

from uuid import UUID


# 📝 دالة لإنشاء دورة جديدة
@api_view(["POST"])
def create_course(request):
    # 🚦 جلب الحالة من البيانات المدخلة
    status = request.data.get("status")

    # 🖨️ طباعة البيانات للتصحيح أو التحقق
    print(request.data)

    # ⚠️ إذا كانت الحالة 'published'، يتم تحويلها إلى 'draft'
    if status == "published":
        status = "draft"

    # 📚 إنشاء الدورة مع البيانات المدخلة
    course = Course.objects.create(
        title=request.data.get("title"),
        slug="%s-%s"
        % (
            slugify(request.data.get("title")),
            randint(1000, 10000),
        ),  # ✍️ توليد Slug عشوائي
        short_description=request.data.get("short_description"),
        long_description=request.data.get("long_description"),
        status=status,
        created_by=request.user,  # 👤 المستخدم الذي أنشأ الدورة
    )

    # 🏷️ إضافة الفئات للدورة
    for id in request.data.get("categories"):
        course.categories.add(id)

    # 💾 حفظ الدورة
    course.save()

    # 📘 إنشاء الدروس المرتبطة بالدورة
    for lesson in request.data.get("lessons"):
        tmp_lesson = Lesson.objects.create(
            course=course,
            title=lesson.get("title"),
            slug=slugify(lesson.get("title")),  # ✍️ تحويل عنوان الدرس إلى Slug
            short_description=lesson.get("short_description"),
            long_description=lesson.get("long_description"),
            status=Lesson.DRAFT,  # 🚦 الحالة الافتراضية للدرس
        )

    # 🔙 إرجاع استجابة تحتوي على معرف الدورة
    return Response({"course_id": course.id})


# ❓ دالة لجلب الاختبار المرتبط بدورة ودرس معينين
@api_view(["GET"])
def get_quiz(request, course_slug, lesson_slug):
    lesson = Lesson.objects.get(slug=lesson_slug)  # 🔎 جلب الدرس حسب الـ Slug
    quiz = lesson.quizzes.first()  # 🧩 جلب أول اختبار مرتبط بالدرس
    serializer = QuizSerializer(quiz)
    return Response(serializer.data)


@api_view(["GET"])
@authentication_classes([])  # 🔓 عدم استخدام مصادقة
@permission_classes([])  # 🔓 عدم استخدام تصاريح
def categories_list(request):  # 🏷️ دالة لجلب جميع الفئات
    categories = Category.objects.all()  # 📚 جلب كل الفئات
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def courses_list(request):
    courses = Course.objects.all()
    serializer = CourseListSerializer(courses, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def courses_list_by_category(request):
    category_id = request.GET.get("category_id", "")
    courses = Course.objects.filter(status=Course.PUBLISHED)
    if category_id:
        try:
            # ✅ التحقق من صحة الـ UUID
            category_uuid = UUID(category_id)
            # 📝 تصفية الدورات بناءً على الفئة
            courses = courses.filter(categories__id=category_uuid)
        except ValueError:
            # ❌ إرجاع خطأ إذا كان UUID غير صالح
            return JsonResponse({"error": "Invalid category_id format"}, status=400)

    serializer = CourseListSerializer(courses, many=True)
    return JsonResponse(serializer.data, safe=False)


# 📄 دالة لجلب الدورات الأمامية (الواجهة)
@api_view(["GET"])
@authentication_classes([])  # 🔓 عدم استخدام مصادقة
@permission_classes([])  # 🔓 عدم استخدام تصاريح
def courses_list_frontpage(request):
    courses = Course.objects.filter(status=Course.PUBLISHED)[
        0:4
    ]  # 📚 جلب أول 4 دورات منشورة
    serializer = CourseListSerializer(courses, many=True)
    return JsonResponse(serializer.data, safe=False)


# 📚 دالة لجلب بيانات دورة معينة باستخدام المعرف (pk)
@api_view(["GET"])
def course_detail(request, pk):
    user_ids = [request.user.id]

    for user in request.user.friends.all():
        user_ids.append(user.id)

    # 📦 جلب الدورة إذا كان منشؤها موجودًا ضمن معرفات المستخدمين
    # 🔍 البحث عن الدورة المحددة باستخدام شرط أن تكون منشأة بواسطة المستخدم أو أصدقائه.
    course = Course.objects.filter(Q(created_by_id__in=list(user_ids))).get(pk=pk)

    # 🎨 تحويل بيانات الدورة إلى JSON باستخدام الـ Serializer
    course_serializer = CourseDetailSerializer(course)
    course_data = course_serializer.data

    # 🔐 التحقق من إذا كان المستخدم مصرحًا له
    # 🔐 التحقق من إذا كان المستخدم قد سجل الدخول
    if request.user.is_authenticated:
        # ✅ إذا كان مصرحًا له، يتم استخدام بيانات الدورة كما هي
        course_data = course_serializer.data
    else:
        # 🚫 إذا لم يكن مصرحًا له، تكون بيانات الدورة فارغة
        course_data = {}

    # 📚 جلب جميع الدروس المرتبطة بالدورة
    lesson = course.lessons.all()
    # 🎨 تحويل بيانات الدروس إلى JSON باستخدام الـ Serializer
    lesson_serializer = LessonListSerializer(lesson, many=True)
    lesson_data = lesson_serializer.data

    # 📝 إرجاع بيانات الدورة والدروس في صيغة JSON
    return JsonResponse(
        {
            "course": course_data,  # 📝 بيانات الدورة
            "lessons": lesson_data,  # 📚 بيانات الدروس
        }
    )


# 💬 دالة لجلب التعليقات المرتبطة بدورة ودرس معينين
@api_view(["GET"])
def comments_list(request, course_id, lesson_id):
    course = Course.objects.get(id=course_id)  # 🔎 جلب الدورة باستخدام المعرف (id)
    lesson = Lesson.objects.get(id=lesson_id)  # 🔎 جلب الدرس باستخدام المعرف (id)
    # 📝 جلب التعليقات المرتبطة بالدرس
    comments = lesson.comments.all()  # 💬 جميع التعليقات المرتبطة بالدرس
    # 🎨 تحويل التعليقات المرتبطة بالدرس إلى صيغة JSON باستخدام الـ Serializer
    serializer = CommentsSerializer(comments, many=True)
    # 📤 إرجاع البيانات كاستجابة
    return Response(serializer.data)


# ➕ دالة لإضافة تعليق على درس
@api_view(["POST"])
def add_comment(request, course_id, lesson_id):
    # البيانات المرسلة الى قاعدة البيانات
    data = request.data
    course = Course.objects.get(id=course_id)  # 🔎 جلب الدورة باستخدام المعرف (id)
    lesson = Lesson.objects.get(id=lesson_id)  # 🔎 جلب الدرس باستخدام المعرف (id)

    # ✍️ إنشاء تعليق جديد
    comment = Comment.objects.create(
        course=course,
        lesson=lesson,
        name=request.data.get("name"),
        content=request.data.get("content"),
        created_by=request.user,  # 👤 المستخدم الذي أنشأ التعليق
    )
    lesson.comments.add(comment)
    lesson.save()

    serializer = CommentsSerializer(comment)
    # 📤 إرجاع البيانات باستخدام JsonResponse من Django
    return JsonResponse(serializer.data, safe=False)


"""


# 📚 دالة لجلب الدورات التي أنشأها مستخدم معين
@api_view(["GET"])
def get_author_courses(request, user_id):
    user = User.objects.get(pk=user_id)  # 👤 جلب المستخدم بالـ ID
    courses = user.courses.filter(status=Course.PUBLISHED)  # 📚 جلب الدورات المنشورة

    user_serializer = UserSerializer(user, many=False)
    courses_serializer = CourseListSerializer(courses, many=True)

    return Response(
        {
            "courses": courses_serializer.data,  # 📄 بيانات الدورات
            "created_by": user_serializer.data,  # 👤 بيانات المستخدم
        }
    )
"""
