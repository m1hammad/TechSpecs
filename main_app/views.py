
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
class Tech:
    def __init__(self,name,processor,display,ram,storage,os,price) -> None:
        self.name = name
        self.processor = processor
        self.display = display
        self.ram = ram
        self.storage = storage
        self.os = os
        self.price = price
        
laptops = [
    Tech('Dell Inspiron','2.7 GHz Intel Core i7','15.6 inch Full HD touch screen','12 GB DDR4 SDRAM','512 GB (PCIe SSD)','Windows 10', 999.99),
    Tech('mibook','Intel i5/i7 (7th Gen)','13.3 inch','8GB @ 2133MHz','256GB','Windows 10',799.99),
    Tech('MacBook Pro','M1 pro with 8-core CPU','14.2-inch (diagonal) Liquid Retina XDR display','16GB unified memory','512GB SSD','macOS', 2499),
    Tech('HP ENVY x360','AMD Ryzen™ 5 2500U Quad-Core','13.3"','8 GB DDR4-2400 SDRAM','256 GB PCIe® NVMe™ M.2 SSD','Windows 10', 1099)
]

def home(request):
    return HttpResponse('<h1>TechSpecs</h1>')

def about(request):
    return render(request,'about.html')

def tech_index(request):
    return render(request, 'tech/index.html', {'laptops': laptops})