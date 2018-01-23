var isNewUser = false;

function onClickNewUser() {
    document.getElementById('confirm-password').style.display = 'block';
    document.getElementById('login').className += 'botao-signUp'
    document.getElementById('newUser').style.display = 'none'
    document.getElementById('login-title').innerHTML = "New User"
    isNewUser = true;
}

function onClickLogin() {

    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    if (isNewUser) {
        var confirm = document.getElementById('confirm-password').value;

        if (confirm != password) {
            alert("Confirmed password not equal!!!");
            return false;
        }
    }
    var hash = sha256.create();
    hash.update(password);

    return login(email, hash.hex());
}

function login(email, password) {
    console.log(email, password);

    $(document).ready(function () {
        $.post("http://localhost:8080/post", {
                name: "Donald Duck",
                city: "Duckburg"
            },
            function (data, status) {
                alert("Data: " + data + "\nStatus: " + status);

                if (data == 'ok') {
                    window.location.href = 'index.html'
                }

            });
    });
}