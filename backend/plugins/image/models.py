from typing import Any
from typing import List
from typing import Tuple

from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.files import get_thumbnailer
from enumfields import Enum
from enumfields import EnumField
from filer.fields.image import FilerImageField
from filer.models import ThumbnailOption
from link_all.models import LinkAllMixin


class ImageAlignment(Enum):
    LEFT = 'left'
    RIGHT = 'right'
    CENTER = 'center'


class ImageVerticalSpacing(Enum):
    EXTRA_SMALL = 'extra_small'
    SMALL = 'small'
    NORMAL = 'normal'

    class Labels:
        EXTRA_SMALL = "Extra small (16px)"
        SMALL = "Small (30px)"
        NORMAL = "Normal (60px)"


class ImagePluginModel(CMSPlugin, LinkAllMixin):
    image = FilerImageField(on_delete=models.PROTECT)
    alignment = EnumField(ImageAlignment, default=ImageAlignment.CENTER, max_length=64)
    thumbnail_config = models.ForeignKey(
        ThumbnailOption,
        verbose_name=_("Thumbnail config"),
        blank=True,
        null=True,
        help_text=_(
            "When set the image is going to be cropped / scaled up to the provided dimensions."
        ),
        on_delete=models.PROTECT,
    )
    is_full_screen_on_click = models.BooleanField(
        default=True, verbose_name="Open full screen modal on click"
    )
    vertical_spacing = EnumField(
        ImageVerticalSpacing,
        default=ImageVerticalSpacing.EXTRA_SMALL,
        max_length=32,
        blank=True,
        null=True,
    )
    link_is_optional = True

    def get_alignment_class(self) -> str:
        if self.alignment == ImageAlignment.CENTER:
            return 'align-self-center justify-content-center'
        elif self.alignment == ImageAlignment.LEFT:
            return 'align-self-start justify-content-start'
        elif self.alignment == ImageAlignment.RIGHT:
            return 'align-self-end justify-content-end'

    def copy_relations(self, oldinstance: 'ImagePluginModel'):
        self.image = oldinstance.image
        self.thumbnail_config = oldinstance.thumbnail_config

    def get_image_url(self) -> str:
        if not self.thumbnail_config:
            return self.image.url
        thumbnail_options = {
            'size': (self.thumbnail_config.width, self.thumbnail_config.height),
            'crop': self.thumbnail_config.crop,
            'upscale': self.thumbnail_config.upscale,
            'subject_location': self.image.subject_location,
        }
        thumbnailer = get_thumbnailer(self.image)
        return thumbnailer.get_thumbnail(thumbnail_options).url

    def get_image_source_url(self) -> str:
        return self.image.url

    def get_image_srcset_data(self) -> List[Tuple[int, Any]]:
        thumbnailer = get_thumbnailer(self.image)
        width_breakpoints = [576, 768, 1200]
        srcset: List[Tuple[int, Any]] = []
        for width in filter(lambda x: x < self.get_image_width(), width_breakpoints):
            thumbnail_options = {
                'crop': self.thumbnail_config.crop if self.thumbnail_config else False,
                'size': (width, 0),
            }
            srcset.append((width, thumbnailer.get_thumbnail(thumbnail_options)))
        return srcset

    def get_image_width(self) -> int:
        return self.thumbnail_config.width if self.thumbnail_config else self.image.width

    def __str__(self) -> str:
        return self.image.label if self.image and self.image.label else ''
