from django.shortcuts import redirect, render,get_object_or_404
from  .form import updateProduct
from .models import insertProduct

def store(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        slug=request.POST.get('slug')
        description=request.POST.get('description')
       
        productdata = insertProduct(name=name, slug=slug,description=description)
        productdata.save() 


    return redirect('index')


def createProduct(request):

    return render(request,'product/create.html')


def index(request):
    productdata = insertProduct.objects.all()

    content = {
        'product':productdata
    }
       
    return render(request,'product/index.html',content)

def edit(request,id):
    product = insertProduct.objects.get(id=id)
    
    return render(request,'product/edit.html',{'product':product})

def update(request,id):
    product = get_object_or_404(insertProduct,id=id)
    if request.method == 'POST':
        form=updateProduct(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form=updateProduct()
        return render(request,'edit.html',{'form':form})
        


def destroy(request,id):
     product = insertProduct.objects.get(id=id)
     product.delete()
     return redirect('index')
