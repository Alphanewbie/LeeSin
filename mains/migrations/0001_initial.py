# Generated by Django 2.1.15 on 2020-06-30 10:32

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('scale', models.IntegerField()),
                ('location', models.CharField(max_length=60)),
                ('homepage', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CountIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('javascript', models.CharField(max_length=20)),
                ('java', models.CharField(max_length=20)),
                ('python', models.CharField(max_length=20)),
                ('c', models.CharField(max_length=20)),
                ('csharp', models.CharField(max_length=20)),
                ('cplus', models.CharField(max_length=20)),
                ('go', models.CharField(max_length=20)),
                ('ruby', models.CharField(max_length=20)),
                ('typescript', models.CharField(max_length=20)),
                ('php', models.CharField(max_length=20)),
                ('scala', models.CharField(max_length=20)),
                ('rust', models.CharField(max_length=20)),
                ('kotlin', models.CharField(max_length=20)),
                ('swift', models.CharField(max_length=20)),
                ('shell', models.CharField(max_length=20)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CountRepository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('javascript', models.CharField(max_length=20)),
                ('java', models.CharField(max_length=20)),
                ('python', models.CharField(max_length=20)),
                ('c', models.CharField(max_length=20)),
                ('csharp', models.CharField(max_length=20)),
                ('cplus', models.CharField(max_length=20)),
                ('go', models.CharField(max_length=20)),
                ('ruby', models.CharField(max_length=20)),
                ('typescript', models.CharField(max_length=20)),
                ('php', models.CharField(max_length=20)),
                ('scala', models.CharField(max_length=20)),
                ('rust', models.CharField(max_length=20)),
                ('kotlin', models.CharField(max_length=20)),
                ('swift', models.CharField(max_length=20)),
                ('shell', models.CharField(max_length=20)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('carear', models.CharField(max_length=50)),
                ('carear_start', models.IntegerField()),
                ('carear_end', models.IntegerField()),
                ('recruit_page', models.CharField(max_length=200)),
                ('index', models.IntegerField()),
                ('site', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SkillStack',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('img', imagekit.models.fields.ProcessedImageField(default='icon/dummy.png', upload_to='icon')),
                ('detail', models.TextField(null=True)),
                ('stackshareLink', models.CharField(max_length=100, null=True)),
                ('webpage', models.CharField(max_length=50, null=True)),
                ('category', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='recruit',
            name='wants_stacks',
            field=models.ManyToManyField(related_name='wants_stacks', to='mains.SkillStack'),
        ),
        migrations.AddField(
            model_name='company',
            name='posted_recruit',
            field=models.ManyToManyField(related_name='posting_company', to='mains.Recruit'),
        ),
    ]
