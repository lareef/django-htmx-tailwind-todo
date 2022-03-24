from django.db import models
from model_utils.managers import InheritanceManager

class Todo(models.Model):
    title = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)

class Master(models.Model):
    mname = models.CharField(max_length=255, unique=True, null=False)    

class Doc(models.Model):
    title = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    master = models.ForeignKey(Master, related_name="masters", on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Note(models.Model):
    owner = models.CharField(max_length=2)
    ref = models.CharField(max_length=5)
    
    def __str__(self):
        return self.ref
    
class Notei(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name="%(class)s")
    owner = models.CharField(max_length=2)
    date = models.DateTimeField(auto_now_add=True)
    ref = models.CharField(max_length=5)
    
    objects = InheritanceManager()
    
    def __str__(self):
        return self.ref

class NoteItem(models.Model):
    order = models.SmallIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='%(class)s')
    qty = models.PositiveSmallIntegerField()
    
    class Meta:
        ordering = ('order',)
    
    def __int__(self):
        return self.note
    
class PONote(Notei):
    typ = models.CharField(max_length=2, default="PO")
    
class PONoteItem(NoteItem):
    key = models.ForeignKey(PONote,  on_delete=models.CASCADE, related_name='ponotes')
    typ = models.CharField(max_length=2, default="PO")
    
class PSNote(Notei):
    typ = models.CharField(max_length=2, default="PS")
    
class PSNoteItem(NoteItem):
    key = models.ForeignKey(PSNote,  on_delete=models.CASCADE, related_name='psnotes')
    typ = models.CharField(max_length=2, default="PS")

# class Note(models.Model):
#     owner = models.CharField(max_length=2)
#     ref = models.CharField(max_length=5)
    
#     def __str__(self):
#         return self.ref
    
# class Notei(models.Model):
#     note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name="%(class)s")
#     owner = models.CharField(max_length=2)
#     date = models.DateTimeField(auto_now_add=True)
#     ref = models.CharField(max_length=5)
    
#     class Meta:
#         abstract = True
    
#     def __str__(self):
#         return self.ref

# class NoteItem(models.Model):
#     order = models.SmallIntegerField()
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='%(class)s')
#     qty = models.PositiveSmallIntegerField()
    
#     class Meta:
#         ordering = ('order',)
#         abstract = True
    
#     def __int__(self):
#         return self.note
    
# class PONote(Notei):
#     typ = models.CharField(max_length=2, default="PO")
    
# class PONoteItem(NoteItem):
#     key = models.ForeignKey(PONote,  on_delete=models.CASCADE, related_name='ponotes')
#     typ = models.CharField(max_length=2, default="PO")
    
# class PSNote(Notei):
#     typ = models.CharField(max_length=2, default="PS")
    
# class PSNoteItem(NoteItem):
#     key = models.ForeignKey(PSNote,  on_delete=models.CASCADE, related_name='psnotes')
#     typ = models.CharField(max_length=2, default="PS")