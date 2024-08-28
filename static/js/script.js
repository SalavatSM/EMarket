// Подключение к WebSocket серверу
const socket = new WebSocket('ws://localhost:8000/ws/');

// Обработчик события открытия соединения
socket.onopen = function(event) {
    console.log('Соединение установлено');
};

// Обработчик события получения сообщения
socket.onmessage = function(event) {
    console.log('Получено сообщение:', event.data);
    // Обработать полученное сообщение (например, обновить список пользователей)
};

// Функция для создания пользователя
function createUser() {
    fetch('/create-user/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            // Данные нового пользователя
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Новый пользователь создан:', data);
        // Обновить список пользователей
    })
    .catch(error => {
        console.error('Ошибка при создании пользователя:', error);
    });
}

// Добавление обработчиков событий для кнопок
document.getElementById('create-user').addEventListener('click', createUser);