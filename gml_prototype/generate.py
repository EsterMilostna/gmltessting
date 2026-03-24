from pathlib import Path
import json

root = Path('/mnt/data/gml_prototype')
assets = root / 'assets'
assets.mkdir(exist_ok=True)

menu = {
    'KDO JSME': [
        ('Základní údaje o škole', 'zakladni-udaje-o-skole.html'),
        ('Kontakty', 'kontakty.html'),
        ('Pedagogický sbor', 'pedagogicky-sbor.html'),
        ('Organizační schéma', 'organizacni-schema.html'),
        ('Školská rada', 'skolska-rada.html'),
        ('Školní poradenské pracoviště', 'skolni-poradenske-pracoviste.html'),
        ('Naše vize/koncepce', 'nase-vize-koncepce.html'),
        ('Plán školy', 'plan-skoly.html'),
        ('Nadační fond GML', 'nadacni-fond-gml.html'),
    ],
    'AKTIVITY': [
        ('Aktuality', 'aktuality.html'),
        ('Kalendář', 'kalendar.html'),
        ('Další položky sekce', 'aktivity-dalsi-polozky.html'),
    ],
    'PRO STUDENTY A RODIČE': [
        ('Odkazy a návody', 'odkazy-a-navody.html'),
        ('Volitelné předměty', 'volitelne-predmety.html'),
        ('Maturitní zkoušky', 'maturitni-zkousky.html'),
        ('Karty ISIC', 'karty-isic.html'),
        ('Formuláře', 'formulare.html'),
        ('Studentský parlament', 'studentsky-parlament.html'),
    ],
    'PRO UCHAZEČE': [
        ('8 leté studium', '8-lete-studium.html'),
        ('6 leté studium', '6-lete-studium.html'),
        ('4 leté studium', '4-lete-studium.html'),
        ('Přijímací zkoušky', 'prijimaci-zkousky.html'),
        ('Počty přijatých na VŠ', 'pocty-prijatych-na-vs.html'),
    ],
    'DOKUMENTY': [
        ('ŠVP', 'svp.html'),
        ('Školní řád', 'skolni-rad.html'),
        ('Řád školní jídelny', 'rad-skolni-jidelny.html'),
        ('Způsob hodnocení', 'zpusob-hodnoceni.html'),
        ('Preventivní program', 'preventivni-program.html'),
        ('Žádosti', 'zadosti.html'),
        ('GDPR', 'gdpr.html'),
        ('Pro oznamovatele', 'pro-oznamovatele.html'),
        ('Ročenky', 'rocenky.html'),
        ('ČŠI', 'csi.html'),
    ],
}

placeholder_descriptions = {
    'Základní údaje o škole': 'Na této stránce by uživatelé našli základní informace o škole, její profil a hlavní charakteristiku.',
    'Kontakty': 'Na této stránce by uživatelé našli kontaktní údaje, adresu školy a spojení na jednotlivá oddělení.',
    'Pedagogický sbor': 'Na této stránce by uživatelé našli přehled pedagogického sboru a kontakty na vyučující.',
    'Organizační schéma': 'Na této stránce by uživatelé našli organizační strukturu školy a rozdělení odpovědností.',
    'Školská rada': 'Na této stránce by uživatelé našli informace o školské radě, jejím složení a činnosti.',
    'Školní poradenské pracoviště': 'Na této stránce by uživatelé našli služby školního poradenského pracoviště a možnosti podpory.',
    'Naše vize/koncepce': 'Na této stránce by uživatelé našli vizi školy, hodnoty a dlouhodobé směřování.',
    'Plán školy': 'Na této stránce by uživatelé našli hlavní cíle, priority a plán rozvoje školy.',
    'Nadační fond GML': 'Na této stránce by uživatelé našli informace o nadačním fondu a možnostech podpory školy.',
    'Aktuality': 'Na této stránce by uživatelé našli novinky, důležitá oznámení a aktuální dění.',
    'Kalendář': 'Na této stránce by uživatelé našli termíny akcí, školních událostí a důležitých dat.',
    'Další položky sekce': 'Na této stránce by uživatelé našli další obsah původní sekce Aktivity kromě ISIC a ŠPP.',
    'Odkazy a návody': 'Na této stránce by uživatelé našli užitečné odkazy, návody a rychlou pomoc pro studium.',
    'Volitelné předměty': 'Na této stránce by uživatelé našli nabídku volitelných předmětů a informace k výběru.',
    'Maturitní zkoušky': 'Na této stránce by uživatelé našli informace k maturitním zkouškám, termínům a požadavkům.',
    'Karty ISIC': 'Na této stránce by uživatelé našli informace o ISIC kartách a jejich využití.',
    'Formuláře': 'Na této stránce by uživatelé našli formuláře ke stažení a návody, jak je vyplnit.',
    'Studentský parlament': 'Na této stránce by uživatelé našli informace o studentském parlamentu a jeho aktivitách.',
    '8 leté studium': 'Na této stránce by uživatelé našli přehled osmiletého studia, podmínky a důležité informace pro uchazeče.',
    '6 leté studium': 'Na této stránce by uživatelé našli přehled šestiletého studia, podmínky a důležité informace pro uchazeče.',
    '4 leté studium': 'Na této stránce by uživatelé našli přehled čtyřletého studia, podmínky a důležité informace pro uchazeče.',
    'Přijímací zkoušky': 'Na této stránce by uživatelé našli informace o přijímacích zkouškách, termínech a průběhu.',
    'Počty přijatých na VŠ': 'Na této stránce by uživatelé našli statistiky a přehled počtů přijatých studentů na vysoké školy.',
    'ŠVP': 'Na této stránce by uživatelé našli školní vzdělávací program a související dokumenty.',
    'Školní řád': 'Na této stránce by uživatelé našli školní řád a pravidla fungování školy.',
    'Řád školní jídelny': 'Na této stránce by uživatelé našli pravidla školní jídelny a provozní informace.',
    'Způsob hodnocení': 'Na této stránce by uživatelé našli pravidla hodnocení a klasifikace.',
    'Preventivní program': 'Na této stránce by uživatelé našli preventivní program školy a související opatření.',
    'Žádosti': 'Na této stránce by uživatelé našli žádosti ke stažení a instrukce k jejich podání.',
    'GDPR': 'Na této stránce by uživatelé našli informace o ochraně osobních údajů a GDPR.',
    'Pro oznamovatele': 'Na této stránce by uživatelé našli informace pro oznamovatele a související postupy.',
    'Ročenky': 'Na této stránce by uživatelé našli ročenky a archiv vybraných materiálů.',
    'ČŠI': 'Na této stránce by uživatelé našli dokumenty a výstupy související s Českou školní inspekcí.',
}

cards = [
    ('8 leté studium', '8-lete-studium.html', 'card-green'),
    ('6 leté studium', '6-lete-studium.html', 'card-red'),
    ('4 leté studium', '4-lete-studium.html', 'card-blue'),
]

placeholder_points = [
    'kam v navigaci tato stránka patří',
    'jaké informace by zde očekávali',
    'zda je pojmenování sekce srozumitelné',
]

nav_items = list(menu.items())
menu_json = json.dumps(menu, ensure_ascii=False)


def shell_html(title: str, body_class: str, main_content: str, page_title: str = '', page_section: str = ''):
    return f'''<!doctype html>
<html lang="cs">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} | GML prototyp</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/styles.css">
</head>
<body class="{body_class}" data-page-title="{page_title}" data-page-section="{page_section}">
  <div id="site-header"></div>
  {main_content}
  <div id="site-footer"></div>
  <script src="assets/app.js"></script>
</body>
</html>'''

home_main = f'''
<main>
  <section class="hero">
    <div class="container hero-inner">
      <div class="hero-panel">
        <p class="eyebrow">Nová struktura webu</p>
        <h1>GML je životní styl</h1>
        <div class="hero-actions">
          <a class="btn btn-primary" href="prijimaci-zkousky.html">Podat přihlášku</a>
          <a class="btn btn-secondary" href="pocty-prijatych-na-vs.html">Počty přihlášených a přijatých</a>
        </div>
      </div>
    </div>
  </section>

  <section class="study-cards container">
    {''.join(f'<a class="study-card {cls}" href="{href}"><h2>{label}</h2><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sollicitudin in nisi ac efficitur.</p><span>Zjistit víc</span></a>' for label, href, cls in cards)}
  </section>

  <section class="news-section container">
    <h2 class="section-title">Aktuality</h2>
    <div class="news-grid">
      <article class="news-card news-wide">
        <div class="news-image abstract-one"></div>
        <h3>This outstanding object</h3>
        <p>Call out a feature, benefit, or value that can stand on its own.</p>
      </article>
      <article class="news-card news-tall">
        <div class="news-image abstract-two"></div>
        <h3>Featured story</h3>
        <p>Ukázkový blok pro aktuality a vizuální test domovské stránky.</p>
      </article>
      <article class="news-card news-small">
        <div class="news-image abstract-three"></div>
        <h3>Další novinka</h3>
        <p>Menší karta pro rychlé ověření orientace a struktury sekce.</p>
      </article>
    </div>
  </section>

  <section class="partners container">
    <h2 class="section-title section-title-muted">Našimi partnery jsou</h2>
    <div class="partner-logos">
      <span>Masarykova univerzita</span>
      <span>VUT</span>
      <span>JAMU</span>
      <span>Mendelova univerzita</span>
      <span>CEITEC</span>
    </div>
  </section>
</main>
'''

(root / 'index.html').write_text(shell_html('Homepage', 'home', home_main), encoding='utf-8')

for section, items in menu.items():
    for title, filename in items:
        desc = placeholder_descriptions[title]
        breadcrumb = f'<a href="index.html">Domů</a><span>/</span><span>{section}</span><span>/</span><strong>{title}</strong>'
        content = f'''
<main class="placeholder-main">
  <div class="container">
    <nav class="breadcrumb">{breadcrumb}</nav>
    <section class="placeholder-hero">
      <p class="eyebrow">Zástupná stránka pro testování</p>
      <h1>{title}</h1>
      <p class="placeholder-lead">{desc}</p>
    </section>
    <section class="placeholder-grid">
      <article class="placeholder-card">
        <h2>Co zde uživatel najde</h2>
        <p>{desc}</p>
      </article>
      <article class="placeholder-card">
        <h2>Co chceme otestovat</h2>
        <ul>
          {''.join(f'<li>{point}</li>' for point in placeholder_points)}
        </ul>
      </article>
      <article class="placeholder-card">
        <h2>Další krok</h2>
        <p>Tato stránka zatím není finálně navržená. V další iteraci zde bude doplněn konkrétní obsah a finální vizuální řešení.</p>
      </article>
    </section>
  </div>
</main>
'''
        (root / filename).write_text(shell_html(title, 'placeholder-page', content, title, section), encoding='utf-8')

styles = r'''
:root {
  --color-primary: #1d57ad;
  --color-primary-dark: #15478f;
  --color-accent-green: #b3d526;
  --color-accent-red: #f03838;
  --color-accent-blue: #23aae4;
  --color-bg: #f2f2f2;
  --color-surface: #ffffff;
  --color-text: #111111;
  --color-muted: #6e6e73;
  --color-border: #d9d9de;
  --shadow-soft: 0 12px 30px rgba(0,0,0,.08);
  --radius: 18px;
  --container: 1180px;
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: 'Inter', system-ui, sans-serif;
  color: var(--color-text);
  background: var(--color-bg);
}
a { color: inherit; text-decoration: none; }
img { max-width: 100%; display: block; }
.container { width: min(var(--container), calc(100% - 32px)); margin: 0 auto; }

.site-header {
  position: sticky; top: 0; z-index: 50;
  background: rgba(242,242,242,.95);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(0,0,0,.05);
}
.header-inner {
  display: flex; align-items: center; justify-content: space-between;
  gap: 20px; min-height: 92px;
}
.logo { display: flex; align-items: center; gap: 12px; flex-shrink: 0; }
.logo-mark {
  width: 46px; height: 46px; border-radius: 12px; border: 2px solid var(--color-primary);
  display: grid; place-items: center; color: var(--color-primary); font-weight: 700;
  font-family: 'Barlow Condensed', sans-serif; font-size: 1.5rem;
  background: white;
}
.logo-text { font-size: .72rem; line-height: 1.1; color: var(--color-muted); }
.desktop-nav { display: flex; gap: 14px; align-items: center; }
.nav-item {
  position: relative;
  padding: 18px 0 22px;
  margin: -18px 0 -22px;
}
.nav-link {
  display: inline-flex;
  align-items: center;
  font-family: 'Barlow Condensed', sans-serif;
  font-size: clamp(1.7rem, 1.3vw, 2rem);
  color: var(--color-primary);
  letter-spacing: .02em;
  text-transform: uppercase;
  white-space: nowrap;
}
.nav-link:hover,
.nav-item:hover > .nav-link,
.nav-item:focus-within > .nav-link { color: var(--color-primary-dark); }
.dropdown-menu {
  position: absolute;
  top: calc(100% - 4px);
  left: 0;
  min-width: 280px;
  display: none;
  background: var(--color-primary);
  color: white;
  box-shadow: var(--shadow-soft);
  border-radius: 0 0 14px 14px;
  overflow: hidden;
}
.nav-item:hover .dropdown-menu,
.nav-item:focus-within .dropdown-menu { display: block; }
.dropdown-menu a {
  display: block;
  padding: 14px 16px;
  border-bottom: 1px solid rgba(255,255,255,.45);
  font-size: 1rem;
}
.dropdown-menu a:hover,
.dropdown-menu a:focus-visible { background: rgba(255,255,255,.12); outline: none; }
.dropdown-menu a:last-child { border-bottom: 0; }
.menu-toggle {
  display: none; border: 0; background: white; border-radius: 12px; width: 52px; height: 52px;
  align-items: center; justify-content: center; flex-direction: column; gap: 5px; box-shadow: var(--shadow-soft);
}
.menu-toggle span { width: 22px; height: 2px; background: var(--color-primary); display: block; }
.mobile-menu { display: none; border-top: 1px solid rgba(0,0,0,.06); background: var(--color-surface); }
.mobile-menu-inner { padding: 8px 0 16px; }
.mobile-group { border-bottom: 1px solid var(--color-border); }
.mobile-group summary {
  list-style: none; cursor: pointer; padding: 16px 0;
  font-family: 'Barlow Condensed', sans-serif; font-size: 1.7rem; color: var(--color-primary);
  text-transform: uppercase;
}
.mobile-group summary::-webkit-details-marker { display: none; }
.mobile-submenu { padding: 0 0 16px; display: grid; gap: 0; }
.mobile-submenu a {
  background: var(--color-primary); color: white; padding: 12px 14px; border-bottom: 1px solid rgba(255,255,255,.45);
}
.mobile-submenu a:last-child { border-bottom: 0; }

.hero {
  position: relative; overflow: hidden;
  background:
    linear-gradient(rgba(255,255,255,.55), rgba(255,255,255,.55)),
    radial-gradient(circle at 50% 10%, rgba(29,87,173,.08), transparent 20%),
    linear-gradient(125deg, #dce8f1 0%, #f6f1ea 35%, #d9e8ef 70%, #cfd7d7 100%);
}
.hero::before {
  content: ''; position: absolute; inset: 0;
  background:
    linear-gradient(to right, transparent 0 10%, rgba(0,0,0,.05) 10% 11%, transparent 11% 33%, rgba(0,0,0,.05) 33% 34%, transparent 34% 66%, rgba(0,0,0,.05) 66% 67%, transparent 67% 89%, rgba(0,0,0,.05) 89% 90%, transparent 90%),
    linear-gradient(to bottom, transparent 0 18%, rgba(0,0,0,.04) 18% 19%, transparent 19% 100%);
  opacity: .8;
}
.hero-inner { position: relative; z-index: 1; min-height: 430px; display: flex; align-items: center; }
.hero-panel { max-width: 760px; padding: 60px 0; }
.eyebrow {
  margin: 0 0 12px; color: var(--color-primary); font-weight: 700; text-transform: uppercase; letter-spacing: .08em; font-size: .82rem;
}
.hero h1,
.placeholder-hero h1 {
  margin: 0; font-family: 'Inter', sans-serif; font-size: clamp(3rem, 6vw, 5.2rem); line-height: .95; font-weight: 800;
}
.hero-actions { display: flex; gap: 14px; margin-top: 28px; flex-wrap: wrap; }
.btn {
  display: inline-flex; align-items: center; justify-content: center; min-height: 60px;
  padding: 0 24px; border-radius: 16px; font-size: 1.05rem; font-weight: 600;
}
.btn-primary { background: #000; color: #fff; }
.btn-secondary { background: rgba(255,255,255,.6); border: 2px solid rgba(0,0,0,.14); }

.study-cards {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; margin-top: -40px; position: relative; z-index: 2;
}
.study-card {
  color: white; padding: 24px; border-radius: 18px; min-height: 250px;
  display: flex; flex-direction: column; box-shadow: var(--shadow-soft);
}
.study-card h2 { margin: 0 0 12px; font-family: 'Barlow Condensed', sans-serif; font-size: 2rem; }
.study-card p { margin: 0 0 24px; line-height: 1.5; max-width: 28ch; }
.study-card span {
  margin-top: auto; align-self: flex-start; background: rgba(255,255,255,.92); color: #222;
  padding: 12px 20px; border-radius: 14px; font-weight: 600;
}
.card-green { background: var(--color-accent-green); }
.card-red { background: var(--color-accent-red); }
.card-blue { background: var(--color-accent-blue); }

.section-title {
  margin: 72px 0 28px; text-align: center; font-size: clamp(2rem, 3vw, 2.6rem); font-weight: 800;
}
.section-title-muted { color: #8a8a8f; font-weight: 500; }
.news-grid {
  display: grid; grid-template-columns: 1.1fr 1fr; grid-template-areas: 'wide tall' 'small tall'; gap: 18px;
}
.news-card {
  background: #d9d9dc; border-radius: 10px; padding: 14px; min-height: 180px;
}
.news-wide { grid-area: wide; }
.news-tall { grid-area: tall; }
.news-small { grid-area: small; }
.news-image { border-radius: 8px; margin-bottom: 12px; }
.abstract-one { height: 140px; background: linear-gradient(160deg, #fff 10%, #ff47ba 10% 35%, #ffd9f3 35% 100%); }
.abstract-two { height: 250px; background: radial-gradient(circle at 50% 64%, #f0ebd8 0 8%, transparent 8%), linear-gradient(180deg, #b8c5ff, #7eacef 55%, #a0a54d); }
.abstract-three { height: 92px; background: linear-gradient(180deg, #fff, #f9f9f9 70%, transparent 70%), linear-gradient(135deg, #1e5b8f 20%, transparent 20%), linear-gradient(45deg, #1a7d3f 20%, transparent 20%); }
.news-card h3 { margin: 0 0 8px; font-size: 1rem; }
.news-card p { margin: 0; color: #555; font-size: .92rem; }

.partners { padding-bottom: 70px; }
.partner-logos {
  display: flex; flex-wrap: wrap; gap: 28px; justify-content: center; align-items: center;
  color: var(--color-primary); font-weight: 700; letter-spacing: .03em;
}
.partner-logos span { opacity: .95; }

.placeholder-main { padding: 24px 0 72px; }
.breadcrumb { display: flex; gap: 10px; align-items: center; color: var(--color-muted); font-size: .95rem; margin: 10px 0 30px; flex-wrap: wrap; }
.placeholder-hero {
  background: linear-gradient(135deg, rgba(29,87,173,.08), rgba(29,87,173,.02));
  border: 1px solid rgba(29,87,173,.12); border-radius: 28px; padding: 42px;
}
.placeholder-lead { font-size: 1.15rem; color: #444; max-width: 70ch; line-height: 1.6; }
.placeholder-grid {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; margin-top: 24px;
}
.placeholder-card {
  background: white; border-radius: 20px; padding: 24px; box-shadow: var(--shadow-soft); min-height: 220px;
}
.placeholder-card h2 { margin-top: 0; font-size: 1.2rem; }
.placeholder-card ul { margin: 0; padding-left: 18px; line-height: 1.7; }

.site-footer { background: #030303; color: white; padding: 26px 0; }
.footer-grid { display: grid; grid-template-columns: 1.1fr 1fr 1fr; gap: 24px; }
.footer-brand { font-family: 'Barlow Condensed', sans-serif; font-size: 2rem; margin-bottom: 8px; }
.site-footer p { margin: 0; color: rgba(255,255,255,.82); line-height: 1.6; }

@media (max-width: 1080px) {
  .desktop-nav { display: none; }
  .menu-toggle { display: inline-flex; }
  .mobile-menu.open { display: block; }
  .study-cards { grid-template-columns: 1fr; margin-top: 22px; }
  .news-grid { grid-template-columns: 1fr; grid-template-areas: 'wide' 'small' 'tall'; }
  .placeholder-grid, .footer-grid { grid-template-columns: 1fr; }
}

@media (max-width: 720px) {
  .header-inner { min-height: 78px; }
  .logo-text { display: none; }
  .container { width: min(var(--container), calc(100% - 20px)); }
  .hero-inner { min-height: 360px; align-items: flex-end; }
  .hero-panel { padding: 30px 0 32px; }
  .hero-actions { flex-direction: column; align-items: flex-start; }
  .btn { width: 100%; max-width: 320px; }
  .study-card { min-height: 220px; }
  .section-title { margin-top: 52px; }
  .placeholder-hero { padding: 26px; border-radius: 22px; }
}
'''

app_js = f'''
const MENU = {menu_json};

function renderHeader() {{
  const desktopItems = Object.entries(MENU).map(([title, items]) => {{
    const firstHref = items[0][1];
    const dropdown = items.map(([name, href]) => `<a href="${{href}}">${{name}}</a>`).join('');
    return `
      <div class="nav-item">
        <a class="nav-link" href="${{firstHref}}">${{title}}</a>
        <div class="dropdown-menu">${{dropdown}}</div>
      </div>`;
  }}).join('');

  const mobileGroups = Object.entries(MENU).map(([title, items]) => {{
    const links = items.map(([name, href]) => `<a href="${{href}}">${{name}}</a>`).join('');
    return `
      <details class="mobile-group">
        <summary>${{title}}</summary>
        <div class="mobile-submenu">${{links}}</div>
      </details>`;
  }}).join('');

  return `
    <header class="site-header">
      <div class="container header-inner">
        <a class="logo" href="index.html" aria-label="GML homepage">
          <span class="logo-mark">GL</span>
          <span class="logo-text"><strong>GYMNÁZIUM</strong><br>MATYÁŠE LERCHA</span>
        </a>
        <nav class="desktop-nav">${{desktopItems}}</nav>
        <button class="menu-toggle" aria-expanded="false" aria-controls="mobileMenu" aria-label="Otevřít menu">
          <span></span><span></span><span></span>
        </button>
      </div>
      <div class="mobile-menu" id="mobileMenu">
        <div class="container mobile-menu-inner">${{mobileGroups}}</div>
      </div>
    </header>`;
}}

function renderFooter() {{
  return `
    <footer class="site-footer">
      <div class="container footer-grid">
        <div>
          <div class="footer-brand">GML</div>
          <p>Gymnázium Matyáše Lercha<br>Žižkova 55, 616 00 Brno</p>
        </div>
        <div>
          <p><strong>Kontakt</strong><br>+420 549 123 021<br>info@gml.cz</p>
        </div>
        <div>
          <p><strong>Prototyp pro testování</strong><br>Navigace a struktura jsou klikací, část obsahu je zástupná.</p>
        </div>
      </div>
    </footer>`;
}}

const headerRoot = document.getElementById('site-header');
if (headerRoot) headerRoot.innerHTML = renderHeader();
const footerRoot = document.getElementById('site-footer');
if (footerRoot) footerRoot.innerHTML = renderFooter();

const toggle = document.querySelector('.menu-toggle');
const mobileMenu = document.querySelector('.mobile-menu');

if (toggle && mobileMenu) {{
  toggle.addEventListener('click', () => {{
    const expanded = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!expanded));
    mobileMenu.classList.toggle('open');
  }});
}}

const groups = document.querySelectorAll('.mobile-group');
groups.forEach((group) => {{
  group.addEventListener('toggle', () => {{
    if (group.open) {{
      groups.forEach((other) => {{
        if (other !== group) other.open = false;
      }});
    }}
  }});
}});
'''

(assets / 'styles.css').write_text(styles, encoding='utf-8')
(assets / 'app.js').write_text(app_js, encoding='utf-8')
