from django.db import models

class PerformanceExperiment(models.Model):
    num_threads = models.IntegerField()
    query_batch_size = models.IntegerField()
    execution_time = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Experiment {self.id} - {self.num_threads} threads, {self.query_batch_size} queries"

