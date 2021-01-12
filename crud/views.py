from django.shortcuts import render, redirect
from .models import Member
from .models import Relatorio

# Create your views here.

def index(request):
    members = Member.objects.all()
    context = {'members': members}

    return render(request, 'crud/index.html', context)

def cadprot(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'crud/cadprot.html', context)

def create(request):
    member=Member(protocolo=request.POST['protocolo'],datarecebimento=request.POST['datarecebimento'],datadocumento=request.POST['datadocumento'],aeronave=request.POST['aeronave'],tipodoc=request.POST['tipodoc'],	numdoc=request.POST['numdoc'],anexo=request.POST['anexo'],obsdoc=request.POST['obsdoc'],mecanico=request.POST['mecanico'],inspetor=request.POST['inspetor'],recebido=request.POST['recebido'],erros=request.POST['erros'],	campos=request.POST['campos'],descricao=request.POST['descricao'],status=request.POST['status'],datastatus=request.POST['datastatus'],)
    member.save()
    return redirect('/')

def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crud/edit.html', context)

def form(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crud/form.html', context)

def update(request, id):
    member = Member.objects.get(id=id)
    member.protocolo = request.POST['protocolo']
    member.datarecebimento = request.POST['datarecebimento']
    member.datadocumento=request.POST['datadocumento']
    member.aeronave=request.POST['aeronave']
    member.tipodoc=request.POST['tipodoc']
    member.numdoc=request.POST['numdoc']
    member.anexo=request.POST['anexo']
    member.obsdoc=request.POST['obsdoc']
    member.mecanico=request.POST['mecanico']
    member.inspetor=request.POST['inspetor']
    member.recebido=request.POST['recebido']
    member.erros=request.POST['erros']
    member.campos=request.POST['campos']
    member.descricao=request.POST['descricao']
    member.status=request.POST['status']
    member.datastatus=request.POST['datastatus']
    member.save()
    return redirect('/crud/')

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/crud/')

############################################## Views - RTA#############################################

def cadRTA(request):
    members = Relatorio.objects.all()
    context2 = {'members': members}
    return render(request, 'crud/cadRTA.html', context2)

def createRTA(request):

    member=Relatorio(Acft = request.POST['Acft'], NumRTA = request.POST['NumRTA'],)
    member.save()

    return redirect('/')


def editRTA(request, id):
    members = Relatorio.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crud/editRTA.html', context)

def updateRTA(request, id):
    member = Relatorio.objects.get(id=id)
    member.Acft = request.POST['Acft']
    member.NumRTA = request.POST['NumRTA']
    member.Origem=request.POST['Origem']
    member.NumVoo=request.POST['NumVoo']
    member.NumDB=request.POST['NumDB']
    member.Trecho=request.POST['Trecho']
    member.DataRTA=request.POST['DataRTA']
    member.Disc=request.POST['Disc']
    member.Mecanico1=request.POST['Mecanico1']
    member.CodAnac1=request.POST['CodAnac1']
    member.AcaoDisc=request.POST['AcaoDisc']
    member.Mecanico2=request.POST['Mecanico2']
    member.CodAnac2=request.POST['CodAnac2']
    member.RefRTA=request.POST['RefRTA']
    member.Ata=request.POST['Ata']
    member.Mel=request.POST['Mel']
    member.Acr=request.POST['Acr']
    member.RefItem=request.POST['RefItem']
    member.Cat=request.POST['Cat']
    member.SaidaPN1=request.POST['SaidaPN1']
    member.SaidaSN1=request.POST['SaidaSN1']
    member.SaidaPOS1=request.POST['SaidaPOS1']
    member.EntradaPN1=request.POST['EntradaPN1']
    member.EntradaSN1=request.POST['EntradaSN1']
    member.EntradaPOS1=request.POST['EntradaPOS1']
    member.SaidaPN2=request.POST['SaidaPN2']
    member.SaidaSN2=request.POST['SaidaSN2']
    member.SaidaPOS2=request.POST['SaidaPOS2']
    member.EntradaPN2=request.POST['EntradaPN2']
    member.EntradaSN2=request.POST['EntradaSN2']
    member.EntradaPOS2=request.POST['EntradaPOS2']
    member.SaidaPN3=request.POST['SaidaPN3']
    member.SaidaSN3=request.POST['SaidaSN3']
    member.SaidaPOS3=request.POST['SaidaPOS3']
    member.EntradaPN3=request.POST['EntradaPN3']
    member.EntradaSN3=request.POST['EntradaSN3']
    member.EntradaPOS3=request.POST['EntradaPOS3']
    member.OleoLH=request.POST['OleoLH']
    member.OleoRH=request.POST['OleoRH']
    member.OleoHID=request.POST['OleoHID']
    member.Diaria=request.POST['Diaria']
    member.Linha=request.POST['Linha']
    member.Semanal=request.POST['Semanal']
    member.PMA=request.POST['PMA']
    member.JIC=request.POST['JIC']
    member.Hora=request.POST['Hora']
    member.DataLib=request.POST['DataLib']
    member.CodANACLib=request.POST['CodANACLib']
    member.save()
    return redirect('/crud/')

def deleteRTA(request, id):
    member = Relatorio.objects.get(id=id)
    member.delete()
    return redirect('/crud/')
