import redis


class RedisDB:
    def __init__(self, host='localhost', port=6379, db=0):
        self.r = redis.Redis(host=host, port=port, db=db)

    def update_user_cache(self, user):
        # Сохраняем хеш и соль в Redis
        self.r.set(f'user:{user.id}:username', user.username)
        self.r.set(f'user:{user.id}:password_hash', user.password_hash)
        self.r.set(f'user:{user.id}:password_salt', user.password_salt)

    def verify_user_password(self, user, password):
        # Проверяем хеш и соль в Redis
        stored_username = self.r.get(f'user:{user.id}:username')
        stored_password_hash = self.r.get(f'user:{user.id}:password_hash')
        stored_password_salt = self.r.get(f'user:{user.id}:password_salt')

        if stored_username and stored_password_hash and stored_password_salt:
            # Если они есть в Redis, используем их для проверки
            return user.username == stored_username.decode('utf-8') and user.check_password(password)
        else:
            # Если их нет в Redis, проверяем в базе данных
            if user.check_password(password):
                # Сохраняем хеш и соль в Redis
                self.update_user_cache(user)
                return True
            else:
                return False
