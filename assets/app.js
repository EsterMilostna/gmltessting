
const MENU = {"KDO JSME": [["Základní údaje o škole", "zakladni-udaje-o-skole.html"], ["Kontakty", "kontakty.html"], ["Pedagogický sbor", "pedagogicky-sbor.html"], ["Organizační schéma", "organizacni-schema.html"], ["Školská rada", "skolska-rada.html"], ["Školní poradenské pracoviště", "skolni-poradenske-pracoviste.html"], ["Naše vize/koncepce", "nase-vize-koncepce.html"], ["Plán školy", "plan-skoly.html"], ["Nadační fond GML", "nadacni-fond-gml.html"]], "AKTIVITY": [["Aktuality", "aktuality.html"], ["Kalendář", "kalendar.html"], ["Další položky sekce", "aktivity-dalsi-polozky.html"]], "PRO STUDENTY A RODIČE": [["Odkazy a návody", "odkazy-a-navody.html"], ["Volitelné předměty", "volitelne-predmety.html"], ["Maturitní zkoušky", "maturitni-zkousky.html"], ["Karty ISIC", "karty-isic.html"], ["Formuláře", "formulare.html"], ["Studentský parlament", "studentsky-parlament.html"]], "PRO UCHAZEČE": [["8 leté studium", "8-lete-studium.html"], ["6 leté studium", "6-lete-studium.html"], ["4 leté studium", "4-lete-studium.html"], ["Přijímací zkoušky", "prijimaci-zkousky.html"], ["Počty přijatých na VŠ", "pocty-prijatych-na-vs.html"]], "DOKUMENTY": [["ŠVP", "svp.html"], ["Školní řád", "skolni-rad.html"], ["Řád školní jídelny", "rad-skolni-jidelny.html"], ["Způsob hodnocení", "zpusob-hodnoceni.html"], ["Preventivní program", "preventivni-program.html"], ["Žádosti", "zadosti.html"], ["GDPR", "gdpr.html"], ["Pro oznamovatele", "pro-oznamovatele.html"], ["Ročenky", "rocenky.html"], ["ČŠI", "csi.html"]]};

function renderHeader() {
  const desktopItems = Object.entries(MENU).map(([title, items]) => {
    const firstHref = items[0][1];
    const dropdown = items.map(([name, href]) => `<a href="${href}">${name}</a>`).join('');
    return `
      <div class="nav-item">
        <a class="nav-link" href="${firstHref}">${title}</a>
        <div class="dropdown-menu">${dropdown}</div>
      </div>`;
  }).join('');

  const mobileGroups = Object.entries(MENU).map(([title, items]) => {
    const links = items.map(([name, href]) => `<a href="${href}">${name}</a>`).join('');
    return `
      <details class="mobile-group">
        <summary>${title}</summary>
        <div class="mobile-submenu">${links}</div>
      </details>`;
  }).join('');

  return `
    <header class="site-header">
      <div class="container header-inner">
        <a href="index.html" class="logo">
          <img src="obrazky/logo.png" alt="GML">
        </a>
        <nav class="desktop-nav">${desktopItems}</nav>
        <button class="menu-toggle" aria-expanded="false" aria-controls="mobileMenu" aria-label="Otevřít menu">
          <span></span><span></span><span></span>
        </button>
      </div>
      <div class="mobile-menu" id="mobileMenu">
        <div class="container mobile-menu-inner">${mobileGroups}</div>
      </div>
    </header>`;
}

function renderFooter() {
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
}

const headerRoot = document.getElementById('site-header');
if (headerRoot) headerRoot.innerHTML = renderHeader();
const footerRoot = document.getElementById('site-footer');
if (footerRoot) footerRoot.innerHTML = renderFooter();

const toggle = document.querySelector('.menu-toggle');
const mobileMenu = document.querySelector('.mobile-menu');

if (toggle && mobileMenu) {
  toggle.addEventListener('click', () => {
    const expanded = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!expanded));
    mobileMenu.classList.toggle('open');
  });
}

const groups = document.querySelectorAll('.mobile-group');
groups.forEach((group) => {
  group.addEventListener('toggle', () => {
    if (group.open) {
      groups.forEach((other) => {
        if (other !== group) other.open = false;
      });
    }
  });
});

document.addEventListener('click', (e) => {

  const trigger = e.target.closest('.accordion-trigger');
  if (!trigger) return;

  const item = trigger.closest('.accordion-item');
  if (!item) return;

  const isOpen = item.classList.contains('open');
  item.classList.toggle('open', !isOpen);
  trigger.setAttribute('aria-expanded', String(!isOpen));

});

(function () {
  const track = document.getElementById('partnersTrack');
  const dotsWrap = document.getElementById('partnersDots');
  if (!track || !dotsWrap) return;

  const prevBtn = document.querySelector('.partners-carousel-btn.prev');
  const nextBtn = document.querySelector('.partners-carousel-btn.next');
  const slides = Array.from(track.querySelectorAll('.partner-slide'));

  let currentPage = 0;
  let autoplay;
  const intervalMs = 3500;

  function getPerPage() {
    if (window.innerWidth <= 520) return 1;
    if (window.innerWidth <= 768) return 2;
    if (window.innerWidth <= 1024) return 3;
    return 4;
  }

  function getPageCount() {
    return Math.ceil(slides.length / getPerPage());
  }

  function renderDots() {
    const pageCount = getPageCount();
    dotsWrap.innerHTML = '';

    for (let i = 0; i < pageCount; i++) {
      const dot = document.createElement('button');
      dot.type = 'button';
      dot.setAttribute('aria-label', `Přejít na skupinu partnerů ${i + 1}`);
      if (i === currentPage) dot.classList.add('active');
      dot.addEventListener('click', () => {
        currentPage = i;
        updateCarousel();
        restartAutoplay();
      });
      dotsWrap.appendChild(dot);
    }
  }

  function updateCarousel() {
    const perPage = getPerPage();
    const pageCount = getPageCount();

    if (currentPage >= pageCount) currentPage = 0;

    const offset = currentPage * (100 / perPage);
    track.style.transform = `translateX(-${offset}%)`;

    Array.from(dotsWrap.children).forEach((dot, index) => {
      dot.classList.toggle('active', index === currentPage);
    });
  }

  function nextPage() {
    currentPage = (currentPage + 1) % getPageCount();
    updateCarousel();
  }

  function prevPage() {
    currentPage = (currentPage - 1 + getPageCount()) % getPageCount();
    updateCarousel();
  }

  function startAutoplay() {
    stopAutoplay();
    autoplay = setInterval(nextPage, intervalMs);
  }

  function stopAutoplay() {
    if (autoplay) clearInterval(autoplay);
  }

  function restartAutoplay() {
    startAutoplay();
  }

  prevBtn?.addEventListener('click', () => {
    prevPage();
    restartAutoplay();
  });

  nextBtn?.addEventListener('click', () => {
    nextPage();
    restartAutoplay();
  });

  window.addEventListener('resize', () => {
    renderDots();
    updateCarousel();
  });

  track.addEventListener('mouseenter', stopAutoplay);
  track.addEventListener('mouseleave', startAutoplay);
  prevBtn?.addEventListener('mouseenter', stopAutoplay);
  prevBtn?.addEventListener('mouseleave', startAutoplay);
  nextBtn?.addEventListener('mouseenter', stopAutoplay);
  nextBtn?.addEventListener('mouseleave', startAutoplay);

  renderDots();
  updateCarousel();
  startAutoplay();
})();


/* =========================
   Zvýraznění aktivní sekce v menu
========================= */

const currentSection = document.body.dataset.pageSection;

if (currentSection) {
  document.querySelectorAll('.nav-link').forEach(link => {
    if (link.textContent.trim() === currentSection) {
      link.classList.add('is-active');
    }
  });
}

const teacherData = {

adolf: {
name: "Petr Adolf",
subject: "matematika, fyzika",
room: "kabinet 213",
email: "adolf@gml.cz",
phone: "549 122 111",
class: "1.A"
},

ampapa: {
name: "Pavel Ampapa",
subject: "informatika",
room: "kabinet 310",
email: "ampapa@gml.cz",
phone: "549 122 112",
class: "-"
},

barakova: {
name: "Marcela Baráková",
subject: "angličtina",
room: "kabinet 118",
email: "barakova@gml.cz",
phone: "549 122 113",
class: "2.B"
},

bartak: {
name: "Milan Barták",
subject: "dějepis",
room: "kabinet 204",
email: "bartak@gml.cz",
phone: "549 122 114",
class: "-"
},

benes: {
name: "Vojtěch Beneš",
subject: "chemie",
room: "kabinet 221",
email: "benes@gml.cz",
phone: "549 122 115",
class: "-"
},

benesova: {
name: "Šárka Benešová",
subject: "biologie",
room: "kabinet 218",
email: "benesova@gml.cz",
phone: "549 122 116",
class: "3.C"
},

blaha: {
name: "Vladimír Bláha",
subject: "zeměpis",
room: "kabinet 119",
email: "blaha@gml.cz",
phone: "549 122 117",
class: "-"
},

blazek: {
name: "Pavel Blažek",
subject: "tělesná výchova",
room: "kabinet TV",
email: "blazek@gml.cz",
phone: "549 122 118",
class: "-"
},

bochnickova: {
name: "Eva Bochníčková",
subject: "francouzština",
room: "kabinet 115",
email: "bochnickova@gml.cz",
phone: "549 122 119",
class: "1.F"
},

borosova: {
name: "Romana Borošová",
subject: "český jazyk",
room: "kabinet 205",
email: "borosova@gml.cz",
phone: "549 122 120",
class: "3.AV"
},

broulik: {
name: "Aleš Broulík",
subject: "informatika",
room: "kabinet 312",
email: "broulik@gml.cz",
phone: "549 122 121",
class: "-"
},

brunnova: {
name: "Eva Brunnová",
subject: "němčina",
room: "kabinet 117",
email: "brunnova@gml.cz",
phone: "549 122 122",
class: "2.N"
}

};


const modal = document.getElementById("teacherModal");

document.querySelectorAll(".teacher-link").forEach(link => {

link.addEventListener("click", () => {

const id = link.dataset.teacher;
const teacher = teacherData[id];

document.getElementById("teacherName").textContent = teacher.name;
document.getElementById("teacherSubject").textContent = teacher.subject;
document.getElementById("teacherRoom").textContent = teacher.room;
document.getElementById("teacherEmail").textContent = teacher.email;
document.getElementById("teacherPhone").textContent = teacher.phone;
document.getElementById("teacherClass").textContent = teacher.class;

modal.classList.add("active");

});

});

document.querySelector(".teacher-close").onclick = () => {
modal.classList.remove("active");
};

modal.onclick = (e) => {
if(e.target === modal) modal.classList.remove("active");
};