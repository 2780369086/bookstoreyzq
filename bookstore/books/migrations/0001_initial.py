# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('type_id', models.SmallIntegerField(verbose_name='商品种类', choices=[(1, 'PYTHON'), (2, 'javascript'), (3, '数据结构与算法'), (4, '机器学习'), (5, '操作系统'), (6, '数据库')], default=1)),
                ('name', models.CharField(verbose_name='商品名称', max_length=20)),
                ('desc', models.CharField(verbose_name='商品简介', max_length=128)),
                ('price', models.DecimalField(decimal_places=2, verbose_name='商品价格', max_digits=10)),
                ('unite', models.CharField(verbose_name='商品单位', max_length=20)),
                ('stock', models.IntegerField(verbose_name='商品库存', default=1)),
                ('sales', models.IntegerField(verbose_name='商品销量', default=0)),
                ('detail', tinymce.models.HTMLField(verbose_name='商品详情')),
                ('image', models.ImageField(upload_to='books', verbose_name='商品图片')),
                ('status', models.SmallIntegerField(verbose_name='商品状态', choices=[(0, '下线'), (1, '上线,')], default=1)),
            ],
            options={
                'db_table': 's_books',
            },
        ),
    ]
