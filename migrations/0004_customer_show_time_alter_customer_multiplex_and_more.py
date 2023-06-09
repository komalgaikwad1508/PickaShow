# Generated by Django 4.0.5 on 2022-09-06 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_customer_multiplex'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='show_time',
            field=models.CharField(choices=[('Morning 10 am', 'Morning 10 am'), ('Afternoon 1pm', 'Afternoon 1pm'), ('Evening 5pm', 'Evening 5pm'), ('Night 9pm', 'Night 9pm')], default='morning 9am', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='multiplex',
            field=models.CharField(choices=[('Abhiruchi City Pride Sinhagad Road', 'Abhiruchi City Pride Sinhagad Road'), ('Ashok Theatre Pimpri', 'Ashok Theatre Pimpri'), ('Bollywood Multiplex Kharadi', 'Bollywood Multiplex Kharadi'), ('Carnival Cinemas Moshi Pradhikaran', 'Carnival Cinemas Moshi Pradhikaran'), ('Carnival Premier Plaza Chinchwad', 'Carnival Premier Plaza Chinchwad'), ('CinePRO Vasant Cinema Shivaji Maharaj Chowk Pune', 'CinePRO Vasant Cinema Shivaji Maharaj Chowk Pune'), ('Cinepolis Nexus WESTEND Mall Aundh', 'Cinepolis Nexus WESTEND Mall Aundh'), ('Cinepolis  Seasons Mall Pune', 'Cinepolis  Seasons Mall Pune'), ('City Pride Kothrud', 'City Pride Kothrud'), ('City Pride Satara Road', 'City Pride Satara Road'), ('Mangala Cinema Shivajinagar', 'Mangala Cinema Shivajinagar'), ('E-Square ELITE Hinjawadi', 'E-Square ELITE Hinjawadi'), ('fun Time Multiplex Sinhagad Road', 'fun Time Multiplex Sinhagad Road'), ('INOX Amanora Town centre Hadapsar', 'INOX Amanora Town centre Hadapsar'), ('PVR ICON  Pavillion Pune senapati bapat road', 'PVR ICON  Pavillion Pune senapati bapat road'), ('PVR  Kumar pacific shankarsheth road', 'PVR  Kumar pacific shankarsheth road'), ('Rahul 70 MM Shivajinagar', 'Rahul 70 MM Shivajinagar'), ('Rajhans Cinemas Fatimanagar', 'Rajhans Cinemas Fatimanagar'), ('Satyam Theatre Rajgurunagar', 'Satyam Theatre Rajgurunagar'), ('Victory Theatre Camp Pune', 'Victory Theatre Camp Pune'), ('Vilux talkies Khadki', 'Vilux talkies Khadki'), ('Vishal Cinemas Pimpri', 'Vishal Cinemas Pimpri'), ('Apsara Tokies Seven loves chowk', 'Apsara Tokies  Seven loves chowk'), ('Laxmi Narayan theatre Swargate', 'Laxmi Narayan theatre Swargate'), ('Nilayam tokies Parvati', 'Nilayam tokies  Parvati')], default='Abhiruchi City Pride Sinhagad Road', max_length=50),
        ),
        migrations.AlterField(
            model_name='ticketbooking',
            name='status',
            field=models.CharField(choices=[('Confirm', 'Confirm'), ('Cancel', 'Cancel')], default='Confirm', max_length=50),
        ),
    ]
