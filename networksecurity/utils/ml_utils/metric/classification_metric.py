from networksecurity.entity.artifact_entity import ClassificationMetricsArtifact
from networksecurity.exception.exception import NetworkSecurityException
from sklearn.metrics import f1_score , precision_score, recall_score, accuracy_score
import sys


def get_classification_score(y_true, y_pred) -> ClassificationMetricsArtifact:
    """
    It takes in the true labels and predicted labels, and returns a ClassificationMetricsArtifact object
    containing the f1 score, precision score, recall score, and accuracy score."""
    try:
        model_f1_score = f1_score(y_true, y_pred)
        model_recall_score = recall_score(y_true, y_pred)
        model_precision_score = precision_score(y_true, y_pred)
        model_accuracy_score = accuracy_score(y_true, y_pred)
        
        classification_mrtric = ClassificationMetricsArtifact(f1_score=model_f1_score,
                                                              precision_score=model_precision_score,
                                                              recall_score=model_recall_score,
                                                              accuracy_score=model_accuracy_score)
        return classification_mrtric
    except Exception as e:
        raise NetworkSecurityException(e, sys)