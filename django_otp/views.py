#!/usr/bin/env python
# coding=utf-8

"""Views."""

from io import BytesIO

from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View

from pyotp.utils import build_uri as build_otp_uri
from qrcode import make as generate_qrcode
from qrcode.image.svg import SvgPathImage as svg


class QRCodeView(View):
    """QRCode view."""

    def get(self, req, secret):
        """GET request."""
        result = bytes()
        with BytesIO() as stream:
            generate_qrcode(
                build_otp_uri(secret), image_factory=svg
            ).save(stream)
            result = stream.getvalue()
        return HttpResponse(
            result, content_type=("image/svg+xml; charset={}").format(
                settings.DEFAULT_CHARSET
            )
        )
