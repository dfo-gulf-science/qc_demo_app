from django.db import models
from django.urls import reverse
from django.utils import timezone


#
# class Species(models.Model):
#     code = models.IntegerField(blank=True, null=True, unique=True, verbose_name="code")
#     common_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="English common name")
#     scientific_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Scientific name")
#     tsn = models.IntegerField(blank=True, null=True, verbose_name="ITIS TSN")
#
#     def __str__(self):
#         return self.common_name


class Sample(models.Model):
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    sampler_name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Sample #{self.id}"

    class Meta:
        ordering = ['date']

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("sample-detail", args=[self.pk])

class Observation(models.Model):
    sex_choices = (
        (1, "1-female"),
        (2, "2-male"),
        (9, "9-unknown"),
    )

    maturity_choices = (
        (1, "1-young"),
        (2, "2-old"),
        (2, "3-really old"),
        (9, "9-unknown"),
    )

    sample = models.ForeignKey(Sample, related_name="observations", on_delete=models.CASCADE)
    # species = models.ForeignKey(Species, related_name="fish_details", on_delete=models.CASCADE)
    length = models.FloatField()
    weight = models.FloatField()
    sex = models.IntegerField(choices=sex_choices)
    maturity = models.IntegerField(choices=maturity_choices)
    remarks = models.TextField(null=True, blank=True)
    gonad_weight = models.FloatField(null=True, blank=True)
    parasite = models.NullBooleanField()

    class Meta:
        pass

    def __str__(self):
        return f"fishy #{self.id} [sex={self.get_sex_display()} - length={self.length}mm - weight={self.weight}g]"

    @property
    def length_to_weight_ratio(self):
        return self.length / self.weight

    def get_absolute_url(self):
        return reverse("sample-detail", args=[self.sample.pk])
