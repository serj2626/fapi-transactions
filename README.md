<details>
  <summary>Задачи</summary>

- [X] Подключение к базе данных
- [X] Alembic для миграции
- [X] Создание таблиц: users, tasks, transactions
- [X] Миксин для relationships
- [ ] Авторизация
- [ ] JWT авторизация

</details>

<details>
  <summary>Backend stack</summary>

<ul>
  <li>Python</li>
  <li>FastAPI</li>
  <li>SQLAlchemy</li>
  <li>PostgreSQL</li>
  <li>Asyncpg</li>
  <li>Redis</li>
  <li>Celery</li>
</ul>
</details>

<details>
  <summary>Frontend stack</summary>

<ul>
  <li>Javascript</li>
  <li>Vue</li>
  <li>Axios</li>
  <li>Vue-Router</li>
  <li>VueUse</li>
  <li>Vue-Toast</li>
  <li>Bootstrap</li>
</ul>
</details>

> openssl rsa -in jwt-private.pem -outform PEM -pubout -out jwt-public.pem

> openssl genrsa -out jwt-private.pem 2048