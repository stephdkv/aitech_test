def get_repository(repository_type):
    if repository_type == 'memory':
        from .memory import MemoryRepository
        return MemoryRepository()
    elif repository_type == 'db':
        from .db import DBRepository
        return DBRepository()
    else:
        raise ValueError(f'Unknown repository : {repository_type}')
