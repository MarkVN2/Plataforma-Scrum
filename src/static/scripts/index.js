// Bootstrap tooltips activation
const tooltips = document.querySelectorAll('[data-bs-toggle="tooltip"]');
tooltips.forEach(t=>{new bootstrap.Tooltip(t)});

// Loading screen
(function timer(){
  setTimeout(()=>{document.getElementById('loader').style.display = "none";}, 300)
})()

// Navbar display on scroll:
let prevScrollpos = window.pageYOffset;
document.addEventListener("scroll", ()=>{
  let currentScrollPos = window.pageYOffset;
  let navbar = document.querySelector("nav.navbar")
  let navHeight = navbar.getBoundingClientRect().height;
  if (prevScrollpos > currentScrollPos) {
    navbar.style.top = "0";
  } else {
    navbar.style.top = `-${navHeight}px`;
  }
  prevScrollpos = currentScrollPos;
})

// Handling Dark-mode and Light-mode
let themeQuery = window.matchMedia("(prefers-color-scheme: dark)");
let favicon = document.querySelector(`link[rel="icon"]`);
if (themeQuery.matches) favicon.setAttribute("href", "../../static/images/fav_icon_light.png");
themeQuery.addEventListener("change", e => {
  e.matches ? favicon.setAttribute("href", "../../static/images/fav_icon_light.png") : favicon.setAttribute("href", "../../static/images/fav_icon.png");
})

let themePreference = localStorage.getItem("themePref")
let themeSwitch = document.querySelector("input#themeSwitch");
docRoot = document.documentElement
if (themePreference == "dark") {
  docRoot.setAttribute("data-theme", "dark")
  themeSwitch.checked = true;
}

themeSwitch.addEventListener("change", el => {
  if (el.target.checked){
    docRoot.setAttribute("data-theme", "dark")
    localStorage.setItem("themePref", "dark")
  } else {
    docRoot.setAttribute("data-theme", "light")
    localStorage.setItem("themePref", "light")
  }
})

//handling language change
const langBtn = document.querySelector("img#langBtn");
langBtn.addEventListener("click", ()=>{
  let currLang = langBtn.getAttribute("data-current-lang")
  location.pathname == "/" ? path = "" : path = location.pathname; 
  currLang == "br" ? location.href = `/en${path}` : location.href = `${path.slice(3)}` || `/`
})