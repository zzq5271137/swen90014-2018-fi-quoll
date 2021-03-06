# Generated by Django 2.0.8 on 2018-10-16 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedule', '0009_merge_20180108_2303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('attended', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_email', models.CharField(max_length=100)),
                ('created_time', models.DateTimeField(verbose_name='date added')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('jsa_required', models.BooleanField()),
                ('attendee_required', models.BooleanField()),
                ('customer_sign_required', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='FesClass',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='schedule.Event')),
                ('class_location', models.CharField(max_length=100)),
                ('note', models.CharField(blank=True, max_length=200, null=True)),
                ('comments', models.CharField(blank=True, max_length=200, null=True)),
                ('feedback', models.CharField(blank=True, max_length=200, null=True)),
                ('jsa_committed', models.BooleanField(default=False)),
                ('signed', models.BooleanField(default=False)),
            ],
            bases=('schedule.event',),
        ),
        migrations.CreateModel(
            name='InventoryInteraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taken_date', models.DateTimeField()),
                ('status_at_that_time', models.IntegerField(choices=[(1, 'new'), (2, 'used'), (3, 'exhausted')])),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('item_code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('item_type', models.IntegerField(choices=[(1, 'Water Extinguisher'), (2, 'CO2 Extinguisher'), (3, 'Foam Extinguisher')])),
                ('item_status', models.IntegerField(choices=[(1, 'new'), (2, 'used'), (3, 'exhausted')])),
                ('item_taken', models.DateTimeField(null=True, verbose_name='date taken')),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification_name', models.CharField(max_length=100)),
                ('course_teachable', models.ManyToManyField(to='management_app.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer_first_name', models.CharField(max_length=50)),
                ('trainer_last_name', models.CharField(max_length=50)),
                ('trainer_register_number', models.CharField(max_length=100)),
                ('trainer_email', models.CharField(max_length=100)),
                ('trainer_work_phone', models.CharField(max_length=20)),
                ('trainer_home_phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ClientAddress',
            fields=[
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='address', serialize=False, to='management_app.Client')),
                ('street', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=5)),
                ('postcode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TrainerCalendar',
            fields=[
                ('calendar_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='schedule.Calendar')),
                ('trainer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='calendar', serialize=False, to='management_app.Trainer')),
            ],
            bases=('schedule.calendar',),
        ),
        migrations.AddField(
            model_name='trainer',
            name='trainer_qualification',
            field=models.ManyToManyField(to='management_app.Qualification'),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='taken_trainer',
            field=models.ManyToManyField(through='management_app.InventoryInteraction', to='management_app.Trainer'),
        ),
        migrations.AddField(
            model_name='inventoryinteraction',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_app.InventoryItem'),
        ),
        migrations.AddField(
            model_name='inventoryinteraction',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_app.Trainer'),
        ),
        migrations.AddField(
            model_name='fesclass',
            name='class_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fesclass', to='management_app.Client'),
        ),
        migrations.AddField(
            model_name='fesclass',
            name='class_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fesclass', to='management_app.Course'),
        ),
        migrations.AddField(
            model_name='fesclass',
            name='class_trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fesclass', to='management_app.Trainer'),
        ),
        migrations.AddField(
            model_name='attendee',
            name='class_attend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_app.FesClass'),
        ),
    ]
