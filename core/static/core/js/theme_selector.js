var prefersColorScheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
console.log(prefersColorScheme);
var userTheme = localStorage.getItem('userTheme');

var theme = userTheme || prefersColorScheme || 'default';
var themeSelector = document.querySelector('#theme-selector select');
var themeStylesheet = document.querySelector('#theme-stylesheet');
var siteLogo = document.querySelector('#site-logo');

themeSelector.value = theme;
document.cookie = 'current_theme=' + theme;

themeSelector.addEventListener('change', () => {
    var selectedTheme = themeSelector.value;
    localStorage.setItem('userTheme', selectedTheme);
})
