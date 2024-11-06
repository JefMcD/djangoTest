
# Standard
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

import re
import uuid
import time

# Authentication
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Database
from datetime import datetime
from django.db import IntegrityError, DatabaseError
from .models import *

# Javascript API
import json
from django.http import JsonResponse

# File Handling
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import SuspiciousFileOperation
import os

# Image Handling
from PIL import Image, ImageColor
from io import BytesIO


from django.core.files import File
from django.core.files.images import ImageFile

# Create your views here.


def index(request):
    return render(request, "boiler_app/index.html")