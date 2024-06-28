const body = document.body

const btnTheme = document.querySelector('.fa-moon')
const btnHamburger = document.querySelector('.fa-bars')

const addThemeClass = (bodyClass, btnClass) => {
  body.classList.add(bodyClass)
  btnTheme.classList.add(btnClass)
}

const getBodyTheme = localStorage.getItem('portfolio-theme')
const getBtnTheme = localStorage.getItem('portfolio-btn-theme')

addThemeClass(getBodyTheme, getBtnTheme)

const isDark = () => body.classList.contains('dark')

const setTheme = (bodyClass, btnClass) => {

  body.classList.remove(localStorage.getItem('portfolio-theme'))
  btnTheme.classList.remove(localStorage.getItem('portfolio-btn-theme'))

  addThemeClass(bodyClass, btnClass)

  localStorage.setItem('portfolio-theme', bodyClass)
  localStorage.setItem('portfolio-btn-theme', btnClass)
}

const toggleTheme = () =>
  isDark() ? setTheme('light', 'fa-moon') : setTheme('dark', 'fa-sun')

btnTheme.addEventListener('click', toggleTheme)

const displayList = () => {
  const navUl = document.querySelector('.nav__list')

  if (btnHamburger.classList.contains('fa-bars')) {
    btnHamburger.classList.remove('fa-bars')
    btnHamburger.classList.add('fa-times')
    navUl.classList.add('display-nav-list')
  } else {
    btnHamburger.classList.remove('fa-times')
    btnHamburger.classList.add('fa-bars')
    navUl.classList.remove('display-nav-list')
  }
}

btnHamburger.addEventListener('click', displayList)

const scrollUp = () => {
  const btnScrollTop = document.querySelector('.scroll-top')

  if (
    body.scrollTop > 500 ||
    document.documentElement.scrollTop > 500
  ) {
    btnScrollTop.style.display = 'block'
  } else {
    btnScrollTop.style.display = 'none'
  }
}

document.addEventListener('scroll', scrollUp)

var texts = [
    'Student',
    'Hobbyist',
];

var currentIndex = 0;
var currentText = "";
var isDeleting = false;
var typingSpeed = 200;

function typeText() {
  var typingTextElement = document.getElementById("typing-text");

  if (isDeleting) {
    currentText = texts[currentIndex].substring(0, currentText.length - 1);
    typingSpeed = 70;
  } else {
    currentText = texts[currentIndex].substring(0, currentText.length + 1);
    typingSpeed = 200;
  }

  typingTextElement.textContent = currentText;

  if (!isDeleting && currentText === texts[currentIndex]) {
    isDeleting = true;
    typingSpeed = 1000;
  } else if (isDeleting && currentText === "") {
    isDeleting = false;
    currentIndex++;

    if (currentIndex >= texts.length) {
      currentIndex = 0;
    }

    typingSpeed = 200;
  }

  setTimeout(typeText, typingSpeed);
}

window.onload = typeText;
