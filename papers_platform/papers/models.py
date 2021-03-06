from django.db import models

from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock


class equationBlock(blocks.StructBlock):
    equation = blocks.TextBlock(required=True)

    class Meta:
        icon = "cogs"
        template = 'papers/blocks/equation_block.html'


class PaperPage(Page):
    link = models.URLField()
    video_id = models.CharField(max_length=32)
    summary = RichTextField(blank=True)

    extensions = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('equation', equationBlock()),
        ('image', ImageChooserBlock()),
    ],null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('link'),
        FieldPanel('video_id'),
        FieldPanel('summary', classname="full"),
        StreamFieldPanel('extensions'),
    ]
