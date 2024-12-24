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
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
    return cookieValue || '';
}

// Handle form submission for registration
function handleRegisterSubmit(event, system) {
    event.preventDefault();
    const formData = new FormData(document.getElementById('registerFormElement'));
    const data = {
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
            document.getElementById('registerFormElement').reset();  // Reset form after successful registration
        } else {
            alert(data.error || 'Registration failed.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred during registration.');
    });
}

// Handle form submission for login
function handleLoginSubmit(event, system) {
    event.preventDefault();
    const formData = new FormData(document.getElementById('loginFormElement'));
    const data = {
        username: formData.get('username'),
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
        window.location.href = '/dashboard/userhome/';  // Redirect to user home page after login
    })
    .catch(error => {
        alert(error.message);
    });
}
