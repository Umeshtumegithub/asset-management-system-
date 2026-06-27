from django.shortcuts import render
from .models import Asset

def dashboard(request):
    total = Asset.objects.count()
    available = Asset.objects.filter(status='Available').count()
    assigned = Asset.objects.filter(status='Assigned').count()

    context = {
        'total': total,
        'available': available,
        'assigned': assigned,
    }

    return render(request, 'dashboard.html', context)

def asset_list(request):
    assets = Asset.objects.all()
    return render(request, 'asset_list.html', {'assets': assets})

def add_asset(request):
    if request.method == 'POST':
        Asset.objects.create(
            asset_id=request.POST['asset_id'],
            asset_name=request.POST['asset_name'],
            category=request.POST['category'],
            status=request.POST['status']
        )
        return redirect('/assets/')

    return render(request, 'add_asset.html')
