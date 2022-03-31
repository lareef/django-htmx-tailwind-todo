# Generated by Django 4.0.3 on 2022-03-31 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0010_alter_note_notetype_alter_noteitem_notetypekey'),
    ]

    operations = [
        migrations.CreateModel(
            name='CO',
            fields=[
                ('note_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='note.note')),
                ('typ', models.CharField(max_length=10)),
            ],
            bases=('note.note',),
        ),
        migrations.CreateModel(
            name='COItem',
            fields=[
                ('noteitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='note.noteitem')),
                ('typ', models.CharField(max_length=10)),
            ],
            bases=('note.noteitem',),
        ),
        migrations.CreateModel(
            name='WO',
            fields=[
                ('note_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='note.note')),
                ('typ', models.CharField(max_length=10)),
            ],
            bases=('note.note',),
        ),
        migrations.CreateModel(
            name='WOItem',
            fields=[
                ('noteitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='note.noteitem')),
                ('typ', models.CharField(max_length=10)),
            ],
            bases=('note.noteitem',),
        ),
    ]
