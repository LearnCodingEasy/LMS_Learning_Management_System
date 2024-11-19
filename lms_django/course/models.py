# uuid: يُستخدم لإنشاء معرّفات فريدة عالمياً
# (UUID) التي يمكن استخدامها لتعريف المستخدمين.
import uuid

# 📦 Import إعدادات المشروع الأساسية ونماذج المستخدمين من Django
from django.conf import settings

# ���️ تعريف نموذج "المستخدم"
from account.models import User


from django.db import models


# 🏷️ تعريف نموذج "الفئة" لتصنيف الدورات
class Category(models.Model):
    # 🔑 Define the primary field to be UUID  تعريف الحقل الأساسي ليكون
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # عنوان الفئة بحد أقصى 255 حرفًا
    title = models.CharField(max_length=255)
    # حقل الـ slug لعنوان URL قابل للقراءة
    slug = models.SlugField()
    # وصف قصير للفئة يمكن أن يكون فارغًا
    short_description = models.TextField(blank=True, null=True)
    # تاريخ إنشاء الفئة (يُضاف تلقائيًا عند الإنشاء)
    created_at = models.DateField(auto_now_add=True)

    # لضبط الاسم الجمعي للنموذج عند العرض في لوحة الإدارة
    class Meta:
        verbose_name_plural = "Categories"

    # 📝 لعرض عنوان الفئة عند استدعاء النموذج كمُعرِّف نصي
    def __str__(self):
        return self.title


# 📚 تعريف نموذج "الدورة"
class Course(models.Model):
    # ___________________
    # حقل يتم تعبئة تلقائي
    # ___________________
    # 🔑 Define the primary field to be UUID  تعريف الحقل الأساسي ليكون
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # تاريخ الإنشاء (يُضاف تلقائيًا عند الإنشاء)
    created_at = models.DateField(auto_now_add=True)
    # 🔒 علاقة بين الدورة والمستخدم الذي أنشأها
    created_by = models.ForeignKey(
        User, related_name="courses", on_delete=models.CASCADE
    )

    # ___________________
    # حقل يتم تعبئة من المستخدام
    # ___________________
    # حالات مختلفة لحالة الدورة
    DRAFT = "draft"
    IN_REVIEW = "in_review"
    PUBLISHED = "published"
    # مسودة
    # قيد المراجعة
    # منشورة
    STATUS_CHOICES = (
        (DRAFT, "Draft"),
        (IN_REVIEW, "In review"),
        (PUBLISHED, "Published"),
    )
    # 🔗 ارتباطات بين الدورات والفئات (علاقة متعدد لمتعدد)
    categories = models.ManyToManyField(Category)
    # عنوان الدورة بحد أقصى 255 حرفًا
    title = models.CharField(max_length=255)
    # حقل الـ slug لعنوان URL الخاص بالدورة
    slug = models.SlugField()
    # وصف قصير يمكن أن يكون فارغًا
    short_description = models.TextField(blank=True, null=True)
    # وصف طويل يمكن أن يكون فارغًا
    long_description = models.TextField(blank=True, null=True)
    # صورة مصغرة للدورة
    image = models.ImageField(upload_to="courses", blank=True, null=True)
    # الحالة الحالية للدورة
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=DRAFT)

    # ترتيب الدورات الأحدث أولًا
    class Meta:
        ordering = ("-created_at",)

    # 📝 لعرض عنوان الدورة عند استدعاء النموذج كمُعرِّف نصي
    def __str__(self):
        return self.title

    # 🖼️ إرجاع رابط الصورة أو صورة افتراضية
    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return "http://bulma.io/images/placeholders/1280x960.png"


# 📝 تعريف نموذج "الدرس
class Lesson(models.Model):
    # 🔑 Define the primary field to be UUID  تعريف الحقل الأساسي ليكون
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # حالات مختلفة لحالة الدرس
    DRAFT = "draft"
    PUBLISHED = "published"
    # مسودة
    # منشورة
    CHOICES_STATUS = ((DRAFT, "Draft"), (PUBLISHED, "Published"))

    # أنواع الدروس المختلفة
    ARTICLE = "article"
    QUIZ = "quiz"
    VIDEO = "video"
    # مقالة
    # اختبار
    # فيديو
    CHOICES_LESSON_TYPE = (
        (ARTICLE, "Article"),
        (QUIZ, "Quiz"),
        (VIDEO, "Video"),
    )
    # 🔗 ارتباط الدرس بالدورة (علاقة واحد لمتعدد)
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)
    # عنوان الدرس
    title = models.CharField(max_length=255)
    # حقل الـ slug لعنوان URL الخاص بالدرس
    slug = models.SlugField()
    # وصف قصير
    short_description = models.TextField(blank=True, null=True)
    # وصف طويل
    long_description = models.TextField(blank=True, null=True)
    # الحالة الحالية للدرس
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=PUBLISHED)
    # نوع الدرس
    lesson_type = models.CharField(
        max_length=20, choices=CHOICES_LESSON_TYPE, default=ARTICLE
    )
    # معرف فيديو على YouTube إذا كان الدرس عبارة عن فيديو
    youtube_id = models.CharField(max_length=20, blank=True, null=True)

    # 📝 لعرض عنوان الدورة عند استدعاء النموذج كمُعرِّف نصي
    def __str__(self):
        return self.title


# 💬 تعريف نموذج "التعليقات"
class Comment(models.Model):
    # 🔑 Define the primary field to be UUID  تعريف الحقل الأساسي ليكون
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # 🔗 ارتباط التعليق بالدورة والدرس
    course = models.ForeignKey(
        Course, related_name="comments", on_delete=models.CASCADE
    )
    lesson = models.ForeignKey(
        Lesson, related_name="comments", on_delete=models.CASCADE
    )
    # اسم الشخص الذي قام بكتابة التعليق
    name = models.CharField(max_length=100)
    # محتوى التعليق
    content = models.TextField()
    # تاريخ ووقت إنشاء التعليق (يُضاف تلقائيًا عند الإنشاء)
    created_at = models.DateTimeField(auto_now_add=True)
    # 🔒 المستخدم الذي أنشأ التعليق
    created_by = models.ForeignKey(
        User, related_name="comments", on_delete=models.CASCADE
    )


# ❓ تعريف نموذج "الاختبارات"
class Quiz(models.Model):
    # 🔑 Define the primary field to be UUID  تعريف الحقل الأساسي ليكون
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # 🔗 ارتباط الاختبار بالدرس
    lesson = models.ForeignKey(Lesson, related_name="quizzes", on_delete=models.CASCADE)
    # سؤال الاختبار
    question = models.CharField(max_length=200, null=True)
    # الإجابة الصحيحة
    answer = models.CharField(max_length=200, null=True)
    # الخيارات الثلاثة الإضافية
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    op3 = models.CharField(max_length=200, null=True)

    # لضبط الاسم الجمعي للنموذج عند العرض في لوحة الإدارة
    class Meta:
        verbose_name_plural = "Quizzes"
