from django.db import migrations, models
import django.db.models.deletion

def create_and_set_userprofile_for_expenses(apps, schema_editor):
    User = apps.get_model('core', 'User')
    UserProfile = apps.get_model('profiles', 'UserProfile')
    Expense = apps.get_model('budget', 'Expense')

    # Ensure the default user exists
    default_user_values = {
        'email': 'default_user@example.com',
        'first_name': 'Default',
        'last_name': 'User',
        'mobile': '1234567890',
        'password': 'default_password',
    }
    user, user_created = User.objects.get_or_create(email=default_user_values['email'], defaults=default_user_values)

    # Create a UserProfile for the default user
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    # Set the user_profile for all existing expenses
    for expense in Expense.objects.all():
        if not expense.user_profile:
            expense.user_profile = user_profile
            expense.save()

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_wallet'),
        ('budget', '0003_expense'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='user_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='profiles.userprofile'),
            preserve_default=False,
        ),
        migrations.RunPython(create_and_set_userprofile_for_expenses, reverse_code=migrations.RunPython.noop),
    ]
