
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

function fillCollor(object) {
    var colorThief = new ColorThief();
    var rgbColor = [0, 0, 0];
    try {
        var img = object.getElementsByTagName('img')[0];
        console.log('Image width:', img.width);
        console.log('Image height:', img.height);
        rgbColor = colorThief.getPalette(img, 2)[0];
        console.log('RGB Color:', rgbColor);
        object.style.background = `rgba(${rgbColor[0]}, ${rgbColor[1]}, ${rgbColor[2]}, 0.3)`;
    } catch (e) {
        console.log(e);
    }

    object.style.background = `rgba(${rgbColor[0]}, ${rgbColor[1]}, ${rgbColor[2]}, 0.3)`;
}

function setFormationImageBackground() {
    $(document).ready(function () {
        $('.formation-image').each(function (_index, element) {
            fillCollor(element);
        });
    });
}

function showContent() {
    let loadSpinnerContainer = document.getElementById('loading-spinner-container');
    let content = document.getElementById('main-content');
    loadSpinnerContainer.style.display = 'none';
    content.style.display = 'block';
}

function imageLoaded() {
    loadedImages++;
    if (loadedImages === imagesToLoad.length) {
        if (document.getElementsByClassName('formation-image').length > 0) {
            setFormationImageBackground();
        }
        showContent();
    }
}

var imagesToLoad = document.querySelectorAll('img');
var loadedImages = 0;

// Adiciona um event listener para o evento "load" em cada imagem
imagesToLoad.forEach(function (image) {
    image.addEventListener('load', imageLoaded);
    if (image.complete) {
        imageLoaded();
    }
});
