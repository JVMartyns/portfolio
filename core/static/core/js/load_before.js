function closeMessage(object) {
    object.parentElement.remove();
}

function refreshCaptcha() {
    $.getJSON("/captcha/refresh/", function (result) {
        $('.captcha').attr('src', result['image_url']);
        $('#id_captcha_0').val(result['key'])
    });
}


function changeColor(object) {
    object.style.fill = 'red';
}


