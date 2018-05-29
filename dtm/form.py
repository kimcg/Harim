from django import forms
from .models import *

class MmsImprmnForm(forms.ModelForm) :

    class Meta:
        model = MmsImprmn
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(MmsImprmnForm, self).__init__(*args, **kwargs)  # Call to ModelForm constructor
        self.fields['eqp_sn'].widget.attrs['class'] = 'w10p'
        if 'eqp_sn' in self.data:
            try:
                eqp_sn = int(self.data.get('eqp_sn'))
                self.fields['cmpnt_sn'].queryset = MmsCmpnt.objects.filter(eqp_sn=eqp_sn)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset


    #보전구분
    MMS060 = [(data.dcode_sn, data.dcode_nm) for data in SysCmmncdD.objects.filter(mcode_id='MMS060')]
    #작업구분
    MMS030 = [(data.dcode_sn, data.dcode_nm) for data in SysCmmncdD.objects.filter(mcode_id='MMS030')]
    #고장현상
    MMS040 = [(data.dcode_sn, data.dcode_nm) for data in SysCmmncdD.objects.filter(mcode_id='MMS040')]
    #고장원인
    MMS050 = [(data.dcode_sn, data.dcode_nm) for data in SysCmmncdD.objects.filter(mcode_id='MMS050')]
    #부서
    MMS070 = [(data.dcode_sn, data.dcode_nm) for data in SysCmmncdD.objects.filter(mcode_id='MMS070')]
    #여부
    YN = [('Y', '예'), ('N', '아니요')]

    cmpny_id = forms.CharField(widget=forms.HiddenInput)
    eqp_sn = forms.ChoiceField(choices=[(data.eqp_sn, data.eqp_nm) for data in MmsEqp.objects.all()], label='설비')
    cmpnt_sn = forms.ChoiceField(label='부품')
    presvse_cd = forms.ChoiceField(choices=MMS060, label='보전구분')
    presvexecut_cd = forms.ChoiceField(choices=MMS060, label='보전실행')
    opertdept_cd = forms.ChoiceField(choices=MMS070, label='작업부서')
    chckat_cd = forms.ChoiceField(choices=YN, label='점검여부')
    nrmltat_cd = forms.ChoiceField(choices=YN, label='정상여부')
    processdept_cd = forms.ChoiceField(choices=MMS070, label='처리주체')
    opertse_cd = forms.ChoiceField(choices=MMS030, label='작업구분')
    defectsittn_cd = forms.ChoiceField(choices=MMS040, label='고장상황')
    defectcause_cd = forms.ChoiceField(choices=MMS050, label='고장원인')
    opert_cn = forms.CharField(widget=forms.Textarea, label='작업내용')

