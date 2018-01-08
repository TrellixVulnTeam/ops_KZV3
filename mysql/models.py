from django.db import models

class script(models.Model):
    TOOL_RUN_TYPE = (
        # (0, 'shell'),
        # (1, 'python'),
        (2, 'sql'),
    )
    ENV_RUN_TYPE = (
        (0, 'dev'),
        (1, 'test'),
        (2, 'stable'),
        (3, 'pre'),
        (4, 'prod'),
    )
    FINISHED_STATE = (
        (0, 'unfinished'),
        (1, 'finished'),
    )
    envr_type = models.IntegerField(choices=ENV_RUN_TYPE, verbose_name="环境类型", default=0)
    name = models.CharField(max_length=255, verbose_name='脚本名称',unique=True)
    tool_script = models.TextField(verbose_name='脚本',null=True, blank=True)
    tool_run_type = models.IntegerField(choices=TOOL_RUN_TYPE, verbose_name='类型', default=0)
    comment = models.TextField(verbose_name='说明', null=True, blank=True)
    ctime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    utime = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_finished = models.IntegerField(choices=FINISHED_STATE, verbose_name='完成时间', max_length=30,  default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "script"
        verbose_name = "脚本"
        verbose_name_plural = verbose_name


