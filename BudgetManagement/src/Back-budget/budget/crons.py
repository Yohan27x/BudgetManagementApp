from django_cron import CronJobBase, Schedule
from datetime import datetime
from profiles.models import Wallet

class ResetMonthlyBudget(CronJobBase):
    RUN_EVERY_MINS = 24 * 60  # every day

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'budget.reset_monthly_budget'    # a unique code

    def do(self):
        today = datetime.today()
        # Check if today is the first day of the month
        if today.day == 1:
            # Reset or allocate budget for all wallets
            for wallet in Wallet.objects.all():
                wallet.balance = wallet.monthly_budget
                wallet.save()
