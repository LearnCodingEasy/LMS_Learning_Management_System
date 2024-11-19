# LMS Learning Management System

## Github

###### 📁 Git Clone Project

```cmd
git clone https://github.com/LearnCodingEasy/LMS_Learning_Management_System.git
```

###### 📝 Create File Gitignore

```
.gitignore
```

###### 🖊️ Write Inside File

```
node_modules/
```

###### 📋 Review changes and formulate change action

###### 📋 مراجعة التغييرات وصياغة إجراء التغيير

```cmd
git status
```

###### 📂 Add all new and changed files to the Staging Area.

###### 📂 أضف كل الملفات الجديدة والمغير إلى منطقة التدريج.

```
git add *
```

###### 💾 This command sends the file from the Staging Area to the Local Repo.

###### 💾 يرسل هذا الأمر الملف من منطقة التدريج إلى الريبو المحلي.

```cmd
git commit -m "Commit Explain Code"
```

###### 🌐 This command sends files from (Local Repo) to (Remote Repo).

###### 🌐 يرسل هذا الأمر ملفات من (repo المحلي) إلى (ريبو عن بعد).

```cmd
git push origin main
```

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

## LICENSE

Create File 📝 [ LICENSE ]

```text
LICENSE
```

```text
MIT License
Copyright (c) 2024 Hossam Rashad
📍 +0201091642528
📍 +0201101853042
```

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

## Vite Press

###### 🖥️ Create Vuepress

```cmd
npm init vuepress lms_vuepress
```

###### 🖥️ Command Path

```cmd
cd lms_vuepress
```

###### 🖥️ Install Sass

```cmd
npm install -D sass-embedded
```

###### 📝 Create File [ index.md ] Inside Docs

```
index.md
```

###### 🖥️ Run Vue Press

```cmd
npm run docs:dev
```

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

## Django

### 🖥️ Virtual Environment

###### 🖥️ Create Virtual Environment 🐍

```cmd
python -m venv lms_virtual_environment
```

###### 🚀 Activate Virtual Environment 🔋

```cmd
lms_virtual_environment\Scripts\activate
```

### 🔧 Install Django

###### 🔧 Install Django 🦄

```cmd
pip install django
```

###### 🔧 Django Version 🦄

```cmd
python -m django --version
```

### 🛠️ Django Libraries

###### 🛠️ Install Django Libraries 📚

1 - 🌐 Django Rest Framework

```cmd
pip install djangorestframework
```

2 - 🔒 Django Rest Framework Simplejwt 🛡️

```cmd
pip install djangorestframework-simplejwt
```

3 - 🌍 Django Cors Headers 🔗

```cmd
pip install django-cors-headers
```

4 - 🖼️ pillow 📷

```
pip install pillow
```

### 📂 Create Django Project

```cmd
django-admin startproject lms_django
```

### 👤 Create Django App Account

```cmd
cd lms_django
```

```cmd
python manage.py startapp account
```

### ⚙️ Settings

#### ⚙️ Page Settings [ settings.py ] 📝

```python
# Page [lms/lms_django/lms_django/settings.py]

from datetime import timedelta

# The address of the site that points to the local server.
WEBSITE_URL = "http://127.0.0.1:8000"

# Define the default user model used in the application.
AUTH_USER_MODEL = "account.User"

# SIMPLE_JWT library settings to specify the validity period of tokens
# Access Token Validity (30 days)
# Refresh Token Validity (180 days)
# Disable Auto Refresh Tokens
SIMPLE_JWT = {
  "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
  "REFRESH_TOKEN_LIFETIME": timedelta(days=180),
  "ROTATE_REFRESH_TOKENS": False,
}

# Django REST Framework settings for identity and permissions verification
# Use JWT for identity verification
# Allow only authenticated users
REST_FRAMEWORK = {
  "DEFAULT_AUTHENTICATION_CLASSES": (
      "rest_framework_simplejwt.authentication.JWTAuthentication",
  ),
  "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

# Allow CORS requests from specific addresses
# Allow requests from this origin
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:5174",
]

# Allow CSRF requests from specific addresses
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:5174",
]

INSTALLED_APPS = [
    # ...
    # Apps
    "account",
    # Libraries
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
]

MIDDLEWARE = [
    # Libraries [ Django Cors Headers ]
    "corsheaders.middleware.CorsMiddleware",
    # ...
]
# Access path for static files (such as CSS and JavaScript files)
STATIC_URL = "static/"
# Access path for media files (such as images and files uploaded by users)
MEDIA_URL = "media/"
# Specify a "media" folder in the project to store uploaded media files
MEDIA_ROOT = BASE_DIR / "media"
```

### 🧑 Account Page [ models.py ]

#### 🧑 App [ Account ] Page [ models.py ] 📝

```python
# 📄 صفحة [lms/lms_django/account/models.py]
# uuid: يُستخدم لإنشاء معرّفات فريدة عالمياً
# (UUID) التي يمكن استخدامها لتعريف المستخدمين.
import uuid

# settings: لاستيراد إعدادات
# Django الخاصة بالمشروع.
from django.conf import settings

# AbstractBaseUser, PermissionsMixin: لإنشاء نموذج مستخدم مخصص.
# UserManager: لإدارة إنشاء المستخدمين.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

# models: لإنشاء نماذج Django.
from django.db import models

# Time
# timezone: للتعامل مع التوقيتات.
from django.utils import timezone
from django.utils.timesince import timesince


# 👥 Dedicated manager to create and manage users
# 👥 مدير مخصص لإنشاء وإدارة المستخدمين
class CustomUserManager(UserManager):
    def _create_user(self, name, email, password, **extra_fields):
        # ✉️ Verify email entry
        # ✉️ تحقق من إدخال البريد الإلكتروني
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 👤 Create a regular user
    # 👤 إنشاء مستخدم عادي
    def create_user(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(name, email, password, **extra_fields)

    # 🛡️ Create an administrative user (super user)
    # 🛡️ إنشاء مستخدم إداري (سوبر يوزر)
    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(name, email, password, **extra_fields)


# 🧑 Custom User Form
# 🧑 نموذج المستخدم المخصص
class User(AbstractBaseUser, PermissionsMixin):
    # 🔑 Define the primary field to be UUID  تعريف الحقل الأساسي ليكون
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 📛 User Data Properties خصائص بيانات المستخدم
    name = models.CharField(max_length=255, blank=True, null=True, default="")
    surname = models.CharField(max_length=255, blank=True, default="")
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=15, blank=True, null=True)
    # 🖼️ Profile Picture صورة شخصية
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)
    # 🖼️ Cover Photo صورة الغلاف
    cover = models.ImageField(upload_to="covers", blank=True, null=True)

    # ⚙️ User Status  حالة المستخدم
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # 📋 Custom Admin Link ربط المدير المخصص
    objects = CustomUserManager()

    # 👥 Friends and Characteristics of Friendships الأصدقاء وخصائص الصداقات
    friends = models.ManyToManyField("self")
    friends_count = models.IntegerField(default=0)
    people_you_may_know = models.ManyToManyField("self")

    # 📋 Tasks and Their Number المهام وعددها
    task_count = models.IntegerField(default=0)

    # 📅 Join Date & Last Login تاريخ الانضمام وآخر تسجيل دخول و حالة الاتصال
    # Automatic
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_online = models.BooleanField(default=False)

    # 🔒 إعدادات تسجيل الدخول: البريد الإلكتروني كمحدد رئيسي لتسجيل الدخول
    # يحدد الحقل الذي سيتم استخدامه لتسجيل الدخول. في هذه الحالة، هو email.
    USERNAME_FIELD = "email"
    # يحدد الحقل الذي يتم استخدامه كالبريد الإلكتروني الرئيسي للمستخدم. في هذه الحالة، هو email.
    EMAIL_FIELD = "email"
    # 📝 لا توجد حقول إضافية مطلوبة بجانب البريد الإلكتروني وكلمة المرور عند إنشاء مستخدم جديد عبر الأوامر الإدارية.
    REQUIRED_FIELDS = []

    # 🖼️ Function to get cover image link With default link if none exists
    # 🖼️ دالة للحصول على رابط صورة الغلاف مع رابط افتراضي إذا لم تكن موجودة
    def get_avatar(self):
        if self.avatar:
            return settings.WEBSITE_URL + self.avatar.url
        else:
            return "https://picsum.photos/200/200"

    def get_cover(self):
        if self.cover:
            return settings.WEBSITE_URL + self.cover.url
        else:
            return "https://picsum.photos/200/200"

    def date_joined_formatted(self):
        return timesince(self.date_joined)


# 📬 Friend Request Form نموذج طلب الصداقة
class FriendshipRequest(models.Model):
    # 📝 Friend request cases  حالات طلب الصداقة
    SENT = "sent"
    NOT_SENT = "not sent"
    ACCEPTED = "accepted"
    WAITING = "waiting"
    REJECTED = "rejected"
    CANCEL = "cancel"

    STATUS_CHOICES = (
        (SENT, "Sent"),
        (NOT_SENT, "Not Sent"),
        (ACCEPTED, "Accepted"),
        (WAITING, "Waiting"),
        (REJECTED, "Rejected"),
        (CANCEL, "Cancel"),
    )
    # 🔑 Friend Request UUID Essential Field حقل أساسي UUID لطلب الصداقة
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 🧑 User receiving the request  المستخدم المستلم للطلب
    created_for = models.ForeignKey(
        User, related_name="received_friendshiprequests", on_delete=models.CASCADE
    )
    # 📅 Creation date تاريخ الإنشاء
    created_at = models.DateTimeField(auto_now_add=True)
    # 🧑 The user who sent the request  المستخدم المرسل للطلب
    created_by = models.ForeignKey(
        User, related_name="created_friendshiprequests", on_delete=models.CASCADE
    )
    # 📝 Order Status  حالة الطلب
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=NOT_SENT)
```

### 🆕 Makemigrations

###### 🛠️ Modifications To Models File | تعديلات على ملف النماذج

```cmd
python manage.py makemigrations
```

### 🛠️ Makemigrations

###### 🛠️ Migrate To The Database |الانتقال إلى قاعدة البيانات

```cmd
python manage.py migrate
```

### 🧑 Account Page [ admin.py ]

#### 🧑 App [ Account ] Page [ admin.py ] 📝

```python
from django.contrib import admin
from .models import User
admin.site.register(User)
```

### 🧑 Account Page [ serializers.py ]

#### 🧑 App [ Account ] Page [ serializers.py ] 📝

```
serializers.py
```

```python
#  📝 Page [ lms/lms_django/account/serializers.py ]

# استيراد الاطار لتحويل البيانات
from rest_framework import serializers

# استيراد نموذج البيانات المراد تحويلة
from .models import User, FriendshipRequest

# from django.utils import timezone


# 🧑 سيريلايزر لمستخدم
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        # النموذج المرتبط بالسيريلايزر
        # النموذج المراد استخدامه
        model = User
        # الحقول المطلوبة
        # 🔍 تستخدم لتحديد الحقول المضمنة في البيانات المُسترجعة أو المرسلة عبر المسلسل.
        fields = (
            "id",
            "name",
            "surname",
            "email",
            "date_of_birth",
            "gender",
            "get_avatar",
            "get_cover",
            # Friends
            "friends_count",
            # Tasks
            "task_count",
            # Data & Time
            "date_joined",
            "date_joined_formatted",
            "last_login",
            "is_online",
        )


class FriendshipRequestSerializer(serializers.ModelSerializer):
    # 👤 Sender information using UserSerializer (read-only)
    # 👤 معلومات المرسل باستخدام المستخدمين (القراءة فقط)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = FriendshipRequest
        # 🆔 Request ID and sender data
        # 🆔 طلب معرف وبيانات المرسل
        fields = (
            "id",
            "created_by",
            "status"
        )
```

### 🧑 Account Page [ forms.py ]

#### 🧑 App [ Account ] Page [ forms.py ] 📝

```
forms.py
```

```python
# 📄 ملف [ lms/lms_django/account/forms.py ]

from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


# 📝 نموذج التسجيل
class SignupForm(UserCreationForm):
    # 🔧 إعدادات النموذج: تحديد الحقول المطلوبة
    class Meta:
        model = User
        fields = (
            # 🧑 الاسم الأول
            "name",
            # 🧑 اللقب
            "surname",
            # 📧 البريد الإلكتروني
            "email",
            # 📅 تاريخ الميلاد
            "date_of_birth",
            # ⚧ الجنس
            "gender",
            # 🔑 كلمة المرور
            "password1",
            # 🔑 تأكيد كلمة المرور
            "password2",
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            # 🧑 User's name الاسم الأول
            "name",
            # 🧑 اللقب
            "surname",
            # 📧 User's email البريد الإلكتروني
            "email",
            # 📅 تاريخ الميلاد
            "date_of_birth",
            # ⚧ الجنس
            "gender",
            # 🖼️ User's profile picture صورة ملف تعريف المستخدم
            "avatar",
            # 🖼️ User's Cover picture صورة ملف غلااف المستخدم
            "cover",
        )

```

### 🧑 Account Page [ api.py ]

#### 🧑 App [ Account ] Page [ api.py ] 📝

```python
api.py
```

```python
# 📄 ملف [ lms/lms_django/account/api.py ]

# 🌐 API for User Signup and Profile Info Retrieval
# 🌐 API لتسجيل المستخدم واسترجاع معلومات الحساب

# Django إستيراد إعدادات المشروع في
from django.conf import settings

# إستيراد نموذج تغيير كلمة المرور
from django.contrib.auth.forms import PasswordChangeForm

# إستيراد دالة إرسال البريد الإلكتروني
from django.core.mail import send_mail

# JSON لإرجاع استجابات JsonResponse إستيراد
from django.http import JsonResponse

# إستيراد الديكورات لتعريف وحدات الواجهة البرمجية
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

# إستيراد النماذج المخصصة لتسجيل المستخدم وتعديل الملف الشخصي
from .forms import SignupForm, ProfileForm

# إستيراد النماذج المخصصة للمستخدم وطلبات الصداقة
from .models import User, FriendshipRequest

# إستيراد المسلسلات للمستخدم وطلبات الصداقة
from .serializers import UserSerializer, FriendshipRequestSerializer


# 📝 Signup API Endpoint
# 📝 واجهة برمجية للتسجيل
@api_view(["POST"])
@authentication_classes([])  # 🚫 لا تتطلب مصادقة
@permission_classes([])  # 🚫 لا تتطلب أذونات
def signup(request):
    data = request.data
    message = "success"

    # 🧾 Initialize signup form with request data
    # 🧾 تهيئة نموذج التسجيل باستخدام بيانات الطلب
    form = SignupForm(
        {
            "name": data.get("name"),
            "surname": data.get("surname"),
            "email": data.get("email"),
            "date_of_birth": data.get("date_of_birth"),
            "gender": data.get("gender"),
            "password1": data.get("password1"),
            "password2": data.get("password2"),
        }
    )

    # ✅ Check if form is valid
    # ✅ التحقق من صحة النموذج
    if form.is_valid():
        # 🛠️ Save the new user
        # 🛠️ حفظ المستخدم الجديد
        user = form.save()
        # 🔓 Activate the account
        # 🔓 تأكيد الحساب مباشرة
        user.is_active = True
        user.save()

        return JsonResponse({"message": message, "email_sent": True}, safe=False)
    else:
        # ❌ If errors exist, return them
        # ❌ إذا كان هناك أخطاء
        message = form.errors.as_json()
    # 🔍 Print errors for debugging
    # 🔍 طباعة الأخطاء لأغراض التصحيح
    print(message)
    return JsonResponse({"message": message}, safe=False)


# 👤 User Info API Endpoint
# JSON إرجاع بيانات المستخدم الحالي كاستجابة
# 👤 واجهة برمجية لاسترجاع معلومات المستخدم
@api_view(["GET"])
def me(request):
    if request.user.is_authenticated:
        user_serializer = UserSerializer(request.user)
        return JsonResponse(user_serializer.data, safe=False)
    return JsonResponse({"error": "User not authenticated"}, status=401)


# Profile
@api_view(["GET"])
def profile(request, id):
    # (primary key) استرجاع معلومات المستخدم بناءً على معرفه الفريد
    user = User.objects.get(pk=id)
    # print("Profile User By Id 👉️", user)
    # (primary key)
    # تسلسل بيانات المستخدم باستخدام السيريالايزر المخصص
    user_serializer = UserSerializer(user)
    # print("Profile User By Id 👍", user_serializer)

    #
    can_send_friendship_request = True

    if request.user in user.friends.all():
        can_send_friendship_request = False

    # 🔍 Check if a request already exists between the users
    # 🔍 التحقق مما إذا كان هناك طلب صداقة موجود بالفعل بين المستخدمين
    check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(
        created_by=user
    )
    check2 = FriendshipRequest.objects.filter(created_for=user).filter(
        created_by=request.user
    )
    # For Test
    # print("How Is User check1", check1)
    # print("_______________________________________")
    # print("How Is User check2", check2)
    # print("_______________________________________")

    if check1 or check2:
        can_send_friendship_request = False

    # JSON إرجاع البيانات كاستجابة
    return JsonResponse(
        {
            "user": user_serializer.data,
            "can_send_friendship_request": can_send_friendship_request,
        },
        safe=False,
    )


@api_view(["POST"])
def editprofile(request):
    # 👤 Get current user and new email data
    # 👤 احصل على بيانات بريد إلكتروني حالية وبيانات بريد إلكتروني جديدة
    user = request.user
    email = request.data.get("email")

    # 📧 Check if email is already in use by another user
    # 📧 تحقق مما إذا كان البريد الإلكتروني قيد الاستخدام بالفعل من قبل مستخدم آخر
    if User.objects.exclude(id=user.id).filter(email=email).exists():
        return JsonResponse({"message": "email already exists"})
    else:
        # 📝 Initialize profile form with request data and files
        # 📝 تهيئة نموذج الملف الشخصي مع بيانات الطلب والملفات
        form = ProfileForm(request.POST, request.FILES, instance=user)

        # ✅ Validate and save profile if valid
        # ✅ التحقق من صحة وحفظ الملف الشخصي إذا كان صالحًا
        if form.is_valid():
            form.save()

        # 🔄 Serialize updated user data
        # 🔄 قم بتسلسل بيانات المستخدم المحدثة
        serializer = UserSerializer(user)
        return JsonResponse({"message": "information updated", "user": serializer.data})


@api_view(["POST"])
def editpassword(request):
    # 🔒 Initialize password change form with request data
    # 🔒 تهيئة نموذج تغيير كلمة المرور مع بيانات الطلب
    user = request.user
    form = PasswordChangeForm(data=request.POST, user=user)

    # ✅ Validate and save new password if valid
    # ✅ التحقق من صحة وحفظ كلمة مرور جديدة إذا كانت صالحة
    if form.is_valid():
        form.save()
        return JsonResponse({"message": "success"})
    else:
        # ❌ Return errors if form is invalid
        # ❌ أخطاء الإرجاع إذا كان النموذج غير صالح
        return JsonResponse({"message": form.errors.as_json()}, safe=False)


# 🌐 Friendship Request and Friends Management API
# 🌐 واجهة برمجية لإدارة طلبات الصداقة وإدارة الأصدقاء
@api_view(["POST"])
def send_friendship_request(request, pk):
    # 👤 Get the user to whom the friendship request is being sent
    # 👤 جلب المستخدم الذي يتم إرسال طلب الصداقة إليه
    user = User.objects.get(pk=pk)
    # For Test
    # print("How Is User Send Friend Ship Request", pk)
    # print("_______________________________________")

    # 🔍 Check if a request already exists between the users
    # 🔍 التحقق مما إذا كان هناك طلب صداقة موجود بالفعل بين المستخدمين
    check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(
        created_by=user
    )
    check2 = FriendshipRequest.objects.filter(created_for=user).filter(
        created_by=request.user
    )
    # For Test
    # print("How Is User check1", check1)
    # print("_______________________________________")
    # print("How Is User check2", check2)
    # print("_______________________________________")

    if not check1 or not check2:
        # ✉️ Create a new friendship request if it doesn't exist
        # ✉️ إنشاء طلب صداقة جديد إذا لم يكن موجودًا
        friendrequest = FriendshipRequest.objects.create(
            created_for=user, created_by=request.user
        )
        # For Test
        # print("Friend Ship Request If ", friendrequest)
        # print("_______________________________________")
        # Return = The Message Show In Frontend
        return JsonResponse({"message": "friendship request created"})
    else:
        # Return = The Message Show In Frontend
        return JsonResponse({"message": "request already sent"})


@api_view(["GET"])
def friends(request, pk):
    # 👥 Get the friends and requests for the specified user
    # 👥 جلب الأصدقاء والطلبات للمستخدم المحدد
    user = User.objects.get(pk=pk)
    # print("Friends User By Id 👉️", user)

    requests = []
    # print("Friends Requests By Id 👉️", requests)

    # 📝 Check if the current user is the requested user
    # 📝 التحقق مما إذا كان المستخدم الحالي هو نفس المستخدم المطلوب
    if user == request.user:
        requests = FriendshipRequest.objects.filter(
            created_for=request.user, status=FriendshipRequest.NOT_SENT
        )
        # print("requests Friends", requests)
        requests = FriendshipRequestSerializer(requests, many=True)
        requests = requests.data

        # print("Friends Requests By Id 👉️", requests)

    # 👫 Retrieve all friends of the user
    # 👫 جلب جميع أصدقاء المستخدم
    friends = user.friends.all()
    # print("Friends Friends 👉️", friends)

    return JsonResponse(
        {
            "user": UserSerializer(user).data,
            "friends": UserSerializer(friends, many=True).data,
            "requests": requests,
        },
        safe=False,
    )


@api_view(["GET"])
def my_friendship_suggestions(request):
    # 🤝 Suggest users the current user may know
    # 🤝 اقتراح المستخدمين الذين قد يعرفهم المستخدم الحالي
    serializer = UserSerializer(request.user.people_you_may_know.all(), many=True)
    # print("🤝 Suggest users", serializer)
    return JsonResponse(serializer.data, safe=False)


@api_view(["POST"])
def handle_request(request, pk, status):
    # 🛠️ Handle and update the status of a friendship request
    # 🛠️ معالجة وتحديث حالة طلب الصداقة
    user = User.objects.get(pk=pk)
    # friendship_request = FriendshipRequest.objects.filter(created_for=request.user).get(
    #     created_by=user
    # )
    friendship_request = FriendshipRequest.objects.filter(
        created_for=request.user, created_by=user
    ).first()
    if not friendship_request:
        return JsonResponse(
            {"error": "Friendship request not found or already handled"}, status=404
        )
    # إذا كان يوجد طلب صداقة واحد فقط
    # friendship_request = friendship_requests.first()
    # استخدام first() بدلاً من get()

    if not friendship_request:
        return JsonResponse({"error": "Friendship request not found"}, status=404)

    friendship_request.status = status
    friendship_request.save()

    # 👥 Add each user to the other's friends list if accepted
    # 👥 إضافة كل مستخدم إلى قائمة أصدقاء الآخر إذا تم قبول الطلب
    user.friends.add(request.user)
    user.friends_count += 1
    user.save()

    request_user = request.user
    request_user.friends_count += 1
    request_user.save()

    # return JsonResponse({"message": "friendship request updated"})
    return JsonResponse({"message": f"Friendship request {status} successfully"})

```

### 🧑 Account Page [ urls.py ]

#### 🧑 App [ Account ] Page [ urls.py ] 📝

```python
urls.py
```

```python
# 📄 ملف [ lms/lms_django/account/urls.py ]

# 🌐 URL Configuration for User and Friend Management API
# 🌐 تكوين الروابط لواجهة برمجية لإدارة المستخدم والأصدقاء

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import api

urlpatterns = [
    # 👤 Retrieve current user's information استرجاع معلومات المستخدم الحالي
    path("me/", api.me, name="me"),
    # 📝 Signup for new users تسجيل مستخدمين جدد
    path("signup/", api.signup, name="signup"),
    # 🔑 Obtain JWT token for login الحصول على رمز JWT لتسجيل الدخول
    path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
    # ♻️ Refresh JWT token تحديث رمز
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # ___________________________
    # ___________________________
    # ___________________________
    # Profile
    path("profile/<uuid:id>/", api.profile, name="profile"),
    # ✏️ Edit user profile تعديل ملف المستخدم
    path("editprofile/", api.editprofile, name="editprofile"),
    # 🔒 Change user password تغيير كلمة مرور المستخدم
    path("editpassword/", api.editpassword, name="editpassword"),
    # ___________________________
    # ___________________________
    # ___________________________
    # All Friends
    # 👫 Retrieve friends of a user  استرجاع أصدقاء المستخدم
    path("friends/<uuid:pk>/", api.friends, name="friends"),
    # 🤝 Retrieve suggested friends استرجاع الأصدقاء المقترحين
    path(
        "friends/suggested/",
        api.my_friendship_suggestions,
        name="my_friendship_suggestions",
    ),
    # ✉️ Send friendship request إرسال طلب صداقة
    path(
        "friends/<uuid:pk>/request/",
        api.send_friendship_request,
        name="send_friendship_request",
    ),
    # 🛠️ Handle friendship request (accept/reject) معالجة طلب الصداقة (قبول/رفض)
    path("friends/<uuid:pk>/<str:status>/", api.handle_request, name="handle_request"),
]
```

### ⚙️ Project Page [ urls.py ]

#### ⚙ Project Page [ urls.py ] 📝

```python
# 📄 ملف [ lms/lms_django/lms_django/urls.py ]

# 🌐 Main URL Configuration for Django Project
# 🌐 تكوين الروابط الرئيسية لمشروع Django

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 🔗 Include URLs from the 'account' app for API endpoints
    # 🔗 تضمين روابط تطبيق 'account' للنقاط البرمجية
    path("api/", include("account.urls")),
    # 🔧 Admin panel for site management
    # 🔧 لوحة تحكم الإدارة لإدارة الموقع
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 🖼️ Serve media files during development
# 🖼️ عرض ملفات الوسائط أثناء التطوير

```

### 🧑 Create File Script

#### ⚙ Create Page [ generate_friend_suggestions.py ]

```python
scripts/generate_friend_suggestions.py
```

```python
# -*- coding: utf-8 -*-
# 🌐 تحديد نوع الترميز للملف كـ UTF-8 لدعم الأحرف غير اللاتينية.
# Set the file encoding to UTF-8 to support non-Latin characters.
# python scripts\generate_friend_suggestions.py

# 📚 استيراد مكتبة Django.
import django

# 📂 استيراد مكتبة os للتعامل مع نظام الملفات.
import os

# ⚙️ استيراد مكتبة sys للتعامل مع مسار Python والبيئة.
import sys

# ⏳ استيراد timedelta لحساب الفروقات الزمنية.
from datetime import timedelta

# 📊 استيراد Counter لحساب تكرار العناصر.
from collections import Counter

# 🕰️ استيراد timezone للتعامل مع التواريخ في Django.
from django.utils import timezone

# ➕ إضافة مسار المشروع الرئيسي إلى sys.path للتأكد من أن Python يمكنه العثور على الوحدات.
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

# ⚙️ إعداد متغير البيئة لاستخدام إعدادات Django.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lms_django.settings")

# 🚀 تشغيل إعدادات Django.
django.setup()


# 👥 استيراد نموذج المستخدم من تطبيق account.
from account.models import User

# 🔍 الحصول على جميع المستخدمين في قاعدة البيانات.
users = User.objects.all()


# 🔄 حلقة تمر على كل مستخدم في القائمة.
for user in users:
    # 🧹 مسح قائمة "الأشخاص الذين قد تعرفهم" للمستخدم الحالي.
    # Clear the "people you may know" list for the current user.
    user.people_you_may_know.clear()

    # 🔁 حلقة تمر على كل صديق للمستخدم.
    for friend in user.friends.all():
        # 📝 طباعة رسالة توضح أن المستخدم صديق مع الشخص الحالي.
        print("User:", user, "Is Friend With 🧑 ", friend)
        print("________________________________________________________________")

        # 🔁 حلقة تمر على أصدقاء الصديق (أصدقاء أصدقائي).
        for friendsfriend in friend.friends.all():
            # 🔎 طباعة قائمة الأصدقاء المقترحين.
            # print("Checking Suggested Friend 👉️ ", friendsfriend)
            # print("________________________________________________________________")
            # طباعة جميع أصدقاء المستخدم.
            # print("All Friends user.friends.all() 👉️ ", user.friends.all())
            # print("________________________________________________________________")
            # تحقق من أن الصديق ليس المستخدم نفسه وليس ضمن أصدقائه الحاليين.
            # print("All friendsfriend != user 👉️ ", friendsfriend != user)
            # print("________________________________________________________________")
            if friendsfriend != user and friendsfriend not in user.friends.all():
                print(
                    "Adding friend suggestion for:",
                    user,
                    f"✔️  Suggested Friend:",
                    friendsfriend,
                )

                # إضافة الصديق المقترح إلى قائمة "الأشخاص الذين قد تعرفهم".
                user.people_you_may_know.add(friendsfriend)
                # print("Added to suggestions 👉️ ", friendsfriend)
                # print(
                #     "________________________________________________________________"
                # )

    # طباعة سطر فارغ للوضوح بين المستخدمين.
    # print("Updated suggestions for user:", user)
    # print("Suggestions:", user.people_you_may_know.all())
    # print("----------------------------------------------------")

print("Finished updating 'people you may know' for all users.")


"""
شرح الكود بشكل عام:
🔹 الوصف العام: الكود يمر على جميع المستخدمين في قاعدة البيانات، ثم يحلل أصدقاء كل مستخدم ويبحث عن أصدقاء أصدقائه لإضافتهم إلى قائمة "الأشخاص الذين قد تعرفهم"، بشرط ألا يكون هؤلاء الأصدقاء موجودين بالفعل في قائمة أصدقاء المستخدم أو أن يكونوا المستخدم نفسه.
"""

```

### 👤 Superuser

#### ⚙ Create Superuser

```cmd
python manage.py createsuperuser
```

```cmd
Email: learncodingeasy0100@gmail.com
Password: ******
Password (again): ******
Superuser created successfully.
```

### 🚀 Run Server

###### 🚀 Run Server

```cmd
python manage.py runserver
```

###### 👉️ Go To

---

```cmd
http://127.0.0.1:8000/
```

```cmd
http://127.0.0.1:8000/admin
```

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

## Vue

### 🖥️ Create Vue Project

###### 📁 Create Vue Project

```cmd
npm create vue@latest
```

###### 🚀 Choose Vite [ Project name & Select a framework] 🛠️

```cmd
√ Project name: ... lms_vue
√ Add TypeScript? ... [No] / Yes
√ Add JSX Support? ... [No] / Yes
√ Add Vue Router for Single Page Application development? ... No / [Yes]
√ Add Pinia for state management? ... No / [Yes]
√ Add Vitest for Unit Testing? ... [No] / Yes
√ Add an End-to-End Testing Solution? » [No]
√ Add ESLint for code quality? ... No / [Yes]
√ Add Prettier for code formatting? ... No / [Yes]
√ Add Vue DevTools 7 extension for debugging? (experimental) ... [No] / Yes

Scaffolding project in E:\Projects\lms\lms_vue...

Done. Now run:
  cd lms_vue
  npm install
  npm run format
  npm run build
  npm run dev
```

```cmd
cd lms_vue
```

```cmd
npm install
```

```cmd
npm run format
```

```cmd
npm run build
```

```cmd
npm run dev
```

### 📚 Install Vue Libraries

###### 📚 Install Vue Libraries

- 1️⃣ Tailwind

```cmd
npm install -D tailwindcss postcss autoprefixer
```

```cmd
npx tailwindcss init -p
```

- 2️⃣ PrimeVue

```cmd
npm install primevue primeicons
```

```cmd
npm install @primevue/themes
```

```cmd
npm install quill
```

- 3️⃣ scss

```cmd
npm install -D sass@latest
```

- 4️⃣ Axios

```cmd
npm install axios
```

- 5️⃣ Font Awesome

```cmd
npm i --save @fortawesome/fontawesome-svg-core @fortawesome/vue-fontawesome@latest @fortawesome/vue-fontawesome@prerelease @fortawesome/free-solid-svg-icons @fortawesome/free-brands-svg-icons @fortawesome/free-regular-svg-icons
```

- 6️⃣ Pwa

```cmd
npm install -D vite-plugin-pwa
```

- 7️⃣ Prism

```cmd
npm i prismjs
```

```cmd
npm i vue-prism-component
```

- 8️⃣ Swiper

```cmd
npm i swiper
```

- 9️⃣

```cmd

```

### 📦 Setup Vue Libraries

###### 1️⃣ Tailwind

- Configure Tailwind

- 📝 File [ tailwind.config.js ]

```js
// Page [ lms/lms_vue/tailwind.config.js ]
export default defineConfig({
  // ...
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"]
  // ...
});
```

- 📝 File [ main.css ]

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

###### - 2️⃣ PrimeVue

- 📝 Create Page [ primeTheme.js ] Inside stores

```
primeTheme.js
```

```js
// Page [ lms/lms_vue/src/stores/primeTheme.js ]

import { reactive } from "vue";
export default {
  install: (app) => {
    const _appState = reactive({ theme: "Aura", darkTheme: false });
    app.config.globalProperties.$appState = _appState;
  }
};
```

- 📝 Create Page [ Theme/ThemeSwitcher.vue ] Inside components

```
Theme/ThemeSwitcher.vue
```

```html
<template>
  <span class="">
    <ul class="flex list-none m-0 p-0 gap-2 items-center">
      <li>
        <button
          type="button"
          class="inline-flex w-8 h-8 p-0 items-center justify-center surface-0 dark:surface-800 border border-surface-200 dark:border-surface-600 rounded-full"
          @click="onThemeToggler"
        >
          <i :class="`dark:text-white pi ${iconClass}`" />
        </button>
      </li>
    </ul>
  </span>
</template>
```

```js
<script>
  import { updatePreset, updateSurfacePalette } from '@primevue/themes'

  export default {
    data() {
      return {
        iconClass: 'pi-moon',
        selectedPrimaryColor: 'noir',
        selectedSurfaceColor: null
      }
    },
    methods: {
      onThemeToggler() {
        const root = document.getElementsByTagName('html')[0]
        root.classList.toggle('p-dark')
        this.iconClass = this.iconClass === 'pi-moon' ? 'pi-sun' : 'pi-moon'
      },

      updateColors(type, color) {
        if (type === 'primary') this.selectedPrimaryColor = color.name
        else if (type === 'surface') this.selectedSurfaceColor = color.name

        this.applyTheme(type, color)
      },
      applyTheme(type, color) {
        if (type === 'primary') {
          updatePreset(this.getPresetExt())
        } else if (type === 'surface') {
          updateSurfacePalette(color.palette)
        }
      },
      onRippleChange(value) {
        this.$primevue.config.ripple = value
      }
    },
    computed: {
      rippleActive() {
        return this.$primevue.config.ripple
      }
    }
  }
</script>
```

- 📝 Create Page [ presets/Noir.js ] Inside src

```
presets/Noir.js
```

```js
import { definePreset } from "@primevue/themes";
import Aura from "@primevue/themes/aura";

const Noir = definePreset(Aura, {
  semantic: {
    primary: {
      50: "{surface.50}",
      100: "{surface.100}",
      200: "{surface.200}",
      300: "{surface.300}",
      400: "{surface.400}",
      500: "{surface.500}",
      600: "{surface.600}",
      700: "{surface.700}",
      800: "{surface.800}",
      900: "{surface.900}",
      950: "{surface.950}"
    },
    colorScheme: {
      light: {
        primary: {
          color: "{primary.950}",
          contrastColor: "#ffffff",
          hoverColor: "{primary.900}",
          activeColor: "{primary.800}"
        },
        highlight: {
          background: "{primary.950}",
          focusBackground: "{primary.700}",
          color: "#ffffff",
          focusColor: "#ffffff"
        }
      },
      dark: {
        primary: {
          color: "{primary.50}",
          contrastColor: "{primary.950}",
          hoverColor: "{primary.100}",
          activeColor: "{primary.200}"
        },
        highlight: {
          background: "{primary.50}",
          focusBackground: "{primary.300}",
          color: "{primary.950}",
          focusColor: "{primary.950}"
        }
      }
    }
  }
});

export default Noir;
```

###### Import Inside main.js

```js
// --------------- PrimeVue Core Configuration ---------------
// Import PrimeVue library configuration
// استيراد مكتبة PrimeVue وإعداداتها الأساسية
import PrimeVue from "primevue/config";

// --------------- Popup Services (For Dialogs and Confirmations) ---------------
// Import services for confirmation and dialog popups
// خدمات النوافذ المنبثقة لتأكيد العمليات وفتح الحوارات
import ConfirmationService from "primevue/confirmationservice";
import DialogService from "primevue/dialogservice";

// Buttons
// الأزرار وزر التبديل
import Button from "primevue/button";
import ToggleButton from "primevue/togglebutton";

// --------------- Form Components ---------------
// Import components for creating forms
// عناصر النماذج
import Fluid from "primevue/fluid";
import InputText from "primevue/inputtext";
import Textarea from "primevue/textarea";
import Password from "primevue/password";
import FloatLabel from "primevue/floatlabel";
import Checkbox from "primevue/checkbox";
import RadioButton from "primevue/radiobutton";
import Listbox from "primevue/listbox";
import DatePicker from "primevue/datepicker";
import InputGroup from "primevue/inputgroup";
import InputGroupAddon from "primevue/inputgroupaddon";
import ColorPicker from "primevue/colorpicker";

// --------------- File Components ---------------
// Import file upload
// تحميل الملفات
import FileUpload from "primevue/fileupload";

// --------------- Menu Components ---------------
// Import components for building menus
// عناصر القائمة
import Menubar from "primevue/menubar";
import TieredMenu from "primevue/tieredmenu";

// --------------- Image Components ---------------
// Import components for handling images and avatars
// مكونات الصور والأفاتار
import Image from "primevue/image";
import Avatar from "primevue/avatar";
import AvatarGroup from "primevue/avatargroup";

// --------------- Popup Components ---------------
// Import popover, dialog, and drawer components for popups
// مكونات النوافذ المنبثقة
import Popover from "primevue/popover";
import Dialog from "primevue/dialog";
import Drawer from "primevue/drawer";

// --------------- Panel Components ---------------
// Import panel-related components for layout and navigation
// مكونات اللوحات لعرض المعلومات المنظمة
import Fieldset from "primevue/fieldset";
import Stepper from "primevue/stepper";
import StepList from "primevue/steplist";
import StepPanels from "primevue/steppanels";
import StepItem from "primevue/stepitem";
import Step from "primevue/step";
import StepPanel from "primevue/steppanel";

// --------------- Card Components ---------------
// Import card component for displaying content in card format
// مكون البطاقات لعرض المحتوى بطريقة منسقة
import Card from "primevue/card";

// --------------- Theme Components ---------------
// Import theme presets and theme switcher component
// مكونات اللوحات لعرض المعلومات المنظمة
import Noir from "./presets/Noir.js";
import ThemeSwitcher from "./components/Theme/ThemeSwitcher.vue";

// --------------- Notification Components ---------------
// Import toast and message components for notifications
import Toast from "primevue/toast";
import ToastService from "primevue/toastservice";
import Message from "primevue/message";

// --------------- Icon Components ---------------
// Import icon components for enhanced UI elements
import IconField from "primevue/iconfield";
import InputIcon from "primevue/inputicon";

// --------------- Editor Components ---------------
// Import rich text editor component (Quill-based)
import Editor from "primevue/editor";

// --------------- Table Components ---------------
// Import table components for data presentation
// Quill محرر النصوص الغنية المستندة إلى
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import ColumnGroup from "primevue/columngroup"; // optional
import Row from "primevue/row"; // optional

// --------------- Placeholder Components ---------------
// Import skeleton component for loading placeholders
import Skeleton from "primevue/skeleton";

// --------------- Placeholder Components ---------------
// Badge is a small status indicator for another element.
import Badge from "primevue/badge";
import OverlayBadge from "primevue/overlaybadge";

// --------------- Styles ---------------
// Import necessary styles for PrimeVue and Tailwind CSS
import "primeicons/primeicons.css";
import "tailwindcss/tailwind.css";

// --------------- Initialize PrimeVue ---------------
// Configure and initialize PrimeVue with theme settings
app.use(PrimeVue, {
  theme: {
    preset: Noir,
    options: {
      prefix: "p",
      darkModeSelector: ".p-dark",
      cssLayer: false
    }
  }
});

// Initialize and add services
// تهيئة وإضافة الخدمات
app.use(ConfirmationService);
app.use(DialogService);
app.use(ToastService);

// --------------- Register Components ---------------
// Register components in the application for global usage
// Prime Button
app.component("prime_button", Button);

// Theme Switcher Component
// مكون تبديل السمة
app.component("ThemeSwitcher", ThemeSwitcher);

// Form Components
app.component("prime_fluid", Fluid);
app.component("prime_input_text", InputText);
app.component("prime_textarea", Textarea);
app.component("prime_input_password", Password);
app.component("prime_float_label", FloatLabel);
app.component("prime_check_box", Checkbox);
app.component("prime_radio_button", RadioButton);
app.component("prime_list_box", Listbox);
app.component("prime_date_picker", DatePicker);
app.component("prime_input_group", InputGroup);
app.component("prime_input_group_addon", InputGroupAddon);
app.component("prime_file_upload", FileUpload);
app.component("prime_toggle_button", ToggleButton);
app.component("prime_color_picker", ColorPicker);

// Menu Components
app.component("prime_menubar", Menubar);
app.component("prime_tiered_menu", TieredMenu);

// Image Components
app.component("prime_image", Image);
app.component("prime_avatar", Avatar);
app.component("prime_avatar_group", AvatarGroup);

// Card Components
app.component("prime_card", Card);

// Popup Components
app.component("prime_popover", Popover);
app.component("prime_dialog", Dialog);
app.component("prime_drawer", Drawer);

// Panel Components
app.component("prime_fieldset", Fieldset);
app.component("prime_stepper", Stepper);
app.component("prime_steplist", StepList);
app.component("prime_steppanels", StepPanels);
app.component("prime_stepitem", StepItem);
app.component("prime_step", Step);
app.component("prime_steppanel", StepPanel);

// Notification Components
app.component("prime_toast", Toast);
app.component("prime_message", Message);

// Icon Components
app.component("prime_icon_field", IconField);
app.component("prime_input_icon", InputIcon);

// Editor Component
app.component("prime_editor", Editor);

// Table Components
app.component("prime_data_table", DataTable);
app.component("prime_column", Column);
app.component("prime_column_group", ColumnGroup);
app.component("prime_row", Row);

// Placeholder Components
app.component("prime_skeleton", Skeleton);

// Badge is a small status indicator for another element.
app.component("prime_badge", Badge);
app.component("prime_overlay_badge", OverlayBadge);
```

###### - 3️⃣ scss

###### 📂 Create Folder [scss] Inside assets And File [style.scss]

```
scss/style.scss
```

###### Import Inside main.js

```js
// My Style
import "./assets/scss/style.scss";
```

###### - 4️⃣ Axios

```js
// Axios  Import
// Axios  استيراد
import axios from "axios";
axios.defaults.baseURL = "http://127.0.0.1:8000";

app.use(router, axios);
```

###### - 5️⃣ Font Awesome

```html
<!-- Font Awesome -->
<link
  rel="stylesheet"
  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
/>
```

```js
// Page [ lms/lms_vue/src/main.js ]

// Font Awesome
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { fab } from "@fortawesome/free-brands-svg-icons";
import { far } from "@fortawesome/free-regular-svg-icons";
// Add Free Icons Styles To SVG Core
library.add(fas, far, fab);

// eslint-disable-next-line vue/multi-word-component-names
app.component("fa", FontAwesomeIcon);
```

###### - 6️⃣ Pwa

- 📝 Edit Page [ vite.config.js ]

```js
import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// For Pwa
// https://vite-pwa-org.netlify.app/guide/
import { VitePWA } from "vite-plugin-pwa";

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    // For Pwa
    VitePWA({
      registerType: "autoUpdate",
      workbox: {
        globPatterns: ["**/*.{js,css,html,ico,png,svg}"],
        clientsClaim: true,
        skipWaiting: true,
        cleanupOutdatedCaches: false,
        offlineGoogleAnalytics: true,
        sourcemap: true,
        runtimeCaching: [
          {
            urlPattern: ({ request }) =>
              request.destination === "document" ||
              request.destination === "script" ||
              request.destination === "style" ||
              request.destination === "image" ||
              request.destination === "font",
            handler: "StaleWhileRevalidate",
            options: {
              cacheName: "assets-cache",
              expiration: {
                maxEntries: 100,
                maxAgeSeconds: 60 * 60 * 24 * 30
              }
            }
          }
        ]
      },
      devOptions: {
        enabled: true
      },
      injectRegister: "auto",
      includeAssets: ["**/*"],
      manifest: {
        name: "Script Youtube",
        short_name: "Script Youtube",
        description: "My Awesome App Script Youtube",
        theme_color: "#ffffff",
        icons: [
          {
            src: "./images/icons/lms_icon_72x72.png",
            type: "image/png",
            sizes: "72x72",
            purpose: "any maskable"
          },
          {
            src: "./images/icons/lms_icon_96x96.png",
            type: "image/png",
            sizes: "96x96",
            purpose: "any maskable"
          },
          {
            src: "./images/icons/lms_icon_128x128.png",
            type: "image/png",
            sizes: "128x128",
            purpose: "any maskable"
          },
          {
            src: "./images/icons/lms_icon_144x144.png",
            type: "image/png",
            sizes: "144x144",
            purpose: "any maskable"
          },
          {
            src: "./images/icons/lms_icon_152x152.png",
            type: "image/png",
            sizes: "152x152",
            purpose: "any maskable"
          },
          {
            src: "./images/icons/lms_icon_192x192.png",
            type: "image/png",
            sizes: "192x192",
            purpose: "any maskable"
          },
          {
            src: "./images/icons/lms_icon_384x384.png",
            type: "image/png",
            sizes: "384x384",
            purpose: "any maskable"
          },
          {
            src: "./images/icons/lms_icon_512x512.png",
            type: "image/png",
            sizes: "512x512",
            purpose: "any maskable"
          }
        ],
        screenshots: [
          {
            src: "./images/screenshots/screenshots.png",
            sizes: "640x480",
            type: "image/png",
            form_factor: "wide"
            // "form_factor": "narrow"
          }
        ]
      }
    })
  ],
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url))
    }
  }
});
```

- 🖼️ Add Image Inside Public

```
images
```

```
icons
```

```
screenshots
```

```

├── public/
│ ├── images/
│ | ├── icons/
│ │ | ├── 🖼️ lms_icon_72x72.png
│ │ | ├── 🖼️ lms_icon_96x96.png
│ │ | ├── 🖼️ lms_icon_128x128.png
│ │ | ├── 🖼️ lms_icon_144x144.png
│ │ | ├── 🖼️ lms_icon_152x152.png
│ │ | ├── 🖼️ lms_icon_192x192.png
│ │ | ├── 🖼️ lms_icon_256x256.png
│ │ | ├── 🖼️ lms_icon_384x384.png
│ │ | ├── 🖼️ lms_icon_512x512.png
│ | ├── screenshots/
│ │ | ├── 🖼️ screenshots.png

```

```
lms_icon_72x72
lms_icon_96x96
lms_icon_128x128
lms_icon_144x144
lms_icon_152x152
lms_icon_192x192
lms_icon_256x256
lms_icon_384x384
lms_icon_512x512
screenshots_640x480
```

###### 👉️ Go To Website To Resize Image

```
https://www.iloveimg.com/resize-image
```

###### - 7️⃣ Prism

###### - 8️⃣ Swiper

###### - 9️⃣ Pinia

- 🧞‍♂️ User Store
- 📝 Create Page [ user.js ] Inside Stores

```
user.js
```

```js
// Page [ lms/lms_vue/src/stores/user.js ]
import { defineStore } from "pinia";
import axios from "axios";
export const useUserStore = defineStore({
  id: "user",
  state: () => ({
    user: {
      isAuthenticated: false,
      id: null,
      name: null,
      surname: null,
      email: null,
      date_of_birth: null,
      access: null,
      refresh: null,
      // 📋 Number of Friends عدد الاصدقاء
      friends_count: 0,
      // User gender 👤 جنس المستخدم
      gender: null,
      // 🖼️ Profile picture  صورة الملف الشخصي
      get_avatar: null,
      // 🖼️ Cover photo صورة الغلاف
      get_cover: null,
      // 📋 Number of tasks عدد المهام
      task_count: 0
    }
  }),
  actions: {
    // 🔄 Initialize the store
    // 🔄 تهيئة المخزن
    initStore() {
      if (localStorage.getItem("user.access")) {
        // console.log('User has access!')
        this.user.isAuthenticated = true;
        this.user.id = localStorage.getItem("user.id");
        this.user.name = localStorage.getItem("user.name");
        this.user.surname = localStorage.getItem("user.surname");
        this.user.email = localStorage.getItem("user.email");
        this.user.date_of_birth = localStorage.getItem("user.date_of_birth");
        this.user.gender = localStorage.getItem("user.gender");
        this.user.get_avatar = localStorage.getItem("user.get_avatar");
        this.user.get_cover = localStorage.getItem("user.get_cover");
        this.user.access = localStorage.getItem("user.access");
        this.user.refresh = localStorage.getItem("user.refresh");
        this.user.friends_count = localStorage.getItem("user.friends_count");
        this.user.task_count = localStorage.getItem("user.task_count");
        this.refreshToken();
      }
    },
    // 🔑 Set access and refresh tokens
    // 🔑 إعداد رموز الوصول والتحديث
    setToken(data) {
      // console.log('setToken', data)
      this.user.access = data.access;
      this.user.refresh = data.refresh;
      this.user.isAuthenticated = true;
      localStorage.setItem("user.access", data.access);
      localStorage.setItem("user.refresh", data.refresh);
      // console.log('user.access: ', localStorage.getItem('user.access'))
    },
    // ❌ Remove tokens and clear user data
    // ❌ إزالة الرموز ومسح بيانات المستخدم
    removeToken() {
      // console.log('removeToken')
      this.user.refresh = null;
      this.user.access = null;
      this.user.isAuthenticated = false;
      this.user.id = null;
      this.user.name = null;
      this.user.surname = null;
      this.user.email = null;
      this.user.date_of_birth = null;
      this.user.gender = null;
      this.user.get_avatar = null;
      this.user.get_cover = null;
      this.user.friends_count = null;
      this.user.task_count = null;

      localStorage.setItem("user.access", "");
      localStorage.setItem("user.refresh", "");
      localStorage.setItem("user.id", "");
      localStorage.setItem("user.name", "");
      localStorage.setItem("user.surname", "");
      localStorage.setItem("user.email", "");
      localStorage.setItem("user.date_of_birth", "");
      localStorage.setItem("user.gender", "");
      localStorage.setItem("user.get_avatar", "");
      localStorage.setItem("user.get_cover", "");
      localStorage.setItem("user.friends_count", "");
      localStorage.setItem("user.task_count", "");
    },
    // ✍️ Set user info in state and localStorage
    // ✍️ تعيين بيانات المستخدم في الحالة و localStorage
    setUserInfo(user) {
      // console.log('setUserInfo', user)
      this.user.id = user.id;
      this.user.name = user.name;
      this.user.surname = user.surname;
      this.user.email = user.email;
      this.user.date_of_birth = user.date_of_birth;
      this.user.gender = user.gender;
      this.user.get_avatar = user.get_avatar;
      this.user.get_cover = user.get_cover;
      this.user.friends_count = user.friends_count;
      this.user.task_count = user.task_count;
      localStorage.setItem("user.id", this.user.id);
      localStorage.setItem("user.name", this.user.name);
      localStorage.setItem("user.surname", this.user.surname);
      localStorage.setItem("user.email", this.user.email);
      localStorage.setItem("user.date_of_birth", this.user.date_of_birth);
      localStorage.setItem("user.gender", this.user.gender);
      localStorage.setItem("user.get_avatar", this.user.get_avatar);
      localStorage.setItem("user.get_cover", this.user.get_cover);
      localStorage.setItem("user.friends_count", this.user.friends_count);
      localStorage.setItem("user.task_count", this.user.task_count);
    },
    // 🔄 Refresh access token
    // 🔄 تحديث رمز الوصول
    refreshToken() {
      console.log("Attempting to refresh token:", this.user.refresh);
      // عرض قيمة الرمز
      axios
        .post("/api/refresh/", {
          refresh: this.user.refresh
        })
        .then((response) => {
          this.user.access = response.data.access;
          localStorage.setItem("user.access", response.data.access);
          axios.defaults.headers.common["Authorization"] =
            "Bearer " + response.data.access;
        })
        .catch((error) => {
          console.log(error);
          // عرض تفاصيل الخطأ
          console.log("Refresh token error:", error.response);
          this.removeToken();
        });
    }
  }
});
```

### 📝 Page [ index.html ]

```
cheang App Name [ lms | ]
```

### 🌊 Run Vue

###### Run Vue

```cmd
cd lms_vue
```

```cmd
npm install
```

```cmd
npm run format
```

```cmd
npm run build
```

```cmd
npm run dev
```

### 📝 Page Page Not Found

###### 📝 Create Page [PageNotFound.vue ] Inside Components

```
PageNotFound/PageNotFound.vue
```

```html
<template>
  <div class="PageNotFound">
    <div class="w-full">
      <img
        :src="imageSrc"
        @error="loadFallbackImage"
        alt="Page Not Found"
        class="img-fluid h-screen w-full"
      />
    </div>
  </div>
</template>
```

```js
<script>
  export default {
    name: 'PageNotFound',
    data() {
      return {
        // الرابط الأساسي للصورة من الإنترنت
        imageSrc:
          'https://raw.githubusercontent.com/LearnCodingEasy/Images/refs/heads/main/images/Page_Not_Found/404.jpg',
      }
    },
    methods: {
      loadFallbackImage() {
        // في حالة الخطأ، تغيير الصورة إلى المسار المحلي
        // eslint-disable-next-line no-undef
        this.imageSrc = require('../../Images/Page_Not_Found/404.jpg')
        console.log(`Bad`)
      },
    },
    mounted() {
      document.title = 'Trello | Page Not Found'
    },
  }
  </script>

```

```css
<style lang="scss">
  .PageNotFound {
    > div {
      height: calc(100vh - 70px);
    }
  }
</style>
```

### 📝 Page App

###### 📝 Edit Page [ App.vue ]

```js
<script setup>
  import { RouterLink, RouterView } from 'vue-router'
  import axios from 'axios'

  // import { ref } from 'vue'
  //
  import { onMounted } from 'vue'
  import { useUserStore } from '@/stores/user'
  import { useRouter } from 'vue-router'

  const userStore = useUserStore()
  userStore.initStore()
  const router = useRouter()

  onMounted(() => {
    // Perform any necessary operations on component mount
    if (!userStore.user.access) {
      // console.log('User Data: ', userStore.user.access)
      // Replace '/login' with your actual login route
      router.push('/login')
    } else {
      // Set default Authorization header for axios
      axios.defaults.headers.common['Authorization'] = `Bearer ${userStore.user.access}`
      // console.log('User Data: ', userStore.user)
    }
  })

  // For Toggle Theme
  // const op = ref(null)
  // const toggle = event => {
  //   // console.log('toggle: ', toggle);
  //   op.value.toggle(event)
  // }
  // Log Out
  let logout = () => {
    // console.log('User Log out')
    userStore.removeToken()
    // توجيه المستخدم إلى صفحة تسجيل الدخول
    setTimeout(() => {
      router.push('/login').then(() => {})
    }, 10)
  }
</script>
```

```html
<template>
  <div class="wrapper_page_app">
    <!-- Header Tailwind -->
    <div class="header_wrapper sticky top-0 left-0 right-0">
      <div class="container mx-auto">
        <div class="header_inner">
          <prime_card
            class="header_card px-2"
            v-if="userStore.user.isAuthenticated"
          >
            <template #content>
              <header class="header_header">
                <nav class="header_nav">
                  <div class="header_content">
                    <div
                      class="header_content_inner relative flex items-center justify-between"
                    >
                      <div
                        class="header_mobile_menu_button absolute inset-y-0 left-0 flex items-center sm:hidden"
                      >
                        <!-- Mobile menu button-->
                        <button
                          type="button"
                          class="relative inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-blue-600 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
                          aria-controls="mobile-menu"
                          aria-expanded="false"
                        >
                          <span class="absolute -inset-0.5"></span>
                          <span class="sr-only">Open main menu</span>
                          <!--
                  Icon when menu is closed.

                  Menu open: "hidden", Menu closed: "block"
                -->
                          <svg
                            class="block h-6 w-6"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke-width="1.5"
                            stroke="currentColor"
                            aria-hidden="true"
                            data-slot="icon"
                          >
                            <path
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"
                            />
                          </svg>
                          <!--
                  Icon when menu is open.

                  Menu open: "block", Menu closed: "hidden"
                -->
                          <svg
                            class="hidden h-6 w-6"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke-width="1.5"
                            stroke="currentColor"
                            aria-hidden="true"
                            data-slot="icon"
                          >
                            <path
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              d="M6 18 18 6M6 6l12 12"
                            />
                          </svg>
                        </button>
                      </div>
                      <div
                        class="header_wrapper_links flex flex-1 items-center justify-center sm:items-stretch sm:justify-start"
                      >
                        <div
                          class="header_logo_link flex flex-shrink-0 items-center"
                        >
                          <!-- Logo -->
                          <RouterLink to="/" class="logo flex">
                            <img
                              class="h-10 w-auto"
                              src="../"
                              alt="Your Company"
                            />
                          </RouterLink>
                        </div>
                        <div class="header_main_links hidden sm:ml-6 sm:block">
                          <div class="header_main_link flex space-x-4">
                            <RouterLink
                              to="/Workspace"
                              class="rounded-md px-3 py-2 text-md"
                              aria-current="page"
                            >
                              workspace</RouterLink
                            >
                            <RouterLink
                              to="/"
                              class="rounded-md px-3 py-2 text-md"
                              >Recent
                            </RouterLink>
                            <RouterLink
                              to="/"
                              class="rounded-md px-3 py-2 text-md"
                              >Starred
                            </RouterLink>
                            <RouterLink
                              to="/"
                              class="rounded-md px-3 py-2 text-md"
                              >More
                            </RouterLink>
                            <prime_button
                              icon="pi pi-plus"
                              severity="info"
                              @click="visibleAddBoard = true"
                              class="class_name"
                            />
                          </div>
                        </div>
                      </div>
                      <div
                        class="header_wrapper_profile_search absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0"
                      >
                        <!-- input_search -->
                        <div class="header_input_search">
                          <prime_input_text></prime_input_text>
                        </div>
                        <button
                          type="button"
                          class="relative rounded-full bg-gray-800 p-1 text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800"
                        >
                          <span class="absolute -inset-1.5"></span>
                          <span class="sr-only">View notifications</span>
                          <svg
                            class="h-6 w-6"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke-width="1.5"
                            stroke="currentColor"
                            aria-hidden="true"
                            data-slot="icon"
                          >
                            <path
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              d="M14.857 17.082a23.848 23.848 0 0 0 5.454-1.31A8.967 8.967 0 0 1 18 9.75V9A6 6 0 0 0 6 9v.75a8.967 8.967 0 0 1-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 0 1-5.714 0m5.714 0a3 3 0 1 1-5.714 0"
                            />
                          </svg>
                        </button>
                        <!-- Profile  -->
                        <div class="relative ml-3">
                          <div>
                            <button
                              type="button"
                              class="relative flex rounded-full bg-gray-800 text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800"
                              id="user-menu-button"
                              aria-expanded="false"
                              aria-haspopup="true"
                              @click="toggleDropdown"
                            >
                              <span class="absolute -inset-1.5"></span>
                              <span class="sr-only">Open user menu</span>
                              <img
                                v-if="userStore.user.get_avatar !== 'undefined'"
                                :src="userStore.user.get_avatar"
                                class="h-8 w-8 rounded-full"
                                alt=""
                              />
                              <img
                                v-else
                                class="h-8 w-8 rounded-full"
                                src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                                alt=""
                              />
                            </button>
                          </div>
                          <!-- dropdown -->
                          <div
                            v-if="isDropdownOpen"
                            class="border absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none"
                            role="menu"
                            aria-orientation="vertical"
                            aria-labelledby="user-menu-button"
                            tabindex="-1"
                          >
                            <!-- User Profile -->
                            <div
                              class="div_wrapper_profile flex py-1 items-center cursor-pointer"
                            >
                              <div
                                class="icon_div_wrapper_profile flex justify-center items-center"
                              >
                                <RouterLink
                                  class="flex justify-center items-center"
                                  v-if="userStore.user.id"
                                  :to="{
                                    name: 'profile',
                                    params: { id: userStore.user.id },
                                  }"
                                  @click="closeDropdown"
                                >
                                  <!-- If Image -->
                                  <div class="mr-1">
                                    <span
                                      class="user_img"
                                      v-if="userStore.user.get_avatar !== 'undefined'"
                                    >
                                      <img
                                        :src="userStore.user.get_avatar"
                                        class="rounded-full w-8 h-8"
                                        alt=""
                                      />
                                    </span>
                                    <span class="user_icon" v-else>
                                      <i
                                        class="pi pi-user px-2"
                                        shape="circle"
                                      ></i>
                                    </span>
                                  </div>
                                  <!-- If Name -->
                                  <div class="">
                                    <span
                                      class="user_name"
                                      v-if="userStore.user.name"
                                      >{{ userStore.user.name }}</span
                                    >
                                    <span class="user_name" v-else
                                      >Your Profile</span
                                    >
                                  </div>
                                </RouterLink>
                              </div>
                            </div>
                            <!-- Settings -->
                            <div
                              class="div_wrapper_logout flex py-1 items-center cursor-pointer"
                            >
                              <div
                                class="icon_logout flex justify-center items-center"
                                @click="closeDropdown"
                              >
                                <i class="pi pi-cog px-2" shape="circle"></i>
                                <button class="">Settings</button>
                              </div>
                            </div>
                            <!-- Sign Out -->
                            <div
                              class="div_wrapper_logout flex py-1 items-center cursor-pointer"
                              @click="logout"
                            >
                              <div
                                class="icon_logout flex justify-center items-center"
                                @click="closeDropdown"
                              >
                                <i
                                  class="pi pi-sign-out px-2"
                                  shape="circle"
                                ></i>
                                <button class="">Sign out</button>
                              </div>
                            </div>
                            <!-- Toggle Theme -->
                            <div
                              class="flex div_wrapper_toggle_theme cursor-pointer"
                              @click="closeDropdown"
                            >
                              <ThemeSwitcher />
                              <span class="mb-2">Toggle theme</span>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- Mobile menu, show/hide based on menu state. -->
                  <div class="sm:hidden" id="mobile-menu">
                    <div class="space-y-1 px-2 pb-3 pt-2">
                      <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
                      <a
                        href="#"
                        class="block rounded-md bg-gray-900 px-3 py-2 text-base font-medium text-white"
                        aria-current="page"
                        >Dashboard</a
                      >
                      <a
                        href="#"
                        class="block rounded-md px-3 py-2 text-base font-medium text-gray-300 hover:bg-gray-700 hover:text-white"
                        >Team</a
                      >
                      <a
                        href="#"
                        class="block rounded-md px-3 py-2 text-base font-medium text-gray-300 hover:bg-gray-700 hover:text-white"
                        >Projects</a
                      >
                      <a
                        href="#"
                        class="block rounded-md px-3 py-2 text-base font-medium text-gray-300 hover:bg-gray-700 hover:text-white"
                        >Calendar</a
                      >
                    </div>
                  </div>
                </nav>
              </header>
            </template>
          </prime_card>
        </div>
      </div>
    </div>
    <prime_toast />

    <RouterView />
  </div>
</template>
```

```js
<script>
  export default {
    data() {
      return {
        // تعريف الخاصية
        visibleAddBoard: false,
        isDropdownOpen: false,
      }
    },
    mounted() {
      document.title = 'Trello | Home'
    },
    methods: {
      toggleDropdown() {
        this.isDropdownOpen = !this.isDropdownOpen
      },
      closeDropdown() {
        this.isDropdownOpen = false
      },
    },
  }
</script>
```

```css
<style lang="scss">
  .header_right_section {
    a,
    RouterLink {
      margin: 0 0.5rem;
    }
  }

  .wrapper_page_app {
    .header_wrapper {
      border-bottom: 1px solid #99999985;
      z-index: 7;
      .container {
        .header_inner {
          .header_card {
            border-radius: 0;
            box-shadow: none;

            > div {
              padding: 0;

              header.header_header {
                nav.header_nav {
                  .header_content {
                    .header_content_inner {
                      .header_mobile_menu_button {
                        button {
                          border: 0.1rem solid #085dd8;
                        }
                      }

                      .header_wrapper_links {
                        .header_logo_link {
                          .logo {
                            img {
                            }
                          }
                        }

                        .header_main_links {
                          .header_main_link {
                            a {
                            }

                            button {
                              background-color: #085dd8;
                              border: 0;
                              color: white;
                            }
                          }
                        }
                      }

                      .header_wrapper_profile_search {
                        .header_input_search {
                          margin: 0 0.5rem;
                          height: 30px;

                          input {
                            border-radius: 3px;
                            height: 100%;
                            box-shadow: none;
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
</style>
```

### 📝 Page Login

###### 📝 Create Page [ LoginView.vue ] Inside [ Authentication ]

```
Authentication/LoginView.vue
```

```js

<script>
  import axios from 'axios'
  // eslint-disable-next-line no-unused-vars
  import { RouterLink } from 'vue-router'
  import { useUserStore } from '@/stores/user'
  export default {
    name: 'loginView',
    setup() {
      const userStore = useUserStore()
      return {
        userStore,
      }
    },
    data() {
      return {
        formLogin: {
          email: '',
          password: '',
        },
        errorsLogin: [],

        // Signup
        formSignup: {
          name: '',
          surname: '',
          email: '',
          date_of_birth: null,
          gender: '',
          password1: '',
          password2: '',
        },
        day: '',
        month: '',
        year: '',
        errorsSignup: [],
      }
    },
    methods: {
      async submitFormLogin() {
        this.errorsLogin = []
        if (this.formLogin.email === '') {
          this.$toast.add({
            severity: 'error',
            summary: 'User Name missing',
            detail: 'Your name is missing',
            life: 3000,
          })
          this.errorsLogin.push('Your e-mail is missing')
        }
        if (this.formLogin.password === '') {
          this.$toast.add({
            severity: 'error',
            summary: 'User password is missing',
            detail: 'Your password is missing',
            life: 3000,
          })
          this.errorsLogin.push('Your password is missing')
        }
        if (this.errorsLogin.length === 0) {
          await axios
            .post('/api/login/', this.formLogin)
            .then((response) => {
              this.userStore.setToken(response.data)
              // console.log('response.data: ', response.data)
              axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access
            })
            .catch((error) => {
              console.log('error', error)
              if (error.response.data.detail) {
                // Code If True
                this.$toast.add({
                  severity: 'error',
                  summary: 'Error Message',
                  detail: `${error.response.data.detail}`,
                  life: 6000,
                })
              }

              this.errorsLogin.push(
                'The email or password is incorrect! Or the user is not activated!',
              )
            })
        }
        if (this.errorsLogin.length === 0) {
          await axios
            .get('/api/me/')
            .then((response) => {
              this.userStore.setUserInfo(response.data)
              this.$router.push('/')
            })
            .catch((error) => {
              console.log('error', error)
            })
        }
      },
      submitFormSignup() {
        this.errorsSignup = []

        // استخراج اليوم، الشهر، والسنة من كائنات Date وتنسيقها
        const day = this.day.getDate().toString().padStart(2, '0')
        const month = (this.month.getMonth() + 1).toString().padStart(2, '0')
        const year = this.year.getFullYear()

        const formattedDate = `${year}-${month}-${day}`
        this.formSignup.date_of_birth = formattedDate

        if (this.formSignup.name === '') {
          this.$toast.add({
            severity: 'error',
            summary: 'User Name missing',
            detail: 'Your name is missing',
            life: 3000,
          })
          this.errorsSignup.push('Your name is missing')
        }
        if (this.formSignup.surname === '') {
          this.$toast.add({
            severity: 'error',
            summary: 'User Surname missing',
            detail: 'Your Surname is missing',
            life: 3000,
          })
          this.errorsSignup.push('Your surname is missing')
        }
        if (this.formSignup.email === '') {
          this.$toast.add({
            severity: 'error',
            summary: 'User Is missing',
            detail: 'Your e-mail is missing',
            life: 3000,
          })
          this.errorsSignup.push('Your e-mail is missing')
        }
        if (this.formSignup.password1 === '') {
          this.$toast.add({
            severity: 'error',
            summary: 'User passwordIs missing',
            detail: 'Your password is missing',
            life: 3000,
          })
          this.errorsSignup.push('Your password is missing')
        }
        if (this.formSignup.password1 !== this.formSignup.password2) {
          this.$toast.add({
            severity: 'error',
            summary: 'User  password does not match',
            detail: 'Your password  does not match',
            life: 3000,
          })
          this.errorsSignup.push('The password does not match')
        }
        if (this.errorsSignup.length === 0) {
          axios
            .post('/api/signup/', this.formSignup)
            .then((response) => {
              if (response.data.message === 'success') {
                if (response.data.email_sent) {
                  this.$toast.add({
                    severity: 'success',
                    summary: 'User Registered',
                    detail: 'Please activate your account by clicking the link sent to your email.',
                    life: 3000,
                  })
                }
                this.$toast.add({
                  severity: 'success',
                  summary: 'User Is Registered',
                  detail: 'Please activate your account by clicking your email link',
                  life: 3000,
                })
                this.formSignup.name = ''
                this.formSignup.surname = ''
                this.formSignup.email = ''
                this.formSignup.date_of_birth = ''
                this.formSignup.gender = ''
                this.formSignup.password1 = ''
                this.formSignup.password2 = ''
                // this.$router.push('/loginView')
                window.location.reload()
              } else {
                const data = JSON.parse(response.data.message)
                this.$toast.add({
                  severity: 'error',
                  summary: 'Error Message',
                  detail: 'Message Content Something went wrong. Please try again',
                  life: 6000,
                })
                for (const key in data) {
                  this.errors.push(data[key][0].message)
                }
                console.log(`Bad`, this.formSignup.date_of_birth)
                console.log(`Day`, this.day)
                console.log(`month`, this.month)
                console.log(`year`, this.year)
              }
            })
            .catch((error) => {
              console.log('error', error)
            })
        }
      },
    },
    mounted() {
      document.title = 'Trello | Login'
    },
  }
  </script>

```

```html
<template>
  <div class="wrapper_page_login">
    <div class="inner_page_login">
      <div class="container mx-auto">
        <div
          class="wrapper_content_page_login flex justify-center items-center"
        >
          <div class="inner_content_page_login">
            <!-- Signup -->
            <div class="mobile_body_dark">
              <span class="voice_up"> </span>
              <span class="voice_down"> </span>
              <span class="power"> </span>
              <span class="sonser"> </span>
              <span class="voice"> </span>
              <span class="carme"> </span>
              <div class="mobile_content">
                <form class="">
                  <prime_card class="prime_card_form_signup">
                    <template #header>
                      <div class="flex justify-between items-center w-full">
                        <div class="text font-bold text-5xl">Signup</div>
                        <div class="image_logo">
                          <img
                            src="../../assets/Images/Messenger_80x80.png"
                            class=""
                            alt=""
                          />
                        </div>
                      </div>
                    </template>
                    <template #content>
                      <prime_fluid class="prime_card_form_signup_content">
                        <div class="">
                          <div class="flex">
                            <!-- First name -->
                            <div class="mr-1">
                              <prime_input_text
                                placeholder="First name"
                                v-model="formSignup.name"
                              />
                            </div>
                            <!-- Surname -->
                            <div class="ml-1">
                              <prime_input_text
                                placeholder="Surname"
                                v-model="formSignup.surname"
                              />
                            </div>
                          </div>
                          <!-- Mobile number or email address -->
                          <div class="col-span-full">
                            <prime_input_text
                              placeholder="Mobile number or email address"
                              v-model="formSignup.email"
                            />
                          </div>
                          <!-- password1 -->
                          <div class="col-span-full">
                            <prime_input_password
                              placeholder="New Password"
                              v-model="formSignup.password1"
                            />
                          </div>
                          <!-- password2 -->
                          <div class="col-span-full">
                            <prime_input_password
                              placeholder="Repeat password"
                              v-model="formSignup.password2"
                            />
                          </div>
                          <!-- Date of birth -->
                          <div class="col-span-full">Date of birth</div>
                          <div class="col-span-full">
                            <div class="flex flex-col md:flex-row gap-2">
                              <!-- Day -->
                              <prime_input_group>
                                <prime_date_picker
                                  v-model="day"
                                  view="day"
                                  dateFormat="dd"
                                />
                              </prime_input_group>
                              <!-- Month -->
                              <prime_input_group>
                                <prime_date_picker
                                  v-model="month"
                                  view="month"
                                  dateFormat="mm"
                                />
                              </prime_input_group>
                              <!-- Year -->
                              <prime_input_group>
                                <prime_date_picker
                                  v-model="year"
                                  view="year"
                                  dateFormat="yy"
                                />
                              </prime_input_group>
                            </div>
                          </div>
                          <!-- Gender -->
                          <div class="col-span-full">Gender</div>
                          <div class="flex flex-col md:flex-row gap-2">
                            <prime_input_group>
                              <prime_radio_button
                                v-model="formSignup.gender"
                                inputId="ingredient1"
                                name="gender"
                                value="Female"
                              />
                              <label for="ingredient1" class="ml-2">
                                Female
                              </label>
                            </prime_input_group>
                            <prime_input_group>
                              <prime_radio_button
                                v-model="formSignup.gender"
                                inputId="ingredient2"
                                name="gender"
                                value="Male"
                              />
                              <label for="ingredient2" class="ml-2">
                                Male
                              </label>
                            </prime_input_group>

                            <prime_input_group>
                              <prime_radio_button
                                v-model="formSignup.gender"
                                inputId="ingredient3"
                                name="gender"
                                value="Custom"
                              />
                              <label for="ingredient3" class="ml-2">
                                Custom
                              </label>
                            </prime_input_group>
                          </div>
                        </div>
                      </prime_fluid>
                    </template>
                    <template #footer>
                      <div class="flex justify-center gap-2">
                        <button
                          type="submit"
                          class="d_block_important mt-1 mx-auto w_50 bg-green-500 py-3 px-5 rounded text-white"
                          @click.prevent="submitFormSignup"
                        >
                          Signup
                        </button>
                      </div>
                    </template>
                    <!-- Errors -->
                    <template v-if="errorsSignup.length > 0">
                      <prime_toast />
                    </template>
                  </prime_card>
                </form>
              </div>
            </div>
            <!-- Log in -->
            <div class="mobile_body_dark">
              <span class="voice_up"> </span>
              <span class="voice_down"> </span>
              <span class="power"> </span>
              <span class="sonser"> </span>
              <span class="voice"> </span>
              <span class="carme"> </span>
              <div class="mobile_content">
                <form class="">
                  <prime_card class="prime_card_form_login">
                    <template #header>
                      <div class="flex justify-between items-center w-full">
                        <div class="text font-bold text-5xl">Log in</div>
                        <div class="image_logo">
                          <img
                            src="../../assets/Images/Messenger_80x80.png"
                            class=""
                            alt=""
                          />
                        </div>
                      </div>
                    </template>
                    <template #content>
                      <prime_fluid class="prime_card_form_signup_content">
                        <div class="input_email">
                          <!-- Mobile number or email address -->
                          <div class="col-span-full">
                            <prime_input_text
                              placeholder="Mobile number or email address"
                              v-model="formLogin.email"
                            />
                          </div>
                        </div>
                      </prime_fluid>
                      <!-- password -->
                      <div class="input_password">
                        <prime_input_password
                          placeholder="Your Password"
                          v-model="formLogin.password"
                        />
                      </div>
                      <div class="Forgotten_password">
                        <a
                          href="#"
                          class="text-blue-600 mx-auto my-2 block text-center"
                          >Forgotten password?</a
                        >
                        <hr />
                      </div>
                    </template>
                    <template #footer>
                      <div class="row">
                        <!-- Errors -->
                        <template v-if="errorsLogin.length > 0">
                          <prime_toast></prime_toast>
                        </template>
                        <!-- Login -->
                        <div class="mt-2">
                          <button
                            type="submit"
                            class="d_block_important mt-1 mb-2 mx-auto w_100 bg-red-500 py-3 px-5 rounded text-white"
                            @click.prevent="submitFormLogin"
                          >
                            Log In
                          </button>

                          <!-- Button Signup -->
                        </div>
                      </div>
                    </template>
                  </prime_card>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <prime_toast />
  </div>
</template>
```

```css
<style lang="scss">
  * {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
  }

  .wrapper_page_login {
    padding: 0;
    margin: 0;
    height: 99.99vh;
    max-height: 100vh;
    overflow: hidden;
    background-image: linear-gradient(to right, #5b66f6, #e54da4);
    .inner_page_login {
      height: 100%;
      .container {
        height: 100%;
        .wrapper_content_page_login {
          height: 100%;
          .inner_content_page_login {
            position: relative;
            height: 85%;
            width: 100%;
            margin: auto;
            display: grid;
            grid-gap: 5%;
            justify-content: space-between;
            align-items: center;
            // screen and (max-width: 568px)
            // @include MediaQueries(Xxs) {}
            @include MediaQueries(Mobile) {
              // background-color: #ffa704;
            }
            // screen and (min-width: 569px) and (max-width: 767px)
            // @include MediaQueries(Xs) {}
            @include MediaQueries(Tablet) {
              // background-color: #b3f5b3;
            }
            // screen and (min-width: 768px) and (max-width: 991px)
            // @include MediaQueries(Md) {}
            @include MediaQueries(laptop) {
              // background-color: #b3d4f5;
            }
            // screen and (min-width: 992px) and (max-width: 1199px)
            // @include MediaQueries(Lg) {  }
            @include MediaQueries(laptopLg) {
            }
            // screen and (min-width: 1200px) and (max-width: 1399px)
            // @include MediaQueries(Xlg) {}
            @include MediaQueries(Desktop) {
              grid-template-columns: repeat(auto-fill, minmax(35%, 1fr));
            }
            // screen and (min-width: 1400px)
            // @include MediaQueries(Xxlg) {}
            @include MediaQueries(DesktopLg) {
              grid-template-columns: repeat(auto-fill, minmax(35%, 1fr));
            }

            .mobile_body {
              border: 0.5rem solid #130e0e;
              border-radius: 32px;
              -webkit-border-radius: 32px;
              -moz-border-radius: 32px;
              -ms-border-radius: 32px;
              -o-border-radius: 32px;
              height: 100%;
              margin: auto;
              position: relative;
              position: relative;
              // screen and (max-width: 568px)
              // @include MediaQueries(Xxs) {}
              @include MediaQueries(Mobile) {
                &::after {
                  content: '📱 568';
                  position: absolute;
                  top: 0%;
                  left: 0px;
                  border-radius: 0.5rem;
                  z-index: 7;
                  font-size: 20px;
                  font-weight: bold;
                  background-color: #130e0e;
                  color: #fff;
                  padding: 10px 15px;
                }
              }
              // screen and (min-width: 569px) and (max-width: 767px)
              // @include MediaQueries(Xs) {}
              @include MediaQueries(Tablet) {
                &::after {
                  content: '📱 567 767';
                  position: absolute;
                  top: 0%;
                  left: 0px;
                  border-radius: 0.5rem;
                  z-index: 7;
                  font-size: 20px;
                  font-weight: bold;
                  background-color: #130e0e;
                  color: #fff;
                  padding: 10px 15px;
                }
              }
              // screen and (min-width: 768px) and (max-width: 991px)
              // @include MediaQueries(Md) {}
              @include MediaQueries(laptop) {
                &::after {
                  content: '💻 768 991';
                  position: absolute;
                  top: 0%;
                  left: 0px;
                  border-radius: 0.5rem;
                  z-index: 7;
                  font-size: 20px;
                  font-weight: bold;
                  background-color: #130e0e;
                  color: #fff;
                  padding: 10px 15px;
                }
              }
              // screen and (min-width: 992px) and (max-width: 1199px)
              // @include MediaQueries(Lg) {}
              @include MediaQueries(laptopLg) {
                &::after {
                  content: '💻➕ 992 1199';
                  position: absolute;
                  top: 0%;
                  left: 0px;
                  border-radius: 0.5rem;
                  z-index: 7;
                  font-size: 20px;
                  font-weight: bold;
                  background-color: #130e0e;
                  color: #fff;
                  padding: 10px 15px;
                }
              }
              // screen and (min-width: 1200px) and (max-width: 1399px)
              // @include MediaQueries(Xlg) {}
              @include MediaQueries(Desktop) {
                &::after {
                  content: '🖥️ 1200 1399';
                  position: absolute;
                  top: 0%;
                  left: 0px;
                  border-radius: 0.5rem;
                  z-index: 7;
                  font-size: 20px;
                  font-weight: bold;
                  background-color: #130e0e;
                  color: #fff;
                  padding: 10px 15px;
                  display: none;
                }
                width: 50%;
                overflow-x: hidden;
              }
              // screen and (min-width: 1400px)
              // @include MediaQueries(Xxlg) {}
              @include MediaQueries(DesktopLg) {
                &::after {
                  content: '🖥️➕ 1400';
                  position: absolute;
                  top: 0%;
                  left: 0px;
                  border-radius: 0.5rem;
                  z-index: 7;
                  font-size: 20px;
                  font-weight: bold;
                  background-color: #130e0e;
                  color: #fff;
                  padding: 10px 15px;
                  display: none;
                }
                width: 50%;
              }
              .mobile_content {
                position: relative;
                border-radius: 24px;
                -webkit-border-radius: 24px;
                -moz-border-radius: 24px;
                -ms-border-radius: 24px;
                -o-border-radius: 24px;
                border: 0.2rem solid #130e0e;
                height: 100%;
                background-color: #fff;
                padding: 1rem;
                display: flex;
                justify-content: space-between;
                align-items: center;
                form {
                  height: 100%;
                  display: flex;
                  justify-content: space-between;
                  align-items: center;
                  width: 100%;
                  .prime_card_form_signup {
                    border: none;
                    padding: 0;
                    margin: 0;
                    box-shadow: none;
                    height: 100%;
                    max-height: 100%;
                    overflow: hidden;
                    border-radius: 0px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    div.p-card-header {
                      height: 20%;
                      width: 100%;
                      display: flex;
                      align-items: center;
                      width: 100%;
                    }
                    div.p-card-body {
                      padding: 0;
                      margin: 0;
                      margin-bottom: 1rem;
                      height: 80%;
                      display: flex;
                      flex-direction: column;
                      div.p-card-content {
                        height: 80%;
                        .prime_card_form_signup_content {
                          > div {
                            display: flex;
                            flex-direction: column;
                            justify-content: space-between;
                            > div {
                              margin-top: 1rem;
                            }
                          }
                        }
                      }
                      div.p-card-footer {
                        height: 20%;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                      }
                    }
                  }
                  .prime_card_form_login {
                    border: none;
                    padding: 0;
                    margin: 0;
                    box-shadow: none;
                    height: 100%;
                    max-height: 100%;
                    overflow: hidden;
                    border-radius: 0px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    width: 100%;
                    div.p-card-header {
                      height: 20%;
                      width: 100%;
                      display: flex;
                      align-items: center;
                      width: 100%;
                    }
                    div.p-card-body {
                      padding: 0;
                      margin: 0;
                      margin-bottom: 1rem;
                      height: 80%;
                      display: flex;
                      flex-direction: column;
                      width: 100%;
                      div.p-card-content {
                        // height: 80%;
                        .input_email {
                          margin-bottom: 1rem;
                          input {
                            width: 100%;
                          }
                        }
                        .input_password {
                          margin-bottom: 1rem;
                          > div {
                            width: 100%;
                            input {
                              width: 100%;
                            }
                          }
                        }
                        .Forgotten_password {
                          margin-bottom: 1rem;
                        }
                      }
                      div.p-card-footer {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                      }
                    }
                  }
                }
              }
              .voice_up,
              .voice_down,
              .power {
                content: '';
                position: absolute;
                height: 70px;
                width: 13px;
                background-color: #130e0e;
                border-radius: 5px;
                z-index: 7;
                //rotate: 90deg;
                -webkit-border-radius: 5px;
                -moz-border-radius: 5px;
                -ms-border-radius: 5px;
                -o-border-radius: 5px;
              }
              .voice_up {
                top: 10%;
                left: -13px;
              }
              .voice_down {
                top: 24%;
                left: -13px;
              }
              .power {
                top: 17%;
                right: -13px;
              }
              .sonser,
              .voice {
                position: absolute;
                z-index: 7;
              }
              .sonser {
                height: 15px;
                background-color: #130e0e;
                width: 33.33%;
                left: 33.33%;
                border-radius: 0 0 15px 15px;
              }
              .voice {
                height: 5px;
                background-color: #b3b0b0;
                width: 15%;
                left: 42.5%;
                border-radius: 15px;
                -webkit-border-radius: 15px;
                -moz-border-radius: 15px;
                -ms-border-radius: 15px;
                -o-border-radius: 15px;
              }
              .carme {
                content: '';
                position: absolute;
                height: 7px;
                width: 7px;
                top: -1px;
                left: calc(63% - 15px);
                background-color: #b3b0b0;
                border-radius: 50%;
                -webkit-border-radius: 50%;
                -moz-border-radius: 50%;
                -ms-border-radius: 50%;
                -o-border-radius: 50%;
                z-index: 10;
                display: none;
              }
            }
            .mobile_body_dark {
              border: 0.5rem solid #130e0e;
              border-radius: 32px;
              -webkit-border-radius: 32px;
              -moz-border-radius: 32px;
              -ms-border-radius: 32px;
              -o-border-radius: 32px;
              height: 100%;
              margin: auto;
              position: relative;
              position: relative;
              // screen and (max-width: 568px)
              // @include MediaQueries(Xxs) {}
              @include MediaQueries(Mobile) {
                &::after {
                  content: '📱 568';
                  position: absolute;
                  top: 0%;
                  left: 0px;
                  border-radius: 0.5rem;
                  z-index: 7;
                  font-size: 20px;
                  font-weight: bold;
                  background-color: #130e0e;
                  color: #fff;
                  padding: 10px 15px;
                }
              }
              // screen and (min-width: 569px) and (max-width: 767px)
              // @include MediaQueries(Xs) {}
              @include MediaQueries(Tablet) {
                &::after {
                  content: '📱 567 767';
                  position: absolute;
                  top: 0%;
                  left: 0px;
                  border-radius: 0.5rem;
                  z-index: 7;
                  font-size: 20px;
                  font-weight: bold;
                  background-color: #130e0e;
                  color: #fff;
                  padding: 10px 15px;
                }
              }
              // screen and (min-width: 768px) and (max-width: 991px)
              // @include MediaQueries(Md) {}
              @include MediaQueries(laptop) {
                &::after {
                  content: '💻 768 991';
                  position: absolute;
                  top: 0%;
                  left: 0px;
                  border-radius: 0.5rem;
                  z-index: 7;
                  font-size: 20px;
                  font-weight: bold;
                  background-color: #130e0e;
                  color: #fff;
                  padding: 10px 15px;
                }
              }
              // screen and (min-width: 992px) and (max-width: 1199px)
              // @include MediaQueries(Lg) {}
              @include MediaQueries(laptopLg) {
                &::after {
                  content: '💻➕ 992 1199';
                  position: absolute;
                  top: 0%;
                  left: 0px;
                  border-radius: 0.5rem;
                  z-index: 7;
                  font-size: 20px;
                  font-weight: bold;
                  background-color: #130e0e;
                  color: #fff;
                  padding: 10px 15px;
                }
              }
              // screen and (min-width: 1200px) and (max-width: 1399px)
              // @include MediaQueries(Xlg) {}
              @include MediaQueries(Desktop) {
                &::after {
                  content: '🖥️ 1200 1399';
                  position: absolute;
                  top: 0%;
                  left: 0px;
                  border-radius: 0.5rem;
                  z-index: 7;
                  font-size: 20px;
                  font-weight: bold;
                  background-color: #130e0e;
                  color: #fff;
                  padding: 10px 15px;
                  display: none;
                }
                width: 50%;
                overflow-x: hidden;
              }
              // screen and (min-width: 1400px)
              // @include MediaQueries(Xxlg) {}
              @include MediaQueries(DesktopLg) {
                &::after {
                  content: '🖥️➕ 1400';
                  position: absolute;
                  top: 0%;
                  left: 0px;
                  border-radius: 0.5rem;
                  z-index: 7;
                  font-size: 20px;
                  font-weight: bold;
                  background-color: #130e0e;
                  color: #fff;
                  padding: 10px 15px;
                  display: none;
                }
                width: 50%;
              }
              .mobile_content {
                position: relative;
                border-radius: 24px;
                -webkit-border-radius: 24px;
                -moz-border-radius: 24px;
                -ms-border-radius: 24px;
                -o-border-radius: 24px;
                border: 0.2rem solid #130e0e;
                height: 100%;
                background-color: #fff;
                padding: 1rem;
                display: flex;
                justify-content: space-between;
                align-items: center;
                form {
                  height: 100%;
                  display: flex;
                  justify-content: space-between;
                  align-items: center;
                  width: 100%;
                  .prime_card_form_signup {
                    border: none;
                    padding: 0;
                    margin: 0;
                    box-shadow: none;
                    height: 100%;
                    max-height: 100%;
                    overflow: hidden;
                    border-radius: 0px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    div.p-card-header {
                      height: 20%;
                      width: 100%;
                      display: flex;
                      align-items: center;
                      width: 100%;
                    }
                    div.p-card-body {
                      padding: 0;
                      margin: 0;
                      margin-bottom: 1rem;
                      height: 80%;
                      display: flex;
                      flex-direction: column;
                      div.p-card-content {
                        height: 80%;
                        .prime_card_form_signup_content {
                          > div {
                            display: flex;
                            flex-direction: column;
                            justify-content: space-between;
                            > div {
                              margin-top: 1rem;
                            }
                          }
                        }
                      }
                      div.p-card-footer {
                        height: 20%;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                      }
                    }
                  }
                  .prime_card_form_login {
                    border: none;
                    padding: 0;
                    margin: 0;
                    box-shadow: none;
                    height: 100%;
                    max-height: 100%;
                    overflow: hidden;
                    border-radius: 0px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    width: 100%;
                    div.p-card-header {
                      height: 20%;
                      width: 100%;
                      display: flex;
                      align-items: center;
                      width: 100%;
                    }
                    div.p-card-body {
                      padding: 0;
                      margin: 0;
                      margin-bottom: 1rem;
                      height: 80%;
                      display: flex;
                      flex-direction: column;
                      width: 100%;
                      div.p-card-content {
                        // height: 80%;
                        .input_email {
                          margin-bottom: 1rem;
                          input {
                            width: 100%;
                          }
                        }
                        .input_password {
                          margin-bottom: 1rem;
                          > div {
                            width: 100%;
                            input {
                              width: 100%;
                            }
                          }
                        }
                        .Forgotten_password {
                          margin-bottom: 1rem;
                        }
                      }
                      div.p-card-footer {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                      }
                    }
                  }
                }
              }
              .voice_up,
              .voice_down,
              .power {
                content: '';
                position: absolute;
                height: 70px;
                width: 13px;
                background-color: #130e0e;
                border-radius: 5px;
                z-index: 7;
                //rotate: 90deg;
                -webkit-border-radius: 5px;
                -moz-border-radius: 5px;
                -ms-border-radius: 5px;
                -o-border-radius: 5px;
              }
              .voice_up {
                top: 10%;
                left: -13px;
              }
              .voice_down {
                top: 24%;
                left: -13px;
              }
              .power {
                top: 17%;
                right: -13px;
              }
              .sonser,
              .voice {
                position: absolute;
                z-index: 7;
              }
              .sonser {
                height: 15px;
                background-color: #130e0e;
                width: 33.33%;
                left: 33.33%;
                border-radius: 0 0 15px 15px;
              }
              .voice {
                height: 5px;
                background-color: #b3b0b0;
                width: 15%;
                left: 42.5%;
                border-radius: 15px;
                -webkit-border-radius: 15px;
                -moz-border-radius: 15px;
                -ms-border-radius: 15px;
                -o-border-radius: 15px;
              }
              .carme {
                content: '';
                position: absolute;
                height: 7px;
                width: 7px;
                top: -1px;
                left: calc(63% - 15px);
                background-color: #b3b0b0;
                border-radius: 50%;
                -webkit-border-radius: 50%;
                -moz-border-radius: 50%;
                -ms-border-radius: 50%;
                -o-border-radius: 50%;
                z-index: 10;
                display: none;
              }
            }
          }
        }
      }
    }
  }
  </style>

```

### 📝 Page Profile

###### 📝 Create Page [ ProfileView.vue ] Inside [ Account ]

```
Account/ProfileView.vue
```

### 📝 Page Page Not Found

###### 📝 Page Page Not Found

```

```

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

## 🎓 course

### 🎓 Django course

```cmd
python manage.py startapp course
```

### ⚙️ Settings

#### ⚙️ Page Settings [ settings.py ] 📝

```python
INSTALLED_APPS = [
    # ...
    # Apps
    "course",
    # Libraries
    # ...
]
```

### 🎓 Course Page [ models.py ]

#### 🎓 App [ Course ] Page [ models.py ] 📝

```python

```

### 🎓 Course Page [ admin.py ]

#### 🎓 App [ Course ] Page [ admin.py ] 📝

```python

```

### 🎓 Course Page [ serializers.py ]

#### 🎓 App [ Course ] Page [ serializers.py ] 📝

```python
serializers.py
```

### 🎓 Course Page [ api.py ]

#### 🎓 App [ Course ] Page [ api.py ] 📝

```python
api.py
```

### 🎓 Course Page [ urls.py ]

#### 🎓 App [ Course ] Page [ urls.py ] 📝

```python
urls.py
```

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

---

## 🎓 course

### 🎓 Vue course

### 🎓 Course Page [ Courses.vue ]

#### 🎓 App [ Course ] Page [ Courses.vue ] 📝

```
CoursesView.vue
```

### 🎓 Course Page [ Course.vue ]

#### 🎓 App [ Course ] Page [ Course.vue ] 📝

```
CourseView.vue
```
