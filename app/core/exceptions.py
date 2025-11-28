class SemanticFlowException(Exception):
    """Base exception for SemanticFlow"""
    pass

class DocumentProcessingError(SemanticFlowException):
    """Raised when document processing fails"""
    def __init__(self, message: str, job_id: str = None):
        self.job_id = job_id
        super().__init__(f"Processing failed for job {job_id}: {message}" if job_id else message)

class ConfigurationError(SemanticFlowException):
    """Raised when there is a configuration error"""
    pass
