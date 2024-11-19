# Django Page Api

<div dir="rtl" style="font-size:1.2vw; padding: 1rem 0; font-weight: 900;">
  إنشاء العناصر المراية و طريقة العرض و الفلاتر
</div>

## All

<div style="font-size:1.2vw; padding: 2rem 0 0 0; font-weight: 900;">
</div>

<div dir="rtl" style="font-size:1.2vw; padding: 1rem 0; font-weight: 900;">
  
  
</div>

```python
@api_view(["GET"])
@authentication_classes([])  # 🔓 عدم استخدام مصادقة
@permission_classes([])  # 🔓 عدم استخدام تصاريح
def categories_list(request):  # 🏷️ دالة لجلب جميع الفئات
    categories = Category.objects.all() # 📚 جلب كل الفئات
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
```

```python
@api_view(["GET"])
@authentication_classes([])  # 🔓 عدم استخدام مصادقة
@permission_classes([])  # 🔓 عدم استخدام تصاريح
def courses_list(request): # 🏷️ دالة لجلب جميع الكرسات
    courses = Course.objects.all() # 📚 جلب كل الكرسات
    serializer = CourseListSerializer(courses, many=True)
    return JsonResponse(serializer.data, safe=False)
```

## Single

```python
# 🧐 Django كائن يُستخدم لبناء استعلامات معقدة في
from django.db.models import Q

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

```
