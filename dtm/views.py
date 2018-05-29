try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import *
from .form import *


# Create your views here.
def index(request):
    return render(request, "dtm/index.html", {})

def sysCmmncdD(request):
    #마스터 코드
    SysCmmncdM = json.dumps([{'text': data.mcode_nm, 'value': data.mcode_id} for data in SysCmmncdM.objects.all()])

    context = {'SysCmmncdM': SysCmmncdM}
    return render(request, 'dtm/sysCmmncdD.html', context)

@require_POST
def sysCmmncdD_List(request):
    if request.method == 'POST':
        qs = SysCmmncdD.objects.values()[:5]
        data = json.dumps(list(qs), cls=DjangoJSONEncoder, ensure_ascii=False)

        content = {
            "result": "true",
            "data": {
                "contents": json.loads(data)
            }
        }
    return JsonResponse(content)

@require_POST
def sysCmmncdD_Save(request):
    cRows = request.POST.get('createdRows', None)
    uRows = request.POST.get('updatedRows', None)
    dRows = request.POST.get('deletedRows', None)
    message = "정상적으로 처리되었습니다.";

    if cRows is not None:
        cRows = json.loads(cRows)
        for idx in range(len(cRows)):
            cData = SysCmmncdDSerializer(data=cRows[idx])
            if cData.is_valid():
                cData.save()
    if uRows is not None:
        uRows = json.loads(uRows)
        for idx in range(len(uRows)):
            pk = uRows[idx]['dcode_sn']
            instance = SysCmmncdD.objects.get(dcode_sn=pk)
            uData = SysCmmncdDSerializer(instance, data=uRows[idx])
            if uData.is_valid():
                uData.save()
    if dRows is not None:
        dRows = json.loads(dRows)
        for idx in range(len(dRows)):
            pk = dRows[idx]['dcode_sn']
            instance = SysCmmncdD.objects.get(dcode_sn=pk)
            instance.delete()

    content = {
        "result": "true",
        "message": message
    }

    return JsonResponse(content)

def mmsImprmn(request):
    #설비
    MMS_EQP = json.dumps([{'text': data.eqp_nm, 'value': data.eqp_sn} for data in MmsEqp.objects.all()])
    #부품
    #MMS_CMPNT = json.dumps([{data1.eqp_sn: [{'text': data.cmpnt_nm, 'value': data.cmpnt_sn} for data in MmsCmpnt.objects.filter(eqp_sn=data1.eqp_sn)]}for data1 in MmsEqp.objects.all()])
    Eqps = MmsEqp.objects.all()
    MMS_CMPNT = {}
    for Eqp in Eqps:
        MMS_CMPNT[Eqp.eqp_sn] = [{'text': data.cmpnt_nm, 'value': data.cmpnt_sn} for data in MmsCmpnt.objects.filter(eqp_sn=Eqp.eqp_sn)]

    MMS_CMPNT = json.dumps(MMS_CMPNT)

    #보전구분
    MMS060 = json.dumps([{'text': data.dcode_nm, 'value': data.dcode_sn} for data in SysCmmncdD.objects.filter(mcode_id='MMS060')])
    #작업구분
    MMS030 = json.dumps([{'text': data.dcode_nm, 'value': data.dcode_sn} for data in SysCmmncdD.objects.filter(mcode_id='MMS030')])
    #고장현상
    MMS040 = json.dumps([{'text': data.dcode_nm, 'value': data.dcode_sn} for data in SysCmmncdD.objects.filter(mcode_id='MMS040')])
    #고장원인
    MMS050 = json.dumps([{'text': data.dcode_nm, 'value': data.dcode_sn} for data in SysCmmncdD.objects.filter(mcode_id='MMS050')])
    #부서
    MMS070 = json.dumps([{'text': data.dcode_nm, 'value': data.dcode_sn} for data in SysCmmncdD.objects.filter(mcode_id='MMS070')])

    context = {'MMS_EQP': MMS_EQP, 'MMS_CMPNT': MMS_CMPNT, 'MMS060': MMS060, 'MMS030': MMS030, 'MMS040': MMS040, 'MMS050': MMS050, 'MMS070': MMS070}
    return render(request, 'dtm/mmsImprmn.html', context)

def mmsImprmnForm(request):

    #설비
    MMS_EQP = MmsEqp.objects.all()
    #보전구분
    MMS060S = SysCmmncdD.objects.filter(mcode_id='MMS060')
    #작업구분
    MMS030S = SysCmmncdD.objects.filter(mcode_id='MMS030')
    #고장현상
    MMS040S = SysCmmncdD.objects.filter(mcode_id='MMS040')
    #고장원인
    MMS050S = SysCmmncdD.objects.filter(mcode_id='MMS050')
    #부서
    MMS070S = SysCmmncdD.objects.filter(mcode_id='MMS070')
    context = {'MMS_EQP': MMS_EQP, 'MMS060S': MMS060S, 'MMS030S': MMS030S, 'MMS040S': MMS040S, 'MMS050S': MMS050S, 'MMS070S': MMS070S}

    return render(request, 'dtm/mmsImprmnForm.html', context)

def mmsImprmnForm2(request):
    form = MmsImprmnForm()
    return render(request, 'dtm/mmsImprmnForm2.html', {'form':form})

def load_cmpnts(request):
    eqp_sn = request.GET.get('eqp_sn')
    cmpnts = MmsCmpnt.objects.filter(eqp_sn=eqp_sn)
    return render(request, 'dtm/cmpnt_select.html', {'cmpnts': cmpnts})

@require_POST
def mmsImprmn_List(request):
    if request.method == 'POST':
        qs = MmsImprmn.objects.values()
        data = json.dumps(list(qs), cls=DjangoJSONEncoder, ensure_ascii=False)

        content = {
            "result": "true",
            "data": {
                "contents": json.loads(data)
            }
        }
    return JsonResponse(content)

@require_POST
def mmsImprmn_Save(request):
    cRows = request.POST.get('createdRows', None)
    uRows = request.POST.get('updatedRows', None)
    dRows = request.POST.get('deletedRows', None)
    message = "정상적으로 처리되었습니다.";

    if cRows is not None:
        cRows = json.loads(cRows)
        for idx in range(len(cRows)):
            cData = MmsImprmnSerializer(data=cRows[idx])
            if cData.is_valid():
                cData.save()
    if uRows is not None:
        uRows = json.loads(uRows)
        for idx in range(len(uRows)):
            pk = uRows[idx]['imprmn_sn']
            instance = MmsImprmn.objects.get(imprmn_sn=pk)
            uData = MmsImprmnSerializer(instance, data=uRows[idx])
            if uData.is_valid():
                uData.save()
    if dRows is not None:
        dRows = json.loads(dRows)
        for idx in range(len(dRows)):
            pk = dRows[idx]['imprmn_sn']
            instance = MmsImprmn.objects.get(imprmn_sn=pk)
            instance.delete()

    content = {
        "result": "true",
        "message": message
    }

    return JsonResponse(content)

def chart(request):

    return render(request, 'dtm/chart1.html', {})