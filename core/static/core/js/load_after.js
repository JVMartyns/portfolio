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

function fillCollor(object) {
    var colorThief = new ColorThief();
    var rgbColor = [0, 0, 0];
    try {
        var img = object.getElementsByTagName('img')[0];
        img.crossOrigin = 'anonymous';

        img.onload = function () {
            rgbColor = colorThief.getPalette(img, 2)[0];
            object.style.background = `rgba(${rgbColor[0]}, ${rgbColor[1]}, ${rgbColor[2]}, 0.3)`;
        };
    } catch (e) {
        console.log(e);
    }

    object.style.background = `rgba(${rgbColor[0]}, ${rgbColor[1]}, ${rgbColor[2]}, 0.3)`;
}

// Adiciona um event listener para o evento "load" em cada imagem
imagesToLoad.forEach(function (image) {
    image.addEventListener('load', imageLoaded);
    if (image.complete) {
        imageLoaded();
    }
});

$(document).ready(function () {
    $('.formation-image').each(function (_index, element) {
        fillCollor(element);
    });
});
