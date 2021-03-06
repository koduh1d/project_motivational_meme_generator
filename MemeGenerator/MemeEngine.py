"""Module for MemeEngine."""

from random import randint
from re import I
import textwrap
from typing import AnyStr
from PIL import Image, ImageDraw, ImageFont
import os


class MemeEngine:
    """A meme maker.

    Takes an output directory to use for making memes.
    """

    def __init__(self, output_dir: AnyStr) -> None:
        """Store an output directory."""
        self.output_dir = output_dir

    def make_meme(
                self,
                img_path: AnyStr,
                text: AnyStr,
                author: AnyStr,
                width=500
            ) -> AnyStr:
        """Create a meme.

        Returns: Saved location of meme.
        """
        img = Image.open(img_path)
        height = None
        if width <= 500:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)
        else:
            raise Exception('Incorrect width parameter')
        if None not in (text, author):
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(
                    './MemeGenerator/fonts/arial.ttf',
                    int(width * 0.05)
                )
            x = randint(0, width//2)
            y = randint(0, int(height * 0.75))
            quote = '\"' + text + '\" - ' + author
            quote = textwrap.wrap(quote, width=30)
            for line in quote:
                draw.text((x, y), line, fill='white', font=font)
                y += font.getsize(line)[1]
        else:
            raise Exception('Incorrect text/author parameter')
        try:
            os.mkdir(self.output_dir)
        except Exception:
            pass
        tmp = f'{self.output_dir}/{randint(0,1000000)}.png'
        img.save(tmp)
        return tmp
