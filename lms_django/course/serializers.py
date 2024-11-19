# 🧑‍💻 استيراد نموذج المستخدمين الافتراضي من Django
# from django.contrib.auth.models import User
from account.serializers import UserSerializer

# 🛠️ استيراد الأدوات المساعدة من مكتبة Django Rest Framework
from rest_framework import serializers

# 📦 استيراد النماذج المخصصة من التطبيق الحالي
from .models import Course, Lesson, Comment, Category, Quiz


# 🏷️ مُسلسل لعرض معلومات الفئات
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        # 🔗 ربط النموذج بموديل الفئة
        model = Category
        # 📄 الحقول التي سيتم تضمينها في السيريالايزر
        fields = ("id", "title", "slug")


# 📚 مُسلسل لعرض قائمة الدورات
class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        # 🔗 ربط النموذج بموديل الدورة
        model = Course
        # 📄 الحقول التي سيتم تضمينها في السيريالايزر لعرض ملخص الدورة
        fields = ("id", "title", "slug", "short_description", "get_image")


# 📖 مُسلسل لعرض تفاصيل الدورة
class CourseDetailSerializer(serializers.ModelSerializer):
    # 👤 تضمين معلومات المستخدم الذي أنشأ الدورة
    # created_by = UserSerializer(many=False)
    created_by = UserSerializer(read_only=True)

    class Meta:
        # 🔗 ربط النموذج بموديل الدورة
        model = Course
        # 📄 الحقول التي سيتم تضمينها في السيريالايزر لعرض تفاصيل الدورة
        fields = (
            "id",
            "title",
            "slug",
            "short_description",
            "long_description",
            "created_by",
        )


# 🎓 مُسلسل لعرض قائمة الدروس
class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        # 🔗 ربط النموذج بموديل الدرس
        model = Lesson
        # 📄 الحقول التي سيتم تضمينها في السيريالايزر لعرض ملخص الدرس
        fields = (
            "id",
            "title",
            "slug",
            "lesson_type",
            "short_description",
            "long_description",
            "youtube_id",
        )


# 💬 مُسلسل لعرض التعليقات
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        # 🔗 ربط النموذج بموديل التعليق
        model = Comment
        # 📄 الحقول التي سيتم تضمينها في السيريالايزر لعرض معلومات التعليق
        fields = ("id", "name", "content", "created_at")


# ❓ مُسلسل لعرض معلومات الاختبارات
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        # 🔗 ربط النموذج بموديل الاختبار
        model = Quiz
        # 📄 الحقول التي سيتم تضمينها في السيريالايزر لعرض تفاصيل الاختبار
        fields = ("id", "lesson_id", "question", "answer", "op1", "op2", "op3")
