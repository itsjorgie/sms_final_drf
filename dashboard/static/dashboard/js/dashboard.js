   // Show the selected section
   function showSection(sectionId) {
    const sections = ['registerForm', 'loginForm'];
    sections.forEach(function(section) {
        document.getElementById(section).style.display = 'none';
    });
    document.getElementById(sectionId).style.display = 'block';
}

// Fetch CSRF token
function getCsrfToken() {
    const cookieValue = document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))?.split('=')[1];
    return cookieValue || '';
}

// Handle form submission for registration
function handleRegisterSubmit(event, system) {
    event.preventDefault();
    const formData = new FormData(document.getElementById('registerFormElement'));
    const data = {
        email: formData.get('email'),
        username: formData.get('username'),
        password: formData.get('password'),
        confirm_password: formData.get('confirm_password')
    };

    if (data.password !== data.confirm_password) {
        alert('Passwords do not match!');
        return;
    }

    const registerUrl = system === 'system1'
        ? 'http://127.0.0.1:8001/api/system1/register/'
        : 'http://127.0.0.1:8002/api/system2/register/';

    fetch(registerUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken()
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert(data.message);
            showSection('loginForm');
            document.getElementById('registerFormElement').reset();
        } else {
            alert(data.error || 'Registration failed.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred during registration.');
    });
}

// Handle form submission for login with username instead of email
function handleLoginSubmit(event, system) {
    event.preventDefault();
    const formData = new FormData(document.getElementById('loginFormElement'));
    const data = {
        username: formData.get('username'),  // Using username instead of email
        password: formData.get('password')
    };

    const loginUrl = system === 'system1'
        ? 'http://127.0.0.1:8001/api/system1/login/'
        : 'http://127.0.0.1:8002/api/system2/login/';

    fetch(loginUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken()
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            return response.json().then(data => {
                throw new Error(data.error || 'Login failed');
            });
        }
    })
    .then(data => {
        localStorage.setItem('access_token', data.access);
        window.location.href = '/dashboard/send_message/';
    })
    .catch(error => {
        alert(error.message);
    });
}

// Toggle password visibility
function togglePasswordVisibility(inputId, toggleId) {
    const input = document.getElementById(inputId);
    const toggle = document.getElementById(toggleId);
    if (input.type === 'password') {
        input.type = 'text';
        toggle.classList.remove('fa-eye');
        toggle.classList.add('fa-eye-slash');
    } else {
        input.type = 'password';
        toggle.classList.remove('fa-eye-slash');
        toggle.classList.add('fa-eye');
    }
}
