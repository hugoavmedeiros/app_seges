# Generated by Django 4.2.4 on 2023-09-06 14:51

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appPainel', '0004_alter_fontesiniciativa_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto_nm', models.CharField(max_length=255, verbose_name='Nome do Produto')),
                ('produto_cd', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Código do Produto')),
            ],
        ),
        migrations.AlterModelOptions(
            name='historicaliniciativa',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical iniciativa', 'verbose_name_plural': 'historical Iniciativas'},
        ),
        migrations.AlterModelOptions(
            name='iniciativa',
            options={'verbose_name_plural': 'Iniciativas'},
        ),
        migrations.CreateModel(
            name='ProdutosIniciativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.CharField(choices=[('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026')], max_length=255, verbose_name='Ano')),
                ('mes', models.CharField(choices=[('1', 'Jan'), ('2', 'Fev'), ('3', 'Mar'), ('4', 'Abr'), ('5', 'Mai'), ('6', 'Jun'), ('7', 'Jul'), ('8', 'Ago'), ('9', 'Set'), ('10', 'Out'), ('11', 'Nov'), ('12', 'Dez')], max_length=255, verbose_name='Ano')),
                ('previsto', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Código da Fonte')),
                ('realizado', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Código da Fonte')),
                ('iniciativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPainel.iniciativa', verbose_name='Nome da Iniciativa')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPainel.produto', verbose_name='Nome do Produto')),
            ],
            options={
                'verbose_name_plural': 'Produtos',
                'ordering': ('iniciativa',),
            },
        ),
        migrations.CreateModel(
            name='HistoricalProdutosIniciativa',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('ano', models.CharField(choices=[('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026')], max_length=255, verbose_name='Ano')),
                ('mes', models.CharField(choices=[('1', 'Jan'), ('2', 'Fev'), ('3', 'Mar'), ('4', 'Abr'), ('5', 'Mai'), ('6', 'Jun'), ('7', 'Jul'), ('8', 'Ago'), ('9', 'Set'), ('10', 'Out'), ('11', 'Nov'), ('12', 'Dez')], max_length=255, verbose_name='Ano')),
                ('previsto', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Código da Fonte')),
                ('realizado', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Código da Fonte')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('iniciativa', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='appPainel.iniciativa', verbose_name='Nome da Iniciativa')),
                ('produto', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='appPainel.produto', verbose_name='Nome do Produto')),
            ],
            options={
                'verbose_name': 'historical produtos iniciativa',
                'verbose_name_plural': 'historical Produtos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalProduto',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('produto_nm', models.CharField(max_length=255, verbose_name='Nome do Produto')),
                ('produto_cd', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Código do Produto')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical produto',
                'verbose_name_plural': 'historical produtos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
