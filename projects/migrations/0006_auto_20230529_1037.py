# Generated by Django 3.1.1 on 2023-05-29 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_profile_social_twitter'),
        ('projects', '0005_project_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='review',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('owner', 'project')},
        ),
    ]
