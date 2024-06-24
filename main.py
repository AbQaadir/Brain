from src.KDC.pipeline.step_01_data_ingestion import DataIngestionTrainingPipeline
from src.KDC.pipeline.step_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.KDC.pipeline.step_03_model_training import ModelTrainingPipeline
from src.KDC import logger

STAGE_NAME = "01 - Data Ingestion step"

try:
    logger.info(f"Data Ingestion Pipeline started")
    logger.info(f"{STAGE_NAME} started.")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed.")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "02 - Prepare Base Model"

try:
    logger.info(f"Prepare Base Model Pipeline started")
    logger.info(f"{STAGE_NAME} started.")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed.")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "03 - Model Training"

try:
    logger.info(f"Model Training Pipeline started")
    logger.info(f"{STAGE_NAME} started.")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed.")
except Exception as e:
    logger.exception(e)
    raise e
