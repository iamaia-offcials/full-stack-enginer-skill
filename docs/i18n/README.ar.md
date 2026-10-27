# Full Stack Engineering Skill

[English](../../README.md) · [Русский](README.ru.md) · [Español](README.es.md) · [العربية](README.ar.md) · [Türkçe](README.tr.md) · [简体中文](README.zh-CN.md)

<div dir="rtl">

**معيار هندسي قابل للنقل لمساعدي الذكاء الاصطناعي: قواعد لاتخاذ القرارات، مع شروح وأمثلة لتخطيط البرمجيات وتطويرها وصيانتها.**

تعمل المهارة الأساسية `unified-development-standard` بشكل مستقل. تساعد الوكيل على فهم المنتج واختيار التقنيات المناسبة وتنفيذ العمل المطلوب مع الفحوص ذات الصلة. تعديل نص بسيط يجب ألا يتحول إلى تدقيق شامل.

## المجالات المشمولة

- رؤية المنتج، وقواعد العمل، والإصدار الأول/MVP، واختيار التقنيات وتقدير التعقيد.
- المعمارية، ومسؤولية منطق التطبيق، والخادم، وواجهات API والتكاملات.
- التحقق من المدخلات، والصلاحيات، والأسرار، وفرض ثوابت العمل في الجانب الموثوق.
- قيود قاعدة البيانات، والمعاملات، والفهارس، والترحيل والاستعادة.
- الواجهة الأمامية، وتنظيم الأنماط القابل للصيانة، وإمكانية الوصول والتصميم المتجاوب دون فرض هوية بصرية.
- حركة الواجهة: اختيار حسب السياق، وإيقاف الانتقال وعكسه، وتقليل الحركة، وبدائل وظيفية وتقدم يعكس الواقع.
- مراجع UX: ‏39 دراسة مصدرية و12 مقارنة لتركيب الصفحات و27 مثال حركة مع لوحات تسلسل وGIF، تُختار حسب المهمة ونموذج العمل الفعلي.
- تحسين محركات البحث التقني (SEO)، وتخطيط التحليلات ووحدات البكسل قبل ربط الخدمات.
- Git، وعمليات CI/CD المراعية للتكلفة، والحاويات عند الحاجة، والإصدارات والتشغيل.
- توثيق مستمر التحديث: تحديث مستند الميزة الحالي مع تمييز الخطط والسجل التاريخي.

نمط القرار: **الشرط ← القرار ← السبب ← المثال ← التحقق**. التحقق من صيغة البريد الإلكتروني، واستعلامات SQL ذات المعاملات، والعرض الآمن، والتحقق من الصلاحيات تعالج مشكلات مختلفة؛ ولا تستبدلها قائمة أحرف محظورة.

## السياق واللغة

جميع التعليمات المثبتة **بالإنجليزية**، لكن على الوكيل الرد بلغتك. يوجه ملف الدخول إلى الأقسام اللازمة، ولا يطلب قراءة المراجع الثلاثين كلها. تثبَّت المهارة الأساسية المستقلة افتراضيًا؛ أما ملفات التخصص الثمانية عشر فهي اختيارية. تبقى ترجمات README خارج المهارة المثبتة. تحتفظ صور الحركة بنصوصها الأصلية، مع شروح إنجليزية مرافقة.

يشرح [دليل المراجع](../../.agents/skills/unified-development-standard/guides/UX-REFERENCE-RESEARCH.md) الاختيار عبر CLI و[المعرض دون اتصال](../../.agents/skills/unified-development-standard/examples/reference-atlas.html). افتح HTML محليًا بعد الاستنساخ أو التنزيل؛ تعرض GitHub الشيفرة المصدرية. مخططات UX ليست لقطات للمواقع، وتواريخ المصدر لا تعني تحققًا جديدًا. عدّل JSON المعتمد ثم شغّل `scripts/reference_atlas.py --build-gallery` من مجلد المهارة الأساسية لإعادة توليد المعرض المشتق؛ يكشف `--check-gallery` عدم التطابق.

قد تستخدم الإنجليزية عددًا أقل من الرموز لدى بعض أدوات تقسيم النص، لكن الوفر يعتمد على النص والنموذج. القراءة الانتقائية وإزالة التكرار مهمتان أيضًا. تميز [نتائج المراجعة](../REVIEW.md) بين قياسات حجم النص وعدد الرموز وسلوك الوكيل أثناء التشغيل الفعلي.

## التثبيت السريع

يلزم **Python 3.10+** دون اعتماديات pip. استخدم `py` في Windows أو `python3` في Linux/macOS إذا كان هذا اسم المفسر لديك. يلزم Git للاستنساخ؛ ويمكن بدلًا منه تنزيل المستودع عبر **Code → Download ZIP** في GitHub ثم فك الضغط.

<div dir="ltr">

```bash
git clone https://github.com/iamaia-offcials/full-stack-enginer-skill.git
cd full-stack-enginer-skill
python tooling/install.py --agent codex --scope user
```

</div>

ينسخ المثبّت الملفات المحلية. لا ينزّل اعتماديات، ولا يصل إلى الحسابات، ولا يعدّل `AGENTS.md` أو `CLAUDE.md` أو `GEMINI.md`.

للتثبيت في مشروع موجود:

<div dir="ltr">

```bash
python tooling/install.py --agent codex --repo "/path/to/my-project" --dry-run
python tooling/install.py --agent codex --repo "/path/to/my-project"
```

</div>

مثال لمسار Windows: `"C:/dev/my-project"`. يجب ألا يتداخل المصدر والوجهة؛ لا تجعل مجلد هذه الحزمة نفسها وجهةً للتثبيت.

## التوافق مع الوكلاء

| الأداة | `--agent` | مجلد المشروع | مجلد المستخدم |
|---|---|---|---|
| Codex | `codex` | `.agents/skills/` | `~/.agents/skills/` |
| Claude Code | `claude` | `.claude/skills/` | `~/.claude/skills/` |
| Gemini CLI | `gemini` | `.gemini/skills/` | `~/.gemini/skills/` |
| Antigravity App / IDE | `antigravity` | `.agents/skills/` | `~/.gemini/config/skills/` |
| Antigravity CLI | `antigravity-cli` | `.agents/skills/` | `~/.gemini/antigravity-cli/skills/` |
| وكلاء متوافقون آخرون | `generic` أو `--target` | حسب الوكيل | حسب الوكيل |

اختر الأمر المناسب لأداتك:

<div dir="ltr">

```bash
python tooling/install.py --agent claude --scope user
python tooling/install.py --agent gemini --repo "/path/to/my-project"
python tooling/install.py --agent antigravity --scope user
python tooling/install.py --target "/path/to/another-agent/skills"
```

</div>

تجنب نسخًا مكررة في مجلدات يكتشفها الوكيل نفسه. يدعم Gemini أيضًا `.agents/skills`، لذا قد يكون تثبيت Codex المشترك ظاهرًا له بالفعل. تحقق من قائمة المهارات ثم اطلب صراحةً استخدام `unified-development-standard`. حدّث القائمة أو ابدأ جلسة جديدة عند الحاجة. نسخ الملفات والتأكد من استخدام النموذج لها فحصان منفصلان.

جرت مطابقة المسارات مع الوثائق الرسمية بتاريخ 2026-10-27: [Codex](https://learn.chatgpt.com/docs/build-skills)، و[Claude Code](https://code.claude.com/docs/en/skills)، و[Gemini CLI](https://geminicli.com/docs/cli/skills/)، و[Antigravity](https://antigravity.google/docs/skills). قد تتغير الواجهات؛ ولا ندّعي إجراء تشغيل فعلي على كل منصة.

### Lovable والواجهات السحابية

في Lovable، افتح **Workspace settings → Skills → Add → Import from GitHub** ثم اختر [مجلد المهارة الأساسية](https://github.com/iamaia-offcials/full-stack-enginer-skill/tree/main/.agents/skills/unified-development-standard). تتطلب العملية صلاحيات مالك مساحة العمل أو مسؤولها وفقًا لـ[وثائق Lovable](https://docs.lovable.dev/features/skills). والبديل هو **Upload ZIP**.

لإنشاء الأرشيف القابل للنقل:

<div dir="ltr">

```bash
python tooling/package.py
```

</div>

الناتج `dist/unified-development-standard.zip` ويحتوي على ملف الدخول والمراجع والأدلة والأمثلة والترخيص. استورد الحزمة كاملة؛ لا يكفي `SKILL.md` وحده. التثبيت في Claude Code لا يثبّت المهارة في حساب Claude السحابي؛ استخدم الاستيراد الذي يدعمه الحساب. لا يدير المثبّت الحسابات السحابية.

إذا كان الوكيل يصل إلى الملفات لكنه لا يدعم المهارات مباشرة، فاطلب قراءة `SKILL.md` الأساسي والأقسام المرتبطة ذات الصلة. دون ملفات أو استيراد، تُقدَّم التعليمات داخل المحادثة؛ وهذا ليس تثبيتًا تلقائيًا. يعتمد التوافق على البيئة لا على اسم النموذج وحده.

## اطلب من الذكاء الاصطناعي التثبيت

أرسل الطلب التالي إلى وكيل يملك الوصول إلى الطرفية والملفات:

> ثبّت المهارة الهندسية من https://github.com/iamaia-offcials/full-stack-enginer-skill.git. اقرأ README والمثبّت. اختر مجلد المهارات المناسب لهذه الأداة ونطاق التثبيت المطلوب؛ وإن لم يُحدَّد النطاق فاستخدم المشروع الحالي. نفّذ dry-run ثم ثبّت دون تعديل ملفات تعليمات المشروع الموجودة أو الكتابة فوق التعديلات المحلية. تحقق من SKILL.md المثبت والمراجع، وأبلغ بشكل منفصل عمّا إذا كان الوكيل يكتشف المهارة. إذا تعذر التثبيت عبر نظام الملفات، فاستخدم الاستيراد الموثق أو اشرح القيد المحدد.

للواجهات السحابية، استخدم استيراد GitHub/ZIP أعلاه. وجود محادثة لا يعني توفر طرفية Python.

## ملفات التخصص الاختيارية

تغطي المهارة الأساسية جميع المجالات. ثبّت ملفات التخصص فقط إذا كانت إجراءات العمل المتخصصة المنفصلة مفيدة. يضمّن المثبّت المهارة الأساسية دائمًا لأنها اعتماد مطلوب.

<div dir="ltr">

```bash
python tooling/install.py --list
python tooling/install.py --agent codex --scope user --skills uds-security,uds-backend
python tooling/install.py --agent codex --scope user --skills all
```

</div>

التخصصات: `uds-product-discovery`، `uds-requirements-planning`، `uds-architecture`، `uds-design-system`، `uds-frontend`، `uds-web-development`، `uds-technical-seo`، `uds-backend`، `uds-data`، `uds-mobile-development`، `uds-performance-optimization`، `uds-dependency-upgrades`، `uds-code-review`، `uds-testing`، `uds-security`، `uds-git-cicd`، `uds-operations`، `uds-project-audit`.

## أمثلة الاستخدام

> استخدم unified-development-standard. خطط لبوابة عملاء: حدّد رؤية المنتج وقواعد العمل ونطاق الإصدار الأول، وقيّم الحاجة المستقبلية إلى فرق الموظفين والمدفوعات، واختر التقنيات. اشرح الأسس المبررة الآن والأعمال التي يمكن تأجيلها.

> استخدم unified-development-standard. أضف حقل بريد إلكتروني إلى نظام CRM الحالي. أعد استخدام المكوّن والعقد الموجودين، وتحقق من التحقق على الخادم والصلاحيات، وحدّث التوثيق الحالي للميزة ونفّذ الفحوص ذات الصلة.

## التحديث والاستعادة والإزالة

في نسختك المحلية من المستودع، اجلب التغييرات وأعد التثبيت مع الوكيل والنطاق واختيار المهارات نفسها:

<div dir="ltr">

```bash
git pull --ff-only
python tooling/install.py --agent codex --scope user --update --dry-run
python tooling/install.py --agent codex --scope user --update
```

</div>

إذا ثبّتَّ تخصصات، فأدرج اختيار `--skills` نفسه عند التحديث. يسجل المثبّت بصمات الملفات ويتوقف عند وجود تعديلات محلية أو ملفات مضافة. احفظ هذه التغييرات ووفّق بينها وبين الإصدار الجديد قبل التحديث. لاعتماد تثبيت قديم دون ملف بيان، راجع ملفاته أولًا ثم استخدم صراحةً:

<div dir="ltr">

```bash
python tooling/install.py --agent codex --scope user --update --adopt-existing --dry-run
python tooling/install.py --agent codex --scope user --update --adopt-existing
```

</div>

يستبدل `--adopt-existing` مجلدات المهارات المتطابقة في الاسم ويحفظ الملفات السابقة في `.uds-backups/` بجوار `skills/`. لا يتجاوز حماية التثبيتات المُدارة ذات التعديلات المحلية. تؤدي أخطاء الاستبدال العادية إلى التراجع؛ بعد انقطاع العملية أو الكهرباء استعد من النسخة الاحتياطية. قبل الاستعادة اليدوية احفظ المجلد الحالي ثم أعد النسخة المطلوبة باسم المهارة الأصلي.

للإزالة احذف فقط مجلد المهارة المثبتة المختارة. إزالة المهارة الأساسية تعطل التخصصات التي تعتمد عليها. تُزال المهارات السحابية من إعدادات منصاتها. لا تحذف مهارات غير مرتبطة.

يرفض المثبّت عمدًا الروابط الرمزية ونقاط junction ومسارات reparse. إذا ترك عطلٌ `.uds-install.lock`، فتأكد أولًا من عدم تشغيل مثبّت آخر، ثم أزل ملف القفل وحده.

## المستودع والتحقق

<div dir="ltr">

```text
README.md                       الوصف الإنجليزي الأساسي والتثبيت
LICENSE                         MIT
.agents/skills/
  unified-development-standard/ المهارة الأساسية والقواعد والأدلة والقوالب والأمثلة
  uds-*/SKILL.md                 إجراءات التخصصات الاختيارية
docs/i18n/                      ترجمات README العام
docs/REVIEW.md                   أدلة المراجعة الحالية وحدودها
tooling/                        التثبيت والتغليف والتحقق والتقييم
tests/                          اختبارات انحدار نظام الملفات والحزمة
```

```bash
python tooling/validate_suite.py
python -m unittest discover -s tests -v
python tooling/package.py
```

</div>

تغطي الفحوص البيانات الوصفية والروابط المحلية ومعرّفات القواعد والتثبيت وحماية التحديث وقابلية نقل الأرشيف. ولا تثبت صحة السلوك لدى كل وكيل أو أمان تطبيق معين. راجع [المراجعة](../REVIEW.md) و[دليل تقييم السلوك](../../tooling/EVALUATION_GUIDE.md).

للمساهمة: عدّل القاعدة المعتمدة مع الحفاظ على معرّفها، وأضف شرحًا وأمثلة مفيدة وسيناريو قابلًا للتكرار عند تغيير السلوك. حدّث الوثائق الموجودة في مكانها. حافظ على توافق ترجمات README مع الإنجليزية؛ لا تترجم المهارة المثبتة أو تكررها لكل لغة.

## الترخيص والحدود

[MIT](../../LICENSE). تحتفظ وثائق الجهات الخارجية بشروطها الخاصة. الإشارة إلى المعايير أو الشركات لا تعني اعتمادًا أو تأييدًا.

لا تضمن المهارة أمان التطبيق أو ترتيب البحث أو الامتثال القانوني أو عدم الحاجة إلى ترحيل مستقبلي. تتطلب هذه النتائج تحققًا خاصًا بكل مشروع. ولا تمنح أدوات أو حسابات أو إذنًا للنشر أو إدارة أنظمة الإنتاج.

</div>

