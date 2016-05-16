from django.db import models


class WorkPosition(models.Model):
    def __str__(self):
        return self.position_name

    position_name = models.CharField(max_length=255)


class RequiredSkills(models.Model):
    def __str__(self):
        return [self.working_position_id, self.skill_name, self.rating, self.rating, self.dichotomy_number]

    working_position_id = models.ForeignKey('WorkPosition', null=True)
    skill_name = models.CharField(max_length=255)
    rating = models.IntegerField()
    dichotomy_number = models.IntegerField(null=True)


class ResultDichotomy(models.Model):
    name = models.CharField(max_length=255)
    pole_1 = models.CharField(max_length=255)
    pole_2 = models.CharField(max_length=255)
    pole_3 = models.CharField(max_length=255)
    pole_4 = models.CharField(max_length=255)


class CalculationResult(models.Model):
    working_position_id = models.ForeignKey('WorkPosition', null=True)
    result_dichotomy_id = models.ForeignKey('ResultDichotomy', null=True)
    generalizing = models.FloatField()
    detailing = models.FloatField()
    participant = models.FloatField()
    observer = models.FloatField()
    object_oriented = models.FloatField()
    connection_oriented = models.FloatField()
    identifying = models.FloatField()
    resultant = models.FloatField()
