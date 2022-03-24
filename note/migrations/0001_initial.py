# Generated by Django 4.0.3 on 2022-03-21 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('notetype', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Noteitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Notekey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notekey', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notetype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notetype', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PO',
            fields=[
                ('note_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='note.note')),
                ('typ', models.CharField(max_length=10)),
            ],
            bases=('note.note',),
        ),
        migrations.CreateModel(
            name='POItem',
            fields=[
                ('noteitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='note.noteitem')),
                ('typ', models.CharField(max_length=10)),
            ],
            bases=('note.noteitem',),
        ),
        migrations.CreateModel(
            name='Noteitemkey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noteitemkey', models.CharField(max_length=25)),
                ('notekey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notekeys', to='note.notekey')),
            ],
        ),
        migrations.AddField(
            model_name='noteitem',
            name='noteitemkey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='note.noteitemkey'),
        ),
        migrations.AddField(
            model_name='noteitem',
            name='notekey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='note.notekey'),
        ),
        migrations.AddField(
            model_name='noteitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='note.product'),
        ),
        migrations.AddField(
            model_name='note',
            name='notekey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='note.notekey'),
        ),
    ]