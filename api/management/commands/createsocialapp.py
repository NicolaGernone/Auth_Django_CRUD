# File: myapp/management/commands/createsocialapp.py

import os
from django.core.management.base import BaseCommand
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site


class Command(BaseCommand):
    help = "Creates a new SocialApp instance"

    def handle(self, *args, **kwargs):
        provider = os.environ.get("PROVIDER")
        name = os.environ.get("APP_NAME")
        client_id = os.environ.get("CLIENT_ID")
        secret = os.environ.get("SECRET_KEY")
        key = os.environ.get("KEY")

        app = SocialApp.objects.create(
            provider=provider, name=name, client_id=client_id, secret=secret, key=key
        )

        for site in Site.objects.all():
            app.sites.add(site)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created SocialApp for {provider}")
        )
