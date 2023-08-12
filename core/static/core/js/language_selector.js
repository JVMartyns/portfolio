var userLanguage = localStorage.getItem('userLanguage');
var browserLanguage = navigator.language;

var language = userLanguage || browserLanguage || 'pt-br';

var languageSelector = document.querySelector('#language-selector select');

languageSelector.value = language.toLowerCase();

languageSelector.addEventListener('change', () => {
    var selectedLanguage = languageSelector.value;
    localStorage.setItem('userLanguage', selectedLanguage);
    document.querySelector('html').lang = selectedLanguage;
});
