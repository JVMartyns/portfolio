function toggleMenu() {
    let menuToggle = document.querySelector('.menu-toggle');
    let menu = document.querySelector('.menu ul');
    menuToggle.classList.toggle('active');
    menu.classList.toggle('active');

    let isActive = menu.classList.contains('active');

    if (isActive) {
        menu.style.display = 'flex';
    } else {
        menu.style.display = 'none';
    }
}

var imagesToLoad = document.querySelectorAll('.project-cover-image');
var loadedImages = 0;

function imageLoaded() {
    loadedImages++;
    console.log(loadedImages);
    if (loadedImages === imagesToLoad.length) {
        showContent();
    }
}

function showContent() {
    let loadSpinnerContainer = document.getElementById('loading-spinner-container');
    let ProjectsSection = document.getElementById('projects-section');
    loadSpinnerContainer.style.display = 'none';
    ProjectsSection.style.display = 'block';
}
