# Generated by Django 4.0.4 on 2022-06-10 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=100, null=True, unique=True, verbose_name='email')),
                ('campus', models.CharField(choices=[('Akpugo', 'Akpugo'), ('Elele', 'Elele'), ('Okija', 'Okija'), ('National', 'National'), ('None', 'None')], max_length=100000, verbose_name='campus')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=100, verbose_name='first name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus', models.CharField(max_length=10000, verbose_name='Name')),
                ('location', models.CharField(blank=True, max_length=10000, null=True, verbose_name='Location')),
                ('history', models.TextField(blank=True, max_length=10000, null=True, verbose_name='Brief History')),
                ('numerical_strength', models.IntegerField(blank=True, null=True, verbose_name='number of members')),
                ('phone_num', models.CharField(blank=True, max_length=10000, null=True, verbose_name='Phone number')),
                ('account_num', models.CharField(blank=True, max_length=10000, null=True, verbose_name='Account number')),
                ('account_bank', models.CharField(blank=True, max_length=10000, null=True, verbose_name='Account Bank')),
                ('date_created', models.DateField(blank=True, null=True, verbose_name='The date the Choir was Created')),
            ],
            options={
                'verbose_name': 'Campus',
                'verbose_name_plural': 'Campuses',
            },
        ),
        migrations.CreateModel(
            name='Position_Akpugo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus', models.CharField(default='Akpugo', editable=False, max_length=100000)),
                ('pos', models.CharField(help_text='Enter the position in full', max_length=10000, verbose_name='Position')),
            ],
            options={
                'verbose_name': 'Position (Akpugo)',
                'verbose_name_plural': 'Position (Akpugo)',
            },
        ),
        migrations.CreateModel(
            name='Position_Elele',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus', models.CharField(default='Elele', editable=False, max_length=100000)),
                ('pos', models.CharField(help_text='Enter the position in full', max_length=10000, verbose_name='Position')),
            ],
            options={
                'verbose_name': 'Position (Elele)',
                'verbose_name_plural': 'Position (Elele)',
            },
        ),
        migrations.CreateModel(
            name='Position_National',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus', models.CharField(default='National', editable=False, max_length=100000)),
                ('pos', models.CharField(help_text='Enter the position in full', max_length=100000, verbose_name='Position')),
            ],
            options={
                'verbose_name': 'Position (National)',
                'verbose_name_plural': 'Position (National)',
            },
        ),
        migrations.CreateModel(
            name='Position_Okija',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus', models.CharField(default='Okija', editable=False, max_length=100000)),
                ('pos', models.CharField(help_text='Enter the position in full', max_length=100000, verbose_name='Position')),
            ],
            options={
                'verbose_name': 'Position (Okija)',
                'verbose_name_plural': 'Position (Okija)',
            },
        ),
        migrations.CreateModel(
            name='Profile_Okija',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default.jpg', upload_to='profile_pics')),
                ('firstname', models.CharField(max_length=10000, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=10000, verbose_name='Last Name')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10000, verbose_name='Gender')),
                ('phone_num', models.CharField(blank=True, max_length=10000, verbose_name='Phone number')),
                ('department', models.CharField(default='none', max_length=10000, verbose_name='Department')),
                ('part', models.CharField(choices=[('Soprano', 'Soprano'), ('Alto', 'Alto'), ('Tenor', 'Tenor'), ('Bass', 'Bass'), ('None', 'None')], help_text='The part of the person', max_length=100)),
                ('campus', models.CharField(choices=[('Okija', 'Okija'), ('None', 'None')], default='Okija', max_length=100000)),
                ('state', models.CharField(blank=True, choices=[('Abia State', 'Abia State'), ('Adamawa State', 'Adamawa State'), ('Akwa Ibom State', 'Akwa Ibom State'), ('Anambra State', 'Anambra State'), ('Bauchi State', 'Bauchi State'), ('Bayelsa State', 'Bayelsa State'), ('Benue State', 'Benue State'), ('Borno State', 'Borno State'), ('Cross River State', 'Cross River State'), ('Delta State', 'Delta State'), ('Ebonyi State', 'Ebonyi State'), ('Edo State', 'Edo State'), ('Ekiti State', 'Ekiti State'), ('Enugu State', 'Enugu State'), ('Gombe State', 'Gombe State'), ('Imo State', 'Imo State'), ('Jigawa State', 'Jigawa State'), ('Kaduna State', 'Kaduna State'), ('Kano State', 'Kano State'), ('Kebbi State', 'Kebbi State'), ('Kogi State', 'Kogi State'), ('Kwara State', 'Kwara State'), ('Lagos State', 'Lagos State'), ('Nasarawa State', 'Nasarawa State'), ('Niger State', 'Niger State'), ('Ogun State', 'Ogun State'), ('Ondo State', 'Ondo State'), ('Osun State', 'Osun State'), ('Oyo State', 'Oyo State'), ('Plateau State', 'Plateau State'), ('Rivers State', 'Rivers State'), ('Sokoto State', 'Sokoto State'), ('Taraba State', 'Taraba State'), ('Yobe State', 'Yobe State'), ('Zamfara State', 'Zamfara State')], max_length=10000, verbose_name='State')),
                ('marital_status', models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Religious', 'Religious')], max_length=10000, verbose_name='Marital Status')),
                ('birthday', models.DateField(blank=True, default='1999-01-01', null=True, verbose_name='Birth Day')),
                ('joindate', models.DateField(blank=True, default='1999-01-01', null=True, verbose_name='Join Date')),
                ('graduatedate', models.DateField(blank=True, default='1999-01-01', null=True, verbose_name='Graduate Date')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile (Okija)',
                'verbose_name_plural': 'Profile (Okija)',
            },
        ),
        migrations.CreateModel(
            name='Profile_National',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default.jpg', upload_to='profile_pics')),
                ('firstname', models.CharField(max_length=10000, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=10000, verbose_name='Last Name')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10000, verbose_name='Gender')),
                ('phone_num', models.CharField(blank=True, max_length=10000, verbose_name='Phone number')),
                ('department', models.CharField(default='none', max_length=10000, verbose_name='Department')),
                ('part', models.CharField(choices=[('Soprano', 'Soprano'), ('Alto', 'Alto'), ('Tenor', 'Tenor'), ('Bass', 'Bass'), ('None', 'None')], help_text='The part of the person', max_length=100)),
                ('campus', models.CharField(choices=[('National', 'National'), ('None', 'None')], default='National', max_length=100000)),
                ('state', models.CharField(blank=True, choices=[('Abia State', 'Abia State'), ('Adamawa State', 'Adamawa State'), ('Akwa Ibom State', 'Akwa Ibom State'), ('Anambra State', 'Anambra State'), ('Bauchi State', 'Bauchi State'), ('Bayelsa State', 'Bayelsa State'), ('Benue State', 'Benue State'), ('Borno State', 'Borno State'), ('Cross River State', 'Cross River State'), ('Delta State', 'Delta State'), ('Ebonyi State', 'Ebonyi State'), ('Edo State', 'Edo State'), ('Ekiti State', 'Ekiti State'), ('Enugu State', 'Enugu State'), ('Gombe State', 'Gombe State'), ('Imo State', 'Imo State'), ('Jigawa State', 'Jigawa State'), ('Kaduna State', 'Kaduna State'), ('Kano State', 'Kano State'), ('Kebbi State', 'Kebbi State'), ('Kogi State', 'Kogi State'), ('Kwara State', 'Kwara State'), ('Lagos State', 'Lagos State'), ('Nasarawa State', 'Nasarawa State'), ('Niger State', 'Niger State'), ('Ogun State', 'Ogun State'), ('Ondo State', 'Ondo State'), ('Osun State', 'Osun State'), ('Oyo State', 'Oyo State'), ('Plateau State', 'Plateau State'), ('Rivers State', 'Rivers State'), ('Sokoto State', 'Sokoto State'), ('Taraba State', 'Taraba State'), ('Yobe State', 'Yobe State'), ('Zamfara State', 'Zamfara State')], max_length=10000, verbose_name='State')),
                ('marital_status', models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Religious', 'Religious')], max_length=10000, verbose_name='Marital Status')),
                ('birthday', models.DateField(blank=True, default='1999-01-01', null=True, verbose_name='Birth Day')),
                ('joindate', models.DateField(blank=True, default='1999-01-01', null=True, verbose_name='Join Date')),
                ('graduatedate', models.DateField(blank=True, default='1999-01-01', null=True, verbose_name='Graduate Date')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile (National)',
                'verbose_name_plural': 'Profile (National)',
            },
        ),
        migrations.CreateModel(
            name='Profile_Elele',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default.jpg', upload_to='profile_pics')),
                ('firstname', models.CharField(max_length=10000, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=10000, verbose_name='Last Name')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10000, verbose_name='Gender')),
                ('phone_num', models.CharField(blank=True, max_length=10000, verbose_name='Phone number')),
                ('department', models.CharField(default='none', max_length=10000, verbose_name='Department')),
                ('part', models.CharField(choices=[('Soprano', 'Soprano'), ('Alto', 'Alto'), ('Tenor', 'Tenor'), ('Bass', 'Bass'), ('None', 'None')], help_text='The part of the person', max_length=100)),
                ('campus', models.CharField(choices=[('Elele', 'Elele'), ('None', 'None')], default='Elele', max_length=100000)),
                ('state', models.CharField(blank=True, choices=[('Abia State', 'Abia State'), ('Adamawa State', 'Adamawa State'), ('Akwa Ibom State', 'Akwa Ibom State'), ('Anambra State', 'Anambra State'), ('Bauchi State', 'Bauchi State'), ('Bayelsa State', 'Bayelsa State'), ('Benue State', 'Benue State'), ('Borno State', 'Borno State'), ('Cross River State', 'Cross River State'), ('Delta State', 'Delta State'), ('Ebonyi State', 'Ebonyi State'), ('Edo State', 'Edo State'), ('Ekiti State', 'Ekiti State'), ('Enugu State', 'Enugu State'), ('Gombe State', 'Gombe State'), ('Imo State', 'Imo State'), ('Jigawa State', 'Jigawa State'), ('Kaduna State', 'Kaduna State'), ('Kano State', 'Kano State'), ('Kebbi State', 'Kebbi State'), ('Kogi State', 'Kogi State'), ('Kwara State', 'Kwara State'), ('Lagos State', 'Lagos State'), ('Nasarawa State', 'Nasarawa State'), ('Niger State', 'Niger State'), ('Ogun State', 'Ogun State'), ('Ondo State', 'Ondo State'), ('Osun State', 'Osun State'), ('Oyo State', 'Oyo State'), ('Plateau State', 'Plateau State'), ('Rivers State', 'Rivers State'), ('Sokoto State', 'Sokoto State'), ('Taraba State', 'Taraba State'), ('Yobe State', 'Yobe State'), ('Zamfara State', 'Zamfara State')], max_length=10000, verbose_name='State')),
                ('marital_status', models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Religious', 'Religious')], max_length=10000, verbose_name='Marital Status')),
                ('birthday', models.DateField(blank=True, default='1999-01-01', null=True, verbose_name='Birth Day')),
                ('joindate', models.DateField(blank=True, default='1999-01-01', null=True, verbose_name='Join Date')),
                ('graduatedate', models.DateField(blank=True, default='1999-01-01', null=True, verbose_name='Graduate Date')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile (Elele)',
                'verbose_name_plural': 'Profile (Elele)',
            },
        ),
        migrations.CreateModel(
            name='Profile_Akpugo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default.jpg', upload_to='profile_pics')),
                ('firstname', models.CharField(max_length=10000, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=10000, verbose_name='Last Name')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10000, verbose_name='Gender')),
                ('phone_num', models.CharField(blank=True, max_length=10000, verbose_name='Phone number')),
                ('department', models.CharField(default='none', max_length=10000, verbose_name='Department')),
                ('part', models.CharField(choices=[('Soprano', 'Soprano'), ('Alto', 'Alto'), ('Tenor', 'Tenor'), ('Bass', 'Bass'), ('None', 'None')], help_text='The part of the person', max_length=100)),
                ('campus', models.CharField(choices=[('Akpugo', 'Akpugo'), ('None', 'None')], default='Akpugo', max_length=100000)),
                ('state', models.CharField(blank=True, choices=[('Abia State', 'Abia State'), ('Adamawa State', 'Adamawa State'), ('Akwa Ibom State', 'Akwa Ibom State'), ('Anambra State', 'Anambra State'), ('Bauchi State', 'Bauchi State'), ('Bayelsa State', 'Bayelsa State'), ('Benue State', 'Benue State'), ('Borno State', 'Borno State'), ('Cross River State', 'Cross River State'), ('Delta State', 'Delta State'), ('Ebonyi State', 'Ebonyi State'), ('Edo State', 'Edo State'), ('Ekiti State', 'Ekiti State'), ('Enugu State', 'Enugu State'), ('Gombe State', 'Gombe State'), ('Imo State', 'Imo State'), ('Jigawa State', 'Jigawa State'), ('Kaduna State', 'Kaduna State'), ('Kano State', 'Kano State'), ('Kebbi State', 'Kebbi State'), ('Kogi State', 'Kogi State'), ('Kwara State', 'Kwara State'), ('Lagos State', 'Lagos State'), ('Nasarawa State', 'Nasarawa State'), ('Niger State', 'Niger State'), ('Ogun State', 'Ogun State'), ('Ondo State', 'Ondo State'), ('Osun State', 'Osun State'), ('Oyo State', 'Oyo State'), ('Plateau State', 'Plateau State'), ('Rivers State', 'Rivers State'), ('Sokoto State', 'Sokoto State'), ('Taraba State', 'Taraba State'), ('Yobe State', 'Yobe State'), ('Zamfara State', 'Zamfara State')], max_length=10000, verbose_name='State')),
                ('marital_status', models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Religious', 'Religious')], max_length=10000, verbose_name='Marital Status')),
                ('birthday', models.DateField(blank=True, default='1999-01-01', null=True, verbose_name='Birth Day')),
                ('joindate', models.DateField(blank=True, default='1999-01-01', null=True, verbose_name='Join Date')),
                ('graduatedate', models.DateField(blank=True, default='1999-01-01', null=True, verbose_name='Graduate Date')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile (Akpugo)',
                'verbose_name_plural': 'Profile (Akpugo)',
            },
        ),
        migrations.CreateModel(
            name='Executive_Okija',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(blank=True, choices=[('1999/2000', '1999/2000'), ('2000/2001', '2000/2001'), ('2001/2002', '2001/2002'), ('2002/2003', '2002/2003'), ('2003/2004', '2003/2004'), ('2004/2005', '2004/2005'), ('2005/2006', '2005/2006'), ('2006/2007', '2006/2007'), ('2007/2008', '2007/2008'), ('2008/2009', '2008/2009'), ('2009/2010', '2009/2010'), ('2010/2011', '2010/2011'), ('2011/2012', '2011/2012'), ('2012/2013', '2012/2013'), ('2013/2014', '2013/2014'), ('2014/2015', '2014/2015'), ('2015/2016', '2015/2016'), ('2016/2017', '2016/2017'), ('2017/2018', '2017/2018'), ('2018/2019', '2018/2019'), ('2019/2020', '2019/2020'), ('2020/2021', '2020/2021'), ('2021/2022', '2021/2022'), ('2022/2023', '2022/2023')], max_length=10000, verbose_name='Session')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_okija', to=settings.AUTH_USER_MODEL)),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='position_okija', to='account.position_okija')),
            ],
            options={
                'verbose_name': 'Executive (Okija)',
                'verbose_name_plural': 'Executives (Okija)',
            },
        ),
        migrations.CreateModel(
            name='Executive_National',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(blank=True, choices=[('1999/2000', '1999/2000'), ('2000/2001', '2000/2001'), ('2001/2002', '2001/2002'), ('2002/2003', '2002/2003'), ('2003/2004', '2003/2004'), ('2004/2005', '2004/2005'), ('2005/2006', '2005/2006'), ('2006/2007', '2006/2007'), ('2007/2008', '2007/2008'), ('2008/2009', '2008/2009'), ('2009/2010', '2009/2010'), ('2010/2011', '2010/2011'), ('2011/2012', '2011/2012'), ('2012/2013', '2012/2013'), ('2013/2014', '2013/2014'), ('2014/2015', '2014/2015'), ('2015/2016', '2015/2016'), ('2016/2017', '2016/2017'), ('2017/2018', '2017/2018'), ('2018/2019', '2018/2019'), ('2019/2020', '2019/2020'), ('2020/2021', '2020/2021'), ('2021/2022', '2021/2022'), ('2022/2023', '2022/2023')], max_length=10000, verbose_name='Session')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_national', to=settings.AUTH_USER_MODEL)),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='position_national', to='account.position_national')),
            ],
            options={
                'verbose_name': 'Executive (National)',
                'verbose_name_plural': 'Executives (National)',
            },
        ),
        migrations.CreateModel(
            name='Executive_Elele',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(blank=True, choices=[('1999/2000', '1999/2000'), ('2000/2001', '2000/2001'), ('2001/2002', '2001/2002'), ('2002/2003', '2002/2003'), ('2003/2004', '2003/2004'), ('2004/2005', '2004/2005'), ('2005/2006', '2005/2006'), ('2006/2007', '2006/2007'), ('2007/2008', '2007/2008'), ('2008/2009', '2008/2009'), ('2009/2010', '2009/2010'), ('2010/2011', '2010/2011'), ('2011/2012', '2011/2012'), ('2012/2013', '2012/2013'), ('2013/2014', '2013/2014'), ('2014/2015', '2014/2015'), ('2015/2016', '2015/2016'), ('2016/2017', '2016/2017'), ('2017/2018', '2017/2018'), ('2018/2019', '2018/2019'), ('2019/2020', '2019/2020'), ('2020/2021', '2020/2021'), ('2021/2022', '2021/2022'), ('2022/2023', '2022/2023')], max_length=10000, verbose_name='Session')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_elele', to=settings.AUTH_USER_MODEL)),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='position_elele', to='account.position_elele')),
            ],
            options={
                'verbose_name': 'Executive (Elele)',
                'verbose_name_plural': 'Executives (Elele)',
            },
        ),
        migrations.CreateModel(
            name='Executive_Akpugo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(blank=True, choices=[('1999/2000', '1999/2000'), ('2000/2001', '2000/2001'), ('2001/2002', '2001/2002'), ('2002/2003', '2002/2003'), ('2003/2004', '2003/2004'), ('2004/2005', '2004/2005'), ('2005/2006', '2005/2006'), ('2006/2007', '2006/2007'), ('2007/2008', '2007/2008'), ('2008/2009', '2008/2009'), ('2009/2010', '2009/2010'), ('2010/2011', '2010/2011'), ('2011/2012', '2011/2012'), ('2012/2013', '2012/2013'), ('2013/2014', '2013/2014'), ('2014/2015', '2014/2015'), ('2015/2016', '2015/2016'), ('2016/2017', '2016/2017'), ('2017/2018', '2017/2018'), ('2018/2019', '2018/2019'), ('2019/2020', '2019/2020'), ('2020/2021', '2020/2021'), ('2021/2022', '2021/2022'), ('2022/2023', '2022/2023')], max_length=10000, verbose_name='Session')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_akpugo', to=settings.AUTH_USER_MODEL)), 
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='position_akpugo', to='account.position_akpugo')),
            ],
            options={
                'verbose_name': 'Executive (Akpugo)',
                'verbose_name_plural': 'Executives (Akpugo)',
            },
        ),
    ]
