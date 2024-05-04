let links            = document.querySelectorAll('.header-list-item__link');
let linksContent     = [];
let burger           = document.querySelector('.burger-menu');
let nav              = document.querySelector('.header__nav');
let body             = document.querySelector('body');
let products         = document.querySelectorAll('.product');

// Задание адаптивного размера шрифта для бургер-меню
function checkBurgerFont() {
  if (window.innerWidth < 768) {
    links.forEach(link => linksContent.push(link.textContent.length));
    let longestWord = Math.max(...linksContent);
    links.forEach(link => link.style.fontSize = String(window.innerWidth / longestWord + 7) + 'px');
  } else {
    links.forEach(link => link.style.fontSize = 'var(--main-font-size)');
  }
  linksContent = [];
};
checkBurgerFont();

// События изменения размера окна
window.addEventListener('resize', () => {
  checkBurgerFont();
});

// Функция переключения бургер-меню
function toggleActive() {
  burger.classList.toggle('active');
  nav.classList.toggle('active');
  body.classList.toggle('active');
}

// Прослушка бургер-меню
burger.addEventListener('click', toggleActive);
links.forEach(link => link.addEventListener('click', toggleActive));

// Карусель
$('.products-list').slick({
  dots: false,
  infinite: true,
  speed: 400,
  slidesToShow: 3,
  slidesToScroll: 3,
  responsive: [
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2,
        arrows: false
      }
    }
  ]
});