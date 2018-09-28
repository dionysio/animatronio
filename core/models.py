import uuid, os
from taggit.managers import TaggableManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from PIL import Image

def save_image(instance, filename):
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid.uuid4().hex, ext)
    # return the whole path to the file
    return filename


class TaggedPicture(models.Model):
    title = models.CharField(_('Title'), max_length=255, unique=True)
    caption = models.TextField(_('Caption'), blank=True, null=True)
    created = models.DateTimeField(_('Date added'), auto_now_add=True, editable=False)
    is_public = models.BooleanField(_('Is photo public'), default=True, help_text=_('Public photographs will be displayed in the default views.'))
    photo = models.ImageField(_('Image'), upload_to=save_image)
    tags = TaggableManager(_('Tags'), blank=True)
    store_link = models.URLField(_('Store link'), null=True, blank=True)

    @property
    def thumb(self):
        return "{}thumb_{}".format(self.photo.storage.base_url, self.photo.name)

    @property
    def tag_names(self):
        return ", ".join(tag.name for tag in self.tags.all())

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        thumb = Image.open(self.photo.file)
        basewidth = 275
        wpercent = (basewidth / float(thumb.size[0]))
        hsize = int((float(thumb.size[1]) * float(wpercent)))
        thumb = thumb.resize((basewidth, hsize), Image.ANTIALIAS)
        thumb.save("{}/thumb_{}".format(self.photo.storage.location, self.photo.name), quality=90)
