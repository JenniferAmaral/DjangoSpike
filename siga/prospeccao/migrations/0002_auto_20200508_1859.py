# Generated by Django 3.0.6 on 2020-05-08 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('prospeccao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DesafioInovacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('aprendizado', models.TextField()),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('servidor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.Servidor')),
            ],
        ),
        migrations.AlterModelOptions(
            name='atendimentoempreendedor',
            options={'verbose_name_plural': 'Atendimentos ao Empreendedor'},
        ),
        migrations.DeleteModel(
            name='DesafiosInovacao',
        ),
    ]