<template><div><h1 id="django-page-api" tabindex="-1"><a class="header-anchor" href="#django-page-api"><span>Django Page Api</span></a></h1>
<div dir="rtl" style="font-size:1.2vw; padding: 1rem 0; font-weight: 900;">
  إنشاء العناصر المراية و طريقة العرض و الفلاتر
</div>
<h2 id="all" tabindex="-1"><a class="header-anchor" href="#all"><span>All</span></a></h2>
<div style="font-size:1.2vw; padding: 2rem 0 0 0; font-weight: 900;">
</div>
<div dir="rtl" style="font-size:1.2vw; padding: 1rem 0; font-weight: 900;">
</div>
<div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token decorator annotation punctuation">@api_view</span><span class="token punctuation">(</span><span class="token punctuation">[</span><span class="token string">"GET"</span><span class="token punctuation">]</span><span class="token punctuation">)</span></span>
<span class="line"><span class="token decorator annotation punctuation">@authentication_classes</span><span class="token punctuation">(</span><span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">)</span>  <span class="token comment"># 🔓 عدم استخدام مصادقة</span></span>
<span class="line"><span class="token decorator annotation punctuation">@permission_classes</span><span class="token punctuation">(</span><span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">)</span>  <span class="token comment"># 🔓 عدم استخدام تصاريح</span></span>
<span class="line"><span class="token keyword">def</span> <span class="token function">categories_list</span><span class="token punctuation">(</span>request<span class="token punctuation">)</span><span class="token punctuation">:</span>  <span class="token comment"># 🏷️ دالة لجلب جميع الفئات</span></span>
<span class="line">    categories <span class="token operator">=</span> Category<span class="token punctuation">.</span>objects<span class="token punctuation">.</span><span class="token builtin">all</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token comment"># 📚 جلب كل الفئات</span></span>
<span class="line">    serializer <span class="token operator">=</span> CategorySerializer<span class="token punctuation">(</span>categories<span class="token punctuation">,</span> many<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">)</span></span>
<span class="line">    <span class="token keyword">return</span> Response<span class="token punctuation">(</span>serializer<span class="token punctuation">.</span>data<span class="token punctuation">)</span></span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token decorator annotation punctuation">@api_view</span><span class="token punctuation">(</span><span class="token punctuation">[</span><span class="token string">"GET"</span><span class="token punctuation">]</span><span class="token punctuation">)</span></span>
<span class="line"><span class="token decorator annotation punctuation">@authentication_classes</span><span class="token punctuation">(</span><span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">)</span>  <span class="token comment"># 🔓 عدم استخدام مصادقة</span></span>
<span class="line"><span class="token decorator annotation punctuation">@permission_classes</span><span class="token punctuation">(</span><span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">)</span>  <span class="token comment"># 🔓 عدم استخدام تصاريح</span></span>
<span class="line"><span class="token keyword">def</span> <span class="token function">courses_list</span><span class="token punctuation">(</span>request<span class="token punctuation">)</span><span class="token punctuation">:</span> <span class="token comment"># 🏷️ دالة لجلب جميع الكرسات</span></span>
<span class="line">    courses <span class="token operator">=</span> Course<span class="token punctuation">.</span>objects<span class="token punctuation">.</span><span class="token builtin">all</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token comment"># 📚 جلب كل الكرسات</span></span>
<span class="line">    serializer <span class="token operator">=</span> CourseListSerializer<span class="token punctuation">(</span>courses<span class="token punctuation">,</span> many<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">)</span></span>
<span class="line">    <span class="token keyword">return</span> JsonResponse<span class="token punctuation">(</span>serializer<span class="token punctuation">.</span>data<span class="token punctuation">,</span> safe<span class="token operator">=</span><span class="token boolean">False</span><span class="token punctuation">)</span></span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h2 id="single" tabindex="-1"><a class="header-anchor" href="#single"><span>Single</span></a></h2>
<div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token comment"># 🧐 Django كائن يُستخدم لبناء استعلامات معقدة في</span></span>
<span class="line"><span class="token keyword">from</span> django<span class="token punctuation">.</span>db<span class="token punctuation">.</span>models <span class="token keyword">import</span> Q</span>
<span class="line"></span>
<span class="line"><span class="token comment"># 📚 دالة لجلب بيانات دورة معينة باستخدام المعرف (pk)</span></span>
<span class="line"><span class="token decorator annotation punctuation">@api_view</span><span class="token punctuation">(</span><span class="token punctuation">[</span><span class="token string">"GET"</span><span class="token punctuation">]</span><span class="token punctuation">)</span></span>
<span class="line"><span class="token keyword">def</span> <span class="token function">course_detail</span><span class="token punctuation">(</span>request<span class="token punctuation">,</span> pk<span class="token punctuation">)</span><span class="token punctuation">:</span></span>
<span class="line">    user_ids <span class="token operator">=</span> <span class="token punctuation">[</span>request<span class="token punctuation">.</span>user<span class="token punctuation">.</span><span class="token builtin">id</span><span class="token punctuation">]</span></span>
<span class="line"></span>
<span class="line">    <span class="token keyword">for</span> user <span class="token keyword">in</span> request<span class="token punctuation">.</span>user<span class="token punctuation">.</span>friends<span class="token punctuation">.</span><span class="token builtin">all</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span></span>
<span class="line">        user_ids<span class="token punctuation">.</span>append<span class="token punctuation">(</span>user<span class="token punctuation">.</span><span class="token builtin">id</span><span class="token punctuation">)</span></span>
<span class="line"></span>
<span class="line">    <span class="token comment"># 📦 جلب الدورة إذا كان منشؤها موجودًا ضمن معرفات المستخدمين</span></span>
<span class="line">    <span class="token comment"># 🔍 البحث عن الدورة المحددة باستخدام شرط أن تكون منشأة بواسطة المستخدم أو أصدقائه.</span></span>
<span class="line">    course <span class="token operator">=</span> Course<span class="token punctuation">.</span>objects<span class="token punctuation">.</span><span class="token builtin">filter</span><span class="token punctuation">(</span>Q<span class="token punctuation">(</span>created_by_id__in<span class="token operator">=</span><span class="token builtin">list</span><span class="token punctuation">(</span>user_ids<span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">.</span>get<span class="token punctuation">(</span>pk<span class="token operator">=</span>pk<span class="token punctuation">)</span></span>
<span class="line"></span>
<span class="line">    <span class="token comment"># 🎨 تحويل بيانات الدورة إلى JSON باستخدام الـ Serializer</span></span>
<span class="line">    course_serializer <span class="token operator">=</span> CourseDetailSerializer<span class="token punctuation">(</span>course<span class="token punctuation">)</span></span>
<span class="line">    course_data <span class="token operator">=</span> course_serializer<span class="token punctuation">.</span>data</span>
<span class="line"></span>
<span class="line">    <span class="token comment"># 🔐 التحقق من إذا كان المستخدم مصرحًا له</span></span>
<span class="line">    <span class="token comment"># 🔐 التحقق من إذا كان المستخدم قد سجل الدخول</span></span>
<span class="line">    <span class="token keyword">if</span> request<span class="token punctuation">.</span>user<span class="token punctuation">.</span>is_authenticated<span class="token punctuation">:</span></span>
<span class="line">        <span class="token comment"># ✅ إذا كان مصرحًا له، يتم استخدام بيانات الدورة كما هي</span></span>
<span class="line">        course_data <span class="token operator">=</span> course_serializer<span class="token punctuation">.</span>data</span>
<span class="line">    <span class="token keyword">else</span><span class="token punctuation">:</span></span>
<span class="line">        <span class="token comment"># 🚫 إذا لم يكن مصرحًا له، تكون بيانات الدورة فارغة</span></span>
<span class="line">        course_data <span class="token operator">=</span> <span class="token punctuation">{</span><span class="token punctuation">}</span></span>
<span class="line"></span>
<span class="line">    <span class="token comment"># 📚 جلب جميع الدروس المرتبطة بالدورة</span></span>
<span class="line">    lesson <span class="token operator">=</span> course<span class="token punctuation">.</span>lessons<span class="token punctuation">.</span><span class="token builtin">all</span><span class="token punctuation">(</span><span class="token punctuation">)</span></span>
<span class="line">    <span class="token comment"># 🎨 تحويل بيانات الدروس إلى JSON باستخدام الـ Serializer</span></span>
<span class="line">    lesson_serializer <span class="token operator">=</span> LessonListSerializer<span class="token punctuation">(</span>lesson<span class="token punctuation">,</span> many<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">)</span></span>
<span class="line">    lesson_data <span class="token operator">=</span> lesson_serializer<span class="token punctuation">.</span>data</span>
<span class="line"></span>
<span class="line">    <span class="token comment"># 📝 إرجاع بيانات الدورة والدروس في صيغة JSON</span></span>
<span class="line">    <span class="token keyword">return</span> JsonResponse<span class="token punctuation">(</span></span>
<span class="line">        <span class="token punctuation">{</span></span>
<span class="line">            <span class="token string">"course"</span><span class="token punctuation">:</span> course_data<span class="token punctuation">,</span>  <span class="token comment"># 📝 بيانات الدورة</span></span>
<span class="line">            <span class="token string">"lessons"</span><span class="token punctuation">:</span> lesson_data<span class="token punctuation">,</span>  <span class="token comment"># 📚 بيانات الدروس</span></span>
<span class="line">        <span class="token punctuation">}</span></span>
<span class="line">    <span class="token punctuation">)</span></span>
<span class="line"></span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div></div></template>


