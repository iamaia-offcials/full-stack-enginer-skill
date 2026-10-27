# Full Stack Engineering Skill

[English](../../README.md) · [Русский](README.ru.md) · [Español](README.es.md) · [العربية](README.ar.md) · [Türkçe](README.tr.md) · [简体中文](README.zh-CN.md)

**Yapay zekâ asistanları için taşınabilir bir mühendislik standardı: yazılım planlama, geliştirme ve bakımına yönelik karar kuralları, açıklamalar ve örnekler.**

Ana beceri `unified-development-standard` tek başına çalışır. Ajanın ürünü anlamasına, uygun teknoloji yığınını seçmesine ve istenen kapsamı ilgili kontrollerle uygulamasına yardımcı olur. Küçük bir metin düzeltmesi kapsamlı bir denetime dönüşmemelidir.

## Kapsam

- Ürün vizyonu, iş kuralları, ilk sürüm/MVP, teknoloji seçimi ve karmaşıklık değerlendirmesi.
- Mimari, mantığın hangi modüle ait olduğu, backend, API'ler ve entegrasyonlar.
- Doğrulama, yetkilendirme, gizli bilgiler ve iş kurallarının güvenilir tarafta uygulanması.
- Veritabanı kısıtları, işlemler, indeksler, şema geçişleri ve kurtarma.
- Marka stilini dayatmadan frontend, sürdürülebilir stil yapısı, erişilebilirlik ve duyarlı arayüzler.
- Hizmetleri bağlamadan önce teknik SEO ile analitik ve piksel planlaması.
- Git, maliyeti gözeten CI/CD, gerektiğinde konteynerler, sürüm çıkarma ve işletim.
- Güncel dokümantasyon: mevcut özellik belgesini güncelleme; planları ve geçmişi ayırma.

Karar düzeni: **koşul → karar → gerekçe → örnek → doğrulama**. E-posta biçim doğrulaması, parametreli SQL, güvenli görüntüleme ve yetkilendirme farklı sorunları çözer; yasaklı karakter listesi bunların yerini tutmaz.

## Bağlam ve dil

Kurulan tüm talimatlar **İngilizcedir**. Ajan yine de sizin dilinizde yanıt vermelidir. Giriş dosyası ilgili bölümlere yönlendirir; 28 başvuru dosyasının tamamını okumayı gerektirmez. Varsayılan olarak tek ve bağımsız bir çekirdek kurulur; 18 uzmanlık profili isteğe bağlıdır. README çevirileri kurulan becerinin dışında kalır.

İngilizce bazı belirteçleyicilerde daha az token kullanabilir; ancak tasarruf metne ve modele bağlıdır. Seçici okuma ve tekrarları kaldırma da önemlidir. [İnceleme sonuçları](../REVIEW.md), ölçülen metin boyutlarını ve token sayılarını gerçek çalışma davranışından ayırır.

## Hızlı kurulum

**Python 3.10+** gerekir; pip bağımlılığı yoktur. Sisteminizdeki komut buysa Windows'ta `py`, Linux/macOS'ta `python3` kullanın. Klonlamak için Git gerekir; alternatif olarak GitHub'da **Code → Download ZIP** ile indirip arşivi açabilirsiniz.

```bash
git clone https://github.com/iamaia-offcials/full-stack-enginer-skill.git
cd full-stack-enginer-skill
python tooling/install.py --agent codex --scope user
```

Kurucu yerel dosyaları kopyalar. Bağımlılık indirmez, hesaplara erişmez ve `AGENTS.md`, `CLAUDE.md` veya `GEMINI.md` dosyalarını değiştirmez.

Mevcut bir projeye kurmak için:

```bash
python tooling/install.py --agent codex --repo "/path/to/my-project" --dry-run
python tooling/install.py --agent codex --repo "/path/to/my-project"
```

Windows'ta `"C:/dev/my-project"` gibi bir yol kullanabilirsiniz. Kaynak ve hedef çakışmamalıdır; bu paketin kendi dizinini hedeflemeyin.

## Ajan uyumluluğu

| Araç | `--agent` | Proje dizini | Kullanıcı dizini |
|---|---|---|---|
| Codex | `codex` | `.agents/skills/` | `~/.agents/skills/` |
| Claude Code | `claude` | `.claude/skills/` | `~/.claude/skills/` |
| Gemini CLI | `gemini` | `.gemini/skills/` | `~/.gemini/skills/` |
| Antigravity App / IDE | `antigravity` | `.agents/skills/` | `~/.gemini/config/skills/` |
| Antigravity CLI | `antigravity-cli` | `.agents/skills/` | `~/.gemini/antigravity-cli/skills/` |
| Diğer uyumlu ajanlar | `generic` veya `--target` | Ajana bağlı | Ajana bağlı |

Aracınıza uygun komutu seçin:

```bash
python tooling/install.py --agent claude --scope user
python tooling/install.py --agent gemini --repo "/path/to/my-project"
python tooling/install.py --agent antigravity --scope user
python tooling/install.py --target "/path/to/another-agent/skills"
```

Aynı ajanın keşfettiği dizinlere yinelenen kopyalar kurmayın. Gemini, `.agents/skills` yolunu da desteklediği için ortak Codex kurulumu zaten görünür olabilir. Ajanın beceri listesini kontrol edin, ardından açıkça `unified-development-standard` kullanmasını isteyin. Gerekirse listeyi yenileyin veya yeni oturum açın. Dosyaları kopyalamak ve modelin onları kullandığını doğrulamak ayrı kontrollerdir.

Yollar 2026-10-27 tarihinde resmî belgelerle karşılaştırılmıştır: [Codex](https://learn.chatgpt.com/docs/build-skills), [Claude Code](https://code.claude.com/docs/en/skills), [Gemini CLI](https://geminicli.com/docs/cli/skills/), [Antigravity](https://antigravity.google/docs/skills). Arayüzler değişebilir; her platformda canlı çalıştırma yapıldığı iddia edilmez.

### Lovable ve bulut arayüzleri

Lovable'da **Workspace settings → Skills → Add → Import from GitHub** yolunu izleyip [çekirdek beceri klasörünü](https://github.com/iamaia-offcials/full-stack-enginer-skill/tree/main/.agents/skills/unified-development-standard) seçin. [Lovable belgelerine](https://docs.lovable.dev/features/skills) göre çalışma alanı sahibi veya yönetici yetkisi gerekir. Alternatif olarak **Upload ZIP** kullanın.

Taşınabilir arşivi oluşturmak için:

```bash
python tooling/package.py
```

Çıktı `dist/unified-development-standard.zip` dosyasıdır; giriş dosyasını, başvuru kaynaklarını, kılavuzları, örnekleri ve lisansı içerir. Paketin tamamını içe aktarın; yalnızca `SKILL.md` yeterli değildir. Claude Code'a kurulum, beceriyi Claude bulut hesabınıza kurmaz; hesabın desteklediği içe aktarma yöntemini kullanın. Bu kurucu bulut hesaplarını yönetmez.

Dosya erişimi olan ancak yerel beceri desteği olmayan bir ajandan ana `SKILL.md` dosyasını ve ilgili bağlantılı bölümleri okumasını isteyin. Dosya veya içe aktarma desteği yoksa talimatlar sohbet içinde verilmelidir; bu otomatik kurulum değildir. Uyumluluk yalnızca model adına değil, ortama bağlıdır.

## Kurulumu yapay zekâdan isteme

Terminal ve dosya erişimi olan bir ajana şu isteği verin:

> https://github.com/iamaia-offcials/full-stack-enginer-skill.git adresindeki mühendislik becerisini kur. README ve kurucuyu oku. Bu araca uygun beceri dizinini ve istenen kurulum kapsamını seç; kapsam belirtilmemişse mevcut projeyi kullan. Önce dry-run çalıştır, sonra mevcut proje talimat dosyalarını değiştirmeden ve yerel düzenlemelerin üzerine yazmadan kur. Kurulan SKILL.md dosyasını ve başvuru kaynaklarını doğrula; ajanın beceriyi keşfedip keşfetmediğini ayrıca bildir. Dosya sistemi üzerinden kurulum mümkün değilse belgelenmiş içe aktarmayı kullan veya somut kısıtı açıkla.

Bulut arayüzleri için yukarıdaki GitHub/ZIP içe aktarmasını kullanın. Sohbet arayüzünün olması Python terminalinin de olduğu anlamına gelmez.

## İsteğe bağlı profiller

Çekirdek zaten tüm alanları kapsar. Profilleri yalnızca ayrı uzmanlık iş akışları yararlıysa kurun. Kurucu çekirdek bağımlılığını her zaman ekler.

```bash
python tooling/install.py --list
python tooling/install.py --agent codex --scope user --skills uds-security,uds-backend
python tooling/install.py --agent codex --scope user --skills all
```

Profiller: `uds-product-discovery`, `uds-requirements-planning`, `uds-architecture`, `uds-design-system`, `uds-frontend`, `uds-web-development`, `uds-technical-seo`, `uds-backend`, `uds-data`, `uds-mobile-development`, `uds-performance-optimization`, `uds-dependency-upgrades`, `uds-code-review`, `uds-testing`, `uds-security`, `uds-git-cicd`, `uds-operations`, `uds-project-audit`.

## Kullanım örnekleri

> unified-development-standard kullan. Bir müşteri portalı planla: ürün vizyonunu ve iş kurallarını tanımla, ilk sürümün kapsamını belirle, ilerideki personel ekiplerini ve ödemeleri değerlendir, teknoloji yığınını seç. Hangi temellerin şimdi gerekçelendirilebildiğini ve hangi işlerin bekleyebileceğini açıkla.

> unified-development-standard kullan. Mevcut CRM'e e-posta alanı ekle. Mevcut bileşeni ve sözleşmeyi yeniden kullan, sunucu doğrulamasını ve yetkileri kontrol et, güncel özellik belgesini düzenle ve ilgili kontrolleri çalıştır.

## Güncelleme, kurtarma ve kaldırma

Yerel depo kopyanızda değişiklikleri çekin ve aynı ajan, kapsam ve beceri seçimiyle kurulumu tekrarlayın:

```bash
git pull --ff-only
python tooling/install.py --agent codex --scope user --update --dry-run
python tooling/install.py --agent codex --scope user --update
```

Profil kurduysanız güncellemede aynı `--skills` seçimini ekleyin. Kurucu dosya özetlerini kaydeder; yerel değişiklik veya eklenen dosya varsa durur. Güncellemeden önce bu değişiklikleri koruyup yeni sürümle uzlaştırın. Manifesti olmayan eski bir kurulumu yönetim altına almak için önce dosyalarını inceleyin, ardından açıkça şu komutları kullanın:

```bash
python tooling/install.py --agent codex --scope user --update --adopt-existing --dry-run
python tooling/install.py --agent codex --scope user --update --adopt-existing
```

`--adopt-existing`, aynı adlı beceri klasörlerini değiştirir ve eski dosyaları `skills/` dizininin yanındaki `.uds-backups/` içinde saklar. Düzenlenmiş yönetilen kurulumların korumasını aşmaz. Olağan değiştirme hataları geri alma işlemini tetikler; süreç kesintisi veya elektrik kaybından sonra yedekten kurtarın. Elle kurtarmadan önce mevcut klasörü koruyun, sonra seçilen yedeği becerinin özgün adıyla geri yükleyin.

Kaldırmak için yalnızca seçilen kurulu beceri klasörünü silin. Çekirdeği kaldırmak ona bağlı profilleri bozar. Bulut becerileri kendi ayarları üzerinden kaldırılmalıdır. İlgisiz becerileri silmeyin.

Sembolik bağlantılar, junction ve reparse yolları kasıtlı olarak reddedilir. Bir çökme sonrasında `.uds-install.lock` kaldıysa önce başka bir kurucunun çalışmadığından emin olun, sonra yalnızca bu kilit dosyasını kaldırın.

## Depo ve doğrulama

```text
README.md                       Ana İngilizce açıklama ve kurulum
LICENSE                         MIT
.agents/skills/
  unified-development-standard/ Çekirdek, kurallar, kılavuzlar, şablonlar ve örnekler
  uds-*/SKILL.md                 İsteğe bağlı alan iş akışları
docs/i18n/                      Genel README çevirileri
docs/REVIEW.md                   Güncel inceleme kanıtları ve sınırlamalar
tooling/                        Kurucu, paketleme, doğrulama ve değerlendirme
tests/                          Dosya sistemi ve paket regresyon testleri
```

```bash
python tooling/validate_suite.py
python -m unittest discover -s tests -v
python tooling/package.py
```

Bu kontroller meta verileri, yerel bağlantıları, kural kimliklerini, kurulumu, güncelleme korumasını ve arşivin taşınabilirliğini kapsar. Her ajanın doğru davranacağını veya bir uygulamanın güvenli olduğunu kanıtlamaz. [İncelemeye](../REVIEW.md) ve [davranış değerlendirme kılavuzuna](../../tooling/EVALUATION_GUIDE.md) bakın.

Katkılar: kanonik kuralı kimliğini koruyarak düzenleyin; davranış değişiklikleri için yararlı açıklama/örnekler ve yeniden üretilebilir bir senaryo ekleyin. Mevcut belgeleri yerinde güncelleyin. README çevirilerini İngilizceyle uyumlu tutun; kurulan beceriyi her dil için çevirmeyin veya çoğaltmayın.

## Lisans ve sınırlar

[MIT](../../LICENSE). Bağlantı verilen üçüncü taraf belgeler kendi koşullarına tabidir. Standartlara veya şirketlere yapılan atıflar sertifikasyon ya da onay anlamına gelmez.

Beceri, uygulama güvenliğini, arama sıralamasını, yasal uyumu veya gelecekte geçiş gerekmeyeceğini garanti etmez. Bunlar projeye özgü doğrulama gerektirir. Araç, hesap veya yayınlama ve üretim sistemlerinde işlem yapma yetkisi sağlamaz.

