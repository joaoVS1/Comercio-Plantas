from multiprocessing import context
from django.shortcuts import render, redirect
from plantas.models import Planta
from django.views import View
from django.contrib import messages

# Create your views here.
def comprar(request):
    plantas = Planta.objects.all()
    context = {
        'plantas': plantas,
    }
    if 'carrinho' in request.session:
        context['num'] = len(request.session['carrinho'])
    return render(request,'comprar.html', context)

def add_carrinho(request):
    pk = request.POST.get('cart')
    qtd = int(request.POST.get('qtd'))
    infoCompra = [pk,qtd]
    i=0
    if 'carrinho' in request.session:
        numi = len(request.session['carrinho'])
        for i in range(numi):
            if pk in request.session['carrinho'][i]:
                #eu tava querendo fazer o carrinho somar apenas a quantidade aos itens já existentes
                request.session['carrinho'][i][1]+=qtd
                request.session.modified = True
                break
            else:
                if i == numi-1:
                    request.session['carrinho'] += [infoCompra] 
                    request.session.modified = True
    else:
        print('first')
        request.session['carrinho'] = [infoCompra]
    return redirect('./#')

def removerCarrinho(request,pk):
    if 'carrinho' in request.session:
        numi = len(request.session['carrinho'])
        for i in range(numi):
            if str(pk) in request.session['carrinho'][i]:
                qtd= request.session['carrinho'][i][1]
                sla = [str(pk),qtd]
                request.session['carrinho'].remove(sla)
                request.session.modified = True
                #del request.session['carrinho'][i]
                break
        return redirect('carrinho')

class PaginaProduto(View):
    def get(self, request, pk):
        planta = Planta.objects.get(pk=pk)
        context = {
            'planta': planta,
        }
        if 'carrinho' in request.session:
            context['num'] = len(request.session['carrinho'])
        return render (request, 'paginaProduto.html', context)
        def post(self, request):
            pass



class Carrinho(View):
        
    def get (self, request):
        if 'carrinho' in request.session:
            cart = request.session['carrinho']
            plantas = Planta.objects.all()
            plantaCarrinho = []
            total = 0
            for car in cart:
                planta = plantas.get(pk=int(car[0]))
                plantaCarrinho.append([planta, car[1]])
                total += planta.preco * int(car[1]) 
                    #for planta in plantas:
                    #    for i in cart:
                    #        if i[0]==str(planta.pk):
                    #            plantaCarrinho.append(planta)
                                
                #            print(plantaCarrinho)  
            numCart = len(cart)

            context = {
                'carrinho': plantaCarrinho,
                'cart': cart,
                'plantas':plantas,
                'total': total,
                'numCart': numCart,
            }   
            return render(request, 'carrinho.html', context)
        else:
            return render(request, 'carrinho.html')
    def post (self, request):
        pass


def pagamento(request):
    if 'usuario' in request.session:
        return render(request, 'pagamento.html')
    else:
        messages.add_message(request, messages.INFO, 'Para Comprar, faça o login ou crie uma conta: ')
        return redirect('login')