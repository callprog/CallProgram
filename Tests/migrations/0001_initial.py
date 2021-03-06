# Generated by Django 2.0.5 on 2018-05-20 16:09

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('QUESTION_SELECT', 'Question Select'), ('QUESTION_TRANSLATE', 'Question Translate'), ('QUESTION_IRREGULAR_VERB', 'Question with irregular verb'), ('QUESTION_MISSED', 'Question with missed')], help_text='Что это за вопрос : Вопрос-выбор, вопрос-перевод, вопрос с неправильным глаголом или вопрос с пропущенным словом', max_length=28)),
                ('exercise', models.CharField(help_text='Текст задания', max_length=1500)),
                ('variants', models.CharField(blank=True, help_text='Варианты, если множестевенный выбор, варианты через //', max_length=1500)),
                ('answer', models.CharField(help_text='Правильный ответ', max_length=1500)),
            ],
            options={
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='QuestionText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('text', tinymce.models.HTMLField(max_length=14000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Short text for question',
            },
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=1500)),
                ('rule', tinymce.models.HTMLField(max_length=14000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('surname', models.CharField(max_length=150)),
                ('code', models.CharField(max_length=10)),
                ('points', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='StudentAndQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_first_time', models.BooleanField(default=1)),
                ('is_learned', models.BooleanField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tests.Question')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tests.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=1500)),
            ],
            options={
                'verbose_name_plural': 'Themes',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='rule',
            field=models.ForeignKey(blank=True, help_text='Правило, по которому правильный ответ правильный', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Tests.Rule'),
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.ForeignKey(blank=True, help_text='Текст вопроса - должен включать в себя задание!', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Tests.QuestionText'),
        ),
        migrations.AddField(
            model_name='question',
            name='theme',
            field=models.ForeignKey(blank=True, help_text='К какому сборнику вопросов относится', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Tests.Theme'),
        ),
    ]
