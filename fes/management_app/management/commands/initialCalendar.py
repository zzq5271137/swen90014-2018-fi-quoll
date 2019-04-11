try:
    from django.core.management.base import NoArgsCommand as BaseCommand
except ImportError:
    from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Load some sample data into the db"

    def handle(self, **options):
        from schedule.models import Calendar
        from schedule.models import Rule

        print("checking for existing data ...")
        try:
            Calendar.objects.get(name="class_calendar")
            print("It looks like you already have loaded the sample data, quitting.")
            import sys
            sys.exit(1)
        except Calendar.DoesNotExist:
            print("Sample data not found in db.")
            print("Install it...")

        print("Create the class calendar. ")
        class_calendar = Calendar(name="class_calendar", slug="classCalendar")
        class_calendar.save()
        print("The class calendar is created")

        print("Create some common rules. ")
        try:
            rule = Rule.objects.get(name="Daily")
        except Rule.DoesNotExist:
            rule = Rule(frequency="YEARLY", name="Yearly", description="will recur once every Year")
            rule.save()
            print("YEARLY recurrence created")
            rule = Rule(frequency="MONTHLY", name="Monthly", description="will recur once every Month")
            rule.save()
            print("Monthly recurrence created")
            rule = Rule(frequency="WEEKLY", name="Weekly", description="will recur once every Week")
            rule.save()
            print("Weekly recurrence created")
            rule = Rule(frequency="DAILY", name="Daily", description="will recur once every Day")
            rule.save()
            print("Daily recurrence created")
        print("The common rules are installed.")
