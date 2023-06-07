from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = 'CountAPI'
    redishost: str = 'redis'
    redisport: int = 6379
    redisuser: str = 'default'
    redispassword: str = ''
    redisdb: int = 0

settings = Settings()
