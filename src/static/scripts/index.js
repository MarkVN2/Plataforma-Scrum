// Bootstrap tooltips activation
const tooltips = document.querySelectorAll('[data-bs-toggle="tooltip"]');
tooltips.forEach(t=>{new bootstrap.Tooltip(t)});

// Loading screen
var timerTime;
function timer(){
    timerTime = setTimeout(showPage, 300)
};
function showPage(){
    document.getElementById('loader').style.display = "none";
};

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