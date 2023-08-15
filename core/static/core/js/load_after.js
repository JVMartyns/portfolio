function toggleMenu() {
    let menuToggle = document.querySelector('.menu-toggle');
    let menuList = document.querySelector('.menu ul');
    menuToggle.classList.toggle('active');
    menuList.classList.toggle('active');

    let isActive = menuList.classList.contains('active');

    if (isActive) {
        menuList.style.display = 'flex';
    } else {
        menuList.style.display = 'none';
    }
}

var imagesToLoad = document.querySelectorAll('img');
var loadedImages = 0;

function imageLoaded() {
    loadedImages++;
    if (loadedImages === imagesToLoad.length) {
        showContent();
    }
}

function showContent() {
    let loadSpinnerContainer = document.getElementById('loading-spinner-container');
    let content = document.getElementById('main-content');
    loadSpinnerContainer.style.display = 'none';
    content.style.display = 'block';
}

// Adiciona um event listener para o evento "load" em cada imagem
imagesToLoad.forEach(function (image) {
    image.addEventListener('load', imageLoaded);

    if (image.complete) {
        imageLoaded();
    }
});
