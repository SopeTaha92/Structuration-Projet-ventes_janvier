


from loguru import logger
from config import LOG_FILE

def logging_file(file : str = LOG_FILE):
    """
    Cette fonction se charge de la mise en place des fichier de logs
    """
    logger.remove()
    logger.add(
        file,
        rotation="10 MB",
        retention="30 days",
        compression='zip',
        level='INFO',
        format="{time} | {level} | {name}:{line} | {message}"
    )

    logger.info('Fichier de logs crée avec succée début du traitement du pipeline')
