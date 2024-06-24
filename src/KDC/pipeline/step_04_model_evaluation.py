import dagshub
import mlflow
from KDC.config.configuration import ConfigurationManager
from KDC.components.model_evaluation_mflow import Evaluation
from KDC import logger



STAGE_NAME = "Model Evaluation Step"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info('04 - Model Evaluation step')
        logger.info(f"{STAGE_NAME} started.")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed.")
            
    except Exception as e:
        logger.exception(e)
        raise e