from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(verbose_name="姓名", blank=False, max_length=30)


class SampleInfo_forTest(models.Model):
    sample_id = models.CharField(verbose_name="样本ID", max_length=15, primary_key=True,blank=False)
    series = models.CharField(verbose_name="实验系列", max_length=10)
    group = models.CharField(verbose_name="分组", max_length=50)
    cell_tissue_type = models.CharField(verbose_name="细胞/组织类型", max_length=50)
    detail = models.CharField(verbose_name="详细信息", max_length=100, blank=True)
    source = models.CharField(verbose_name="来源", max_length=50)
    medical_condition = models.CharField(verbose_name="医学状态", max_length=20, default="Normal")
    experimental_method = models.CharField(verbose_name="实验方法", max_length=50)

    class Meta():
        verbose_name = "生物样本"
        db_table = "SampleInfo"
        ordering = ["-sample_id"] #默认按照样本的ID倒序排列

