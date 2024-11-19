<template><div><h2 id="models-إنشاء-قاعدة-البيانات" tabindex="-1"><a class="header-anchor" href="#models-إنشاء-قاعدة-البيانات"><span>Models =&gt; إنشاء قاعدة البيانات</span></a></h2>
<h3 id="uuidfield-id" tabindex="-1"><a class="header-anchor" href="#uuidfield-id"><span>UUIDField [ id ]</span></a></h3>
<div style="font-size:1.2vw; padding: 2rem 0 0 0; font-weight: 900;">
  📝 UUIDField()
</div>
<div dir="rtl" style="font-size:1.2vw; padding: 1rem 0; font-weight: 900;">
  id مُفتاح أساسي يستخدم كمُعرّف فريد لكل نموذج ويتم إنشاؤه بشكل تلقائي باستخدام
  uuid.uuid4.
</div>
<div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token keyword">import</span> uuid</span>
<span class="line"></span>
<span class="line"><span class="token comment"># 🧑 Custom User Form  نموذج المستخدم المخصص</span></span>
<span class="line"><span class="token keyword">class</span> <span class="token class-name">User</span><span class="token punctuation">(</span>AbstractBaseUser<span class="token punctuation">,</span> PermissionsMixin<span class="token punctuation">)</span><span class="token punctuation">:</span></span>
<span class="line">    <span class="token comment"># ___________________</span></span>
<span class="line">    <span class="token comment"># حقل يتم تعبئة تلقائي</span></span>
<span class="line">    <span class="token comment"># ___________________</span></span>
<span class="line">    <span class="token comment"># id مُفتاح أساسي يستخدم كمُعرّف فريد لكل نموذج ويتم إنشاؤه بشكل تلقائي باستخدام</span></span>
<span class="line">    <span class="token comment"># uuid.uuid4.</span></span>
<span class="line">    <span class="token builtin">id</span> <span class="token operator">=</span> models<span class="token punctuation">.</span>UUIDField<span class="token punctuation">(</span>primary_key<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">,</span> default<span class="token operator">=</span>uuid<span class="token punctuation">.</span>uuid4<span class="token punctuation">,</span> editable<span class="token operator">=</span><span class="token boolean">False</span><span class="token punctuation">)</span></span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="" tabindex="-1"><a class="header-anchor" href="#"><span>__</span></a></h3>
<h3 id="charfield-text" tabindex="-1"><a class="header-anchor" href="#charfield-text"><span>CharField [ Text ]</span></a></h3>
<div style="font-size: 2vw; padding: 2rem 0 0 0; font-weight: 900;">
  📝 CharField()
</div>
<div dir="rtl" style="font-size:1.5vw; padding: 0 0 1rem 0; ">
  <br>
  🌾 حقل النص يُستخدم لتخزين النصوص
  <br>
  <br>
  [ max_length=255 ]
  <br>
  ⚙️ يمكن للخيار تحديد الحد الأقصى لعدد الأحرف في النص بحد أقصى 255 حرفًا
  <br>
<hr>
<p>📝 [ null=False | null=True ]
<br>
أو لا(None) يحدد الحقل ما إذا كان يمكن أن يأخذ قيمة فارغة
<br>
📌 False القيمة الافتراضية هي
<br>
💭 يعني ذلك أن الحقل لا يمكن أن يكون فارغًا
<br>
🌟 True الحقل يمكن أن يكون فارغًا
<br>
👍 بمعنى أنه لا يحتوي على أي محتوى
<br></p>
<hr>
<p>📝 [ blank=False | blank=True ]
<br>
✔️ يحدد ما إذا كان يمكن ترك الحقل فارغًا عند إنشاء نموذج.
<br>
❌ False القيمة الافتراضية هي
<br>
💭 True مما يعني أنه يجب توفير قيمة لهذا الحقل
<br></p>
<hr>
<p>[ ... | default=&quot;Name&quot; | default=5 ]
<br>
⚙️ يحدد القيمة الافتراضية للحقل عندما لا يتم تقديم قيمة له
<br>
⚙️ في هذه الحالة، ليس هناك قيمة افتراضية محددة
<br>
📌 في هذه الحالة، القيمة الافتراضية هي &quot;اسم المنتج&quot;
<br>
🌟 يمكن أن يكون هناك قيمة افتراضية محددة مثل الارقام
<br></p>
<hr>
<p>[ verbose_name=&quot;Name&quot; ]
<br>
🏷️ يحدد الاسم الذي سيظهر في واجهة المستخدم كعنوان للحقل
<br>
🤔 يساعد في فهم المستخدم لغرض الحقل
<br></p>
<hr>
<p>[ help_text=&quot;Name&quot; ]
<br>
🔍 يوفر نص توضيحي للمستخدمين بجانب الحقل
💡 يساعد في ملء الحقل بشكل صحيح</p>
</div>
<div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token comment"># 🧑 Custom User Form  نموذج المستخدم المخصص</span></span>
<span class="line"><span class="token keyword">class</span> <span class="token class-name">User</span><span class="token punctuation">(</span>AbstractBaseUser<span class="token punctuation">,</span> PermissionsMixin<span class="token punctuation">)</span><span class="token punctuation">:</span></span>
<span class="line">    <span class="token comment"># ___________________</span></span>
<span class="line">    <span class="token comment"># حقل يتم تعبئة من المستخدام</span></span>
<span class="line">    <span class="token comment"># ___________________</span></span>
<span class="line">    name <span class="token operator">=</span> models<span class="token punctuation">.</span>CharField<span class="token punctuation">(</span>max_length<span class="token operator">=</span><span class="token number">255</span><span class="token punctuation">)</span></span>
<span class="line">    name <span class="token operator">=</span> models<span class="token punctuation">.</span>CharField<span class="token punctuation">(</span>max_length<span class="token operator">=</span><span class="token number">255</span><span class="token punctuation">,</span> null<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">,</span> blank<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">,</span> default<span class="token operator">=</span><span class="token string">"Name"</span><span class="token punctuation">,</span></span>
<span class="line">        verbose_name<span class="token operator">=</span><span class="token string">"Name"</span><span class="token punctuation">,</span> help_text<span class="token operator">=</span><span class="token string">"Please Enter The Your Name Here"</span><span class="token punctuation">,</span></span>
<span class="line">        choices<span class="token operator">=</span><span class="token punctuation">[</span> <span class="token punctuation">(</span><span class="token string">"available"</span><span class="token punctuation">,</span> <span class="token string">"موجود"</span><span class="token punctuation">)</span><span class="token punctuation">,</span> <span class="token punctuation">(</span><span class="token string">"sold_out"</span><span class="token punctuation">,</span> <span class="token string">"خلص"</span><span class="token punctuation">)</span><span class="token punctuation">,</span> <span class="token punctuation">(</span><span class="token string">"reserved"</span><span class="token punctuation">,</span> <span class="token string">"محجوز"</span><span class="token punctuation">)</span><span class="token punctuation">,</span><span class="token punctuation">]</span><span class="token punctuation">,</span><span class="token punctuation">)</span></span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="-1" tabindex="-1"><a class="header-anchor" href="#-1"><span>___</span></a></h3>
<h3 id="textfield-text" tabindex="-1"><a class="header-anchor" href="#textfield-text"><span>TextField [ Text ]</span></a></h3>
<div style="font-size:1.5vw; padding: 2rem 0 0 0; font-weight: 900;">
  📝 TextField()
</div>
<div dir="rtl" style="font-size:1.5vw; padding: 0 0 1rem 0; ">
  <br>
  🌾 حقل النص يُستخدم لتخزين النصوص الطويله
  <br>
  <br>
  ---
  [ max_length=255 ]
  <br>
  ⚙️ يمكن للخيار تحديد الحد الأقصى لعدد الأحرف في النص بحد أقصى 255 حرفًا
  <br>
  ---
<p>📝 [ null=False | null=True ]
<br>
أو لا(None) يحدد الحقل ما إذا كان يمكن أن يأخذ قيمة فارغة
<br>
📌 False القيمة الافتراضية هي
<br>
💭 يعني ذلك أن الحقل لا يمكن أن يكون فارغًا
<br>
🌟 True الحقل يمكن أن يكون فارغًا
<br>
👍 بمعنى أنه لا يحتوي على أي محتوى
<br></p>
<hr>
<p>📝 [ blank=False | blank=True ]
<br>
✔️ يحدد ما إذا كان يمكن ترك الحقل فارغًا عند إنشاء نموذج.
<br>
❌ False القيمة الافتراضية هي
<br>
💭 True مما يعني أنه يجب توفير قيمة لهذا الحقل
<br></p>
<hr>
<p>[ ... | default=&quot;Name&quot; | default=5 ]
<br>
⚙️ يحدد القيمة الافتراضية للحقل عندما لا يتم تقديم قيمة له
<br>
⚙️ في هذه الحالة، ليس هناك قيمة افتراضية محددة
<br>
📌 في هذه الحالة، القيمة الافتراضية هي &quot;اسم المنتج&quot;
<br>
🌟 يمكن أن يكون هناك قيمة افتراضية محددة مثل الارقام
<br></p>
<hr>
<p>[ verbose_name=&quot;Name&quot; ]
<br>
🏷️ يحدد الاسم الذي سيظهر في واجهة المستخدم كعنوان للحقل
<br>
🤔 يساعد في فهم المستخدم لغرض الحقل
<br></p>
<hr>
<p>[ help_text=&quot;Name&quot; ]
<br>
🔍 يوفر نص توضيحي للمستخدمين بجانب الحقل
💡 يساعد في ملء الحقل بشكل صحيح</p>
</div>
<div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token comment"># 🧑 Custom User Form  نموذج المستخدم المخصص</span></span>
<span class="line"><span class="token keyword">class</span> <span class="token class-name">User</span><span class="token punctuation">(</span>AbstractBaseUser<span class="token punctuation">,</span> PermissionsMixin<span class="token punctuation">)</span><span class="token punctuation">:</span></span>
<span class="line">    <span class="token comment"># ___________________</span></span>
<span class="line">    <span class="token comment"># حقل يتم تعبئة من المستخدام</span></span>
<span class="line">    <span class="token comment"># ___________________</span></span>
<span class="line">    long_description <span class="token operator">=</span> models<span class="token punctuation">.</span>TextField<span class="token punctuation">(</span>null<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">,</span> blank<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">)</span></span>
<span class="line">    long_description <span class="token operator">=</span> models<span class="token punctuation">.</span>TextField<span class="token punctuation">(</span>max_length<span class="token operator">=</span><span class="token number">255</span><span class="token punctuation">,</span> null<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">,</span> blank<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">,</span> default<span class="token operator">=</span><span class="token string">"Name"</span><span class="token punctuation">,</span></span>
<span class="line">        verbose_name<span class="token operator">=</span><span class="token string">"Name"</span><span class="token punctuation">,</span> help_text<span class="token operator">=</span><span class="token string">"Please Enter The Your Name Here"</span><span class="token punctuation">,</span></span>
<span class="line">        choices<span class="token operator">=</span><span class="token punctuation">[</span> <span class="token punctuation">(</span><span class="token string">"available"</span><span class="token punctuation">,</span> <span class="token string">"موجود"</span><span class="token punctuation">)</span><span class="token punctuation">,</span> <span class="token punctuation">(</span><span class="token string">"sold_out"</span><span class="token punctuation">,</span> <span class="token string">"خلص"</span><span class="token punctuation">)</span><span class="token punctuation">,</span> <span class="token punctuation">(</span><span class="token string">"reserved"</span><span class="token punctuation">,</span> <span class="token string">"محجوز"</span><span class="token punctuation">)</span><span class="token punctuation">,</span><span class="token punctuation">]</span><span class="token punctuation">,</span><span class="token punctuation">)</span></span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h3 id="-2" tabindex="-1"><a class="header-anchor" href="#-2"><span>__</span></a></h3>
<h3 id="all" tabindex="-1"><a class="header-anchor" href="#all"><span>All</span></a></h3>
<div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token keyword">class</span> <span class="token class-name">User</span><span class="token punctuation">(</span>models<span class="token punctuation">.</span>Model<span class="token punctuation">)</span><span class="token punctuation">:</span></span>
<span class="line">    <span class="token comment"># ___________________</span></span>
<span class="line">    <span class="token comment"># حقل يتم تعبئة تلقائي</span></span>
<span class="line">    <span class="token comment"># ___________________</span></span>
<span class="line">    <span class="token builtin">id</span> <span class="token operator">=</span> models<span class="token punctuation">.</span>UUIDField<span class="token punctuation">(</span>primary_key<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">,</span> default<span class="token operator">=</span>uuid<span class="token punctuation">.</span>uuid4<span class="token punctuation">,</span> editable<span class="token operator">=</span><span class="token boolean">False</span><span class="token punctuation">)</span></span>
<span class="line"></span>
<span class="line">    <span class="token comment"># ___________________</span></span>
<span class="line">    <span class="token comment"># حقل يتم تعبئة من المستخدام</span></span>
<span class="line">    <span class="token comment"># ___________________</span></span>
<span class="line">    name <span class="token operator">=</span> models<span class="token punctuation">.</span>CharField<span class="token punctuation">(</span>max_length<span class="token operator">=</span><span class="token number">255</span><span class="token punctuation">)</span></span>
<span class="line">    long_description <span class="token operator">=</span> models<span class="token punctuation">.</span>TextField<span class="token punctuation">(</span>null<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">,</span> blank<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">)</span></span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div></div></template>


