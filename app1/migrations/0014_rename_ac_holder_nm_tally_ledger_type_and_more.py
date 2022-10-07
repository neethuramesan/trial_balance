# Generated by Django 4.0.5 on 2022-09-12 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_ledger_vouchers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tally_ledger',
            old_name='ac_holder_nm',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='Echeque_p',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='SA_chequeP_con',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='SA_cheque_bk',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='acc_no',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='address',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='appropriate_to',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='assessable_value',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='balance_billbybill',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='bank_details',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='bank_name',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='country',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='credit_period',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='creditdays_voucher',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='gst_applicable',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='gst_uin',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='ifsc_code',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='method_of_calculation',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='mname',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='pan_no',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='percentage_of_calcution',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='rate_per_unit',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='registration_type',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='rond_limit',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='rond_method',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='rounding_limit',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='rounding_method',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='set_alter_gstdetails',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='set_odl',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='setalter_gstdetails',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='state',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='swift_code',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='tax_type',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='type_duty_tax',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='type_of_ledger',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='type_of_supply',
        ),
        migrations.RemoveField(
            model_name='tally_ledger',
            name='valuation_type',
        ),
    ]
