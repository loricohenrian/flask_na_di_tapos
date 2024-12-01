document.addEventListener('DOMContentLoaded', function() {
    // Password toggle
    const togglePassword = document.getElementById('togglePassword');
    const passwordInput = document.getElementById('password');
    const passwordIcon = document.getElementById('passwordIcon');

    if (togglePassword && passwordInput && passwordIcon) {
        togglePassword.addEventListener('click', function(e) {
            e.preventDefault(); // Prevent form submission
            const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordInput.setAttribute('type', type);

            // Toggle icon
            if (type === 'text') {
                passwordIcon.classList.replace('fa-eye', 'fa-eye-slash');
            } else {
                passwordIcon.classList.replace('fa-eye-slash', 'fa-eye');
            }
        });
    }

    // Confirm password toggle
    const toggleConfirmPassword = document.getElementById('toggleConfirmPassword');
    const confirmPasswordInput = document.getElementById('confirm_password');
    const confirmPasswordIcon = document.getElementById('confirmPasswordIcon');

    if (toggleConfirmPassword && confirmPasswordInput && confirmPasswordIcon) {
        toggleConfirmPassword.addEventListener('click', function(e) {
            e.preventDefault(); // Prevent form submission
            const type = confirmPasswordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            confirmPasswordInput.setAttribute('type', type);

            // Toggle icon
            if (type === 'text') {
                confirmPasswordIcon.classList.replace('fa-eye', 'fa-eye-slash');
            } else {
                confirmPasswordIcon.classList.replace('fa-eye-slash', 'fa-eye');
            }
        });
    }
});