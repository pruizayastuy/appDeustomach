document.addEventListener('DOMContentLoaded', function() {
    let signupForm = document.getElementById('signup-form');
    let signupFailed = signupForm.getAttribute('data-signup-failed');

    if (signupFailed === 'true') {
        showFailedSignup();
    }

    function showFailedSignup() {
        let failedSignupDiv = document.createElement('div');
        failedSignupDiv.className = 'failed-signup';
        failedSignupDiv.innerHTML = '<span style="color: red;">El registro ha fallado. Por favor, revisa tus datos e intenta nuevamente.</span>';
        signupForm.prepend(failedSignupDiv);
    }
});
