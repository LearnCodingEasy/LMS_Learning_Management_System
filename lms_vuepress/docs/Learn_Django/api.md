# تعلم Django

## Api => إنشاء العناصر المراية و طريقة العرض و الفلاتر

###

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
