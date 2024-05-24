document.addEventListener('DOMContentLoaded', function() {
    let loginForm = document.getElementById('login-form');
    let loginFailed = loginForm.getAttribute('data-login-failed');

    if (loginFailed === 'true') {
        showFailedLogin();
    }

    function showFailedLogin() {
        let failedLoginDiv = document.createElement('div');
        failedLoginDiv.className = 'failed-login';
        failedLoginDiv.innerHTML = '<span style="color: red;">Nombre de usuario o contraseña incorrectos.</span>';
        loginForm.prepend(failedLoginDiv);
    }
});
