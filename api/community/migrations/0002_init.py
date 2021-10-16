# Generated by Django 3.2 on 2021-10-16 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('community', '0001_init'),
        ('users', '0001_init'),
    ]

    operations = [
        migrations.AddField(
            model_name='reaction',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='users.profile'),
        ),
        migrations.AddField(
            model_name='reaction',
            name='feed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='community.feed'),
        ),
        migrations.AddField(
            model_name='link',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_links', to='users.profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='users.profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='feed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='community.feed'),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_comments', to='community.comment'),
        ),
    ]