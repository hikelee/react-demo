import datetime

from django.core.management.base import BaseCommand
from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **options):
        from snippets.models import Member
        Member.objects.all().delete()
        f = Faker(locale='zh_CN')
        members = []
        for _ in range(f.random_int(200, 688)):
            birthday = datetime.datetime.now() - datetime.timedelta(seconds=f.random_int(365 * 10*24*3600, 365 * 50*24*3600))
            create_time = datetime.datetime.now() - datetime.timedelta(seconds=f.random_int(0, 360 * 2*24*3600))
            member = Member(
                name=f.name(),
                email=f.ascii_email(),
                website=f.domain_name(),
                balance=round(f.random_int() / 0.99, 2),
                address=f.address(),
                status=f.random_int(1, 2),
                birthday=birthday.date(),
                create_time=create_time,
                signature="".join(f.random_letters(f.random_int(200, 688))),
                single=f.random_element([True, False])
            )
            print(birthday.date(), create_time)
            members.append(member)

        Member.objects.bulk_create(members)
