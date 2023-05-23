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
  let currentScrollPos = window.pageYOffset
  let navbar = document.querySelector("nav.navbar")
  let navHeight = navbar.getBoundingClientRect().height
  if (prevScrollpos > currentScrollPos) {
    navbar.style.top = "0";
  } else {
    navbar.style.top = `-${navHeight}px`;
  }
  prevScrollpos = currentScrollPos
})