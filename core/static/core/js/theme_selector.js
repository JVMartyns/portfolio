var prefersColorScheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
console.log(prefersColorScheme);
var userTheme = localStorage.getItem('userTheme');

var theme = userTheme || prefersColorScheme || 'default';
var themeSelector = document.querySelector('#theme-selector select');
var themeStylesheet = document.querySelector('#theme-stylesheet');

themeSelector.value = theme;
document.cookie = 'current_theme=' + theme;

if (!themeStylesheet.href.includes(theme)) {
    themeSelector.dispatchEvent(new Event('change'));
}

themeSelector.addEventListener('change', () => {
    var selectedTheme = themeSelector.value;
    localStorage.setItem('userTheme', selectedTheme);
})
