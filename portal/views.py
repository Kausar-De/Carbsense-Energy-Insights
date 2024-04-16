from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse

from .forms import *

from playwright.sync_api import sync_playwright

# Create your views here.

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            uname = form.cleaned_data.get('first_name')
            messages.success(request, uname + ' was registered successfully!')
            return redirect('login')

    context = {'form':form}

    return render(request, 'portal/register.html', context)

@unauthenticated_user
def loginPage(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.info(request, 'Username OR Password is incorrect!')
                context = {'form':form}
                return render(request, 'portal/login.html', context)

    context = {'form':form}

    return render(request, 'portal/login.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, 'Successfully logged out!')
    return redirect('login')

def homepage(request):
    return render(request, 'portal/homepage.html')

def calcWallEc(wassembly, walltile, wallarea):
    cem_gwp = Material.objects.filter(name = 'Cement (ordinary Portland cement, OPC)').values_list('gwp', flat=True).first()
    sa_gwp = Material.objects.filter(name = 'M-sand').values_list('gwp', flat=True).first()

    if wassembly == 'Red Brick Construction':
        br_gwp = Material.objects.filter(name = 'Brick (common/facing)').values_list('gwp', flat=True).first()
        brickweight = wallarea * 0.09 * 1900
        brick_ec = brickweight * br_gwp

        cementweight = (wallarea * 0.02 * 2080) / 5
        sandweight = cementweight * 4
        mortar_ec = (cementweight * cem_gwp) + (sandweight * sa_gwp)

        pa_gwp = Material.objects.filter(name = 'Paint').values_list('gwp', flat=True).first()
        paintvolume = wallarea * 0.3
        paint_ec = paintvolume * pa_gwp

        wall_ec = brick_ec + mortar_ec + paint_ec
    else:
        wall_ec = 0

    return wall_ec       

def calcRoofEc(rassembly, rooftile, roofarea):
    cem_gwp = Material.objects.filter(name = 'Cement (ordinary Portland cement, OPC)').values_list('gwp', flat=True).first()
    sa_gwp = Material.objects.filter(name = 'M-sand').values_list('gwp', flat=True).first()
    
    if rassembly == 'Reinforced Cement Concrete (RCC)':
        agg_gwp = Material.objects.filter(name = 'Aggregate (mixed gravel/crushed stone)').values_list('gwp', flat=True).first()
        
        cementweight = (roofarea * 0.2 * 2400) / 4 
        sandweight = cementweight
        aggregatevolume = roofarea * 0.15
        concrete_ec = (cementweight * cem_gwp) + (sandweight * sa_gwp) + (aggregatevolume * agg_gwp)

        cementweight = (roofarea * 0.02 * 2090) / 5.6
        sandweight = cementweight * 4
        mortar_ec = (cementweight * cem_gwp) + (sandweight * sa_gwp)

        st_gwp = Material.objects.filter(name = 'Steel reinforcement (steel rebar)').values_list('gwp', flat=True).first()
        steelweight = roofarea * 12.24
        steel_ec = steelweight * st_gwp
        roof_ec = concrete_ec + mortar_ec + steel_ec
    else:
        roof_ec = 0
    
    if rooftile == 'Clay Roof Tile':
        ti_gwp = Material.objects.filter(name = 'Clay roof tile').values_list('gwp', flat=True).first()
        tileweight = roofarea / (0.25 * 0.3) * 2.17

        pl_gwp = Material.objects.filter(name = 'Cement based plaster').values_list('gwp', flat=True).first()
        plasterweight = roofarea * 0.015 * 1900
        tile_ec = (tileweight * ti_gwp) + (plasterweight * pl_gwp)
    else:
        tile_ec = 0

    return roof_ec + tile_ec
        
def calcFloorEc(fassembly, floorarea):
    cem_gwp = Material.objects.filter(name = 'Cement (ordinary Portland cement, OPC)').values_list('gwp', flat=True).first()
    sa_gwp = Material.objects.filter(name = 'M-sand').values_list('gwp', flat=True).first()

    if fassembly == 'Granite':
        gr_gwp = Material.objects.filter(name = 'Granite').values_list('gwp', flat=True).first()
        graniteweight = floorarea * 0.02 * 2700
        granite_ec = graniteweight * gr_gwp

        cementweight = (floorarea * 0.02 * 2080) / 5
        sandweight = cementweight * 4
        mortar_ec = (cementweight * cem_gwp) + (sandweight * sa_gwp)

        floor_ec = granite_ec + mortar_ec
    else:
        floor_ec = 0

    return floor_ec

def calcGlassEc(glass, frame, windowarea):
    fg_gwp = Material.objects.filter(name = 'Float glass').values_list('gwp', flat=True).first()
    
    if glass == 'Single Glazed Unit (SGU)':
        glassweight = (windowarea / 1.1) * 16.65
        glass_ec = glassweight * fg_gwp
    else:
        glass_ec = 0
    
    if frame == 'Aluminium':
        al_gwp = Material.objects.filter(name = 'Aluminium extruded profile').values_list('gwp', flat=True).first()
        frameweight = windowarea * 21.16
        frame_ec = frameweight * al_gwp
    else:
        frame_ec = 0

    return glass_ec + frame_ec

def calcStructuralEc(sassembly, structuralarea):
    cem_gwp = Material.objects.filter(name = 'Cement (ordinary Portland cement, OPC)').values_list('gwp', flat=True).first()
    sa_gwp = Material.objects.filter(name = 'M-sand').values_list('gwp', flat=True).first()

    if sassembly == 'Reinforced Cement Concrete (RCC)':
        st_gwp = Material.objects.filter(name = 'Steel reinforcement (steel rebar)').values_list('gwp', flat=True).first()
        steelweight = structuralarea * 35.092
        steel_ec = steelweight * st_gwp

        agg_gwp = Material.objects.filter(name = 'Aggregate (mixed gravel/crushed stone)').values_list('gwp', flat=True).first()
        cementweight = (structuralarea * 2.88) / 4
        sandweight = cementweight
        aggregatevolume = structuralarea * 0.15
        binder_ec = (cementweight * cem_gwp) + (sandweight * sa_gwp) + (aggregatevolume * agg_gwp)

        structural_ec = steel_ec + binder_ec
    else:
        structural_ec = 0

    return structural_ec 

@login_required(login_url = 'login')
def datalogger(request):
    formbldg = BuildingForm()
    formsys = BuildingSystemsForm()
    formwall = WallAssemblyForm()
    formroof = RoofAssemblyForm()
    formfloor = FloorAssemblyForm()
    formwindow = WindowAssemblyForm()
    formstructural = StructuralAssemblyForm()

    if request.method == 'POST':
        formbldg = BuildingForm(request.POST)
        formsys = BuildingSystemsForm(request.POST)
        formwall = WallAssemblyForm(request.POST)
        formroof = RoofAssemblyForm(request.POST)
        formfloor = FloorAssemblyForm(request.POST)
        formwindow = WindowAssemblyForm(request.POST)
        formstructural = StructuralAssemblyForm(request.POST)

        if formbldg.is_valid() and formsys.is_valid() and formwall.is_valid() and formroof.is_valid() and formfloor.is_valid() and formwindow.is_valid() and formstructural.is_valid():
            sysid = formsys.save()

            form_wall = formwall.save(commit = False)
            form_wall.roofec = calcWallEc(formwall.cleaned_data.get('wassembly'), formwall.cleaned_data.get('walltile'), formwall.cleaned_data.get('wallarea'))
            wallid = form_wall.save()      

            form_roof = formroof.save(commit = False)
            form_roof.roofec = calcRoofEc(formroof.cleaned_data.get('rassembly'), formroof.cleaned_data.get('rooftile'), formroof.cleaned_data.get('roofarea'))
            roofid = form_roof.save()        

            form_floor = formfloor.save(commit = False)        
            form_floor.floorec = calcFloorEc(formfloor.cleaned_data.get('fassembly'), formfloor.cleaned_data.get('floorarea'))
            floorid = form_floor.save()            

            form_window = formwindow.save(commit = False)
            form_window.windowec = calcGlassEc(formwindow.cleaned_data.get('glass'), formwindow.cleaned_data.get('frame'), formwindow.cleaned_data.get('windowarea'))
            windowid = form_window.save()

            form_structural = formstructural.save(commit = False)
            form_structural.structuralec = calcStructuralEc(formstructural.cleaned_data.get('sassembly'), formstructural.cleaned_data.get('structuralarea'))
            structuralid = form_structural.save()

            bldgsave = formbldg.save(commit = False)
            bldgsave.buildingsystems = sysid
            bldgsave.wallassembly = wallid
            bldgsave.roofassembly = roofid
            bldgsave.floorassembly = floorid
            bldgsave.windowassembly = windowid
            bldgsave.structuralassembly = structuralid
            bldgsave.save()
            return redirect('homepage')
                   
    context = {'formbldg':formbldg, 'formsys':formsys, 'formwall':formwall, 'formroof':formroof, 'formfloor':formfloor, 'formwindow':formwindow, 'formstructural':formstructural}
    return render(request, 'portal/datalogger.html', context)

@login_required(login_url = 'login')
def updateBuilding(request, pk):
    building = Building.objects.get(id = pk)
    formbldg = BuildingForm(instance = building)
    formsys = BuildingSystemsForm(instance = building.buildingsystems)
    formwall = WallAssemblyForm(instance = building.wallassembly)
    formroof = RoofAssemblyForm(instance = building.roofassembly)
    formfloor = FloorAssemblyForm(instance = building.floorassembly)
    formwindow = WindowAssemblyForm(instance = building.windowassembly)
    formstructural = StructuralAssemblyForm(instance = building.structuralassembly)

    if request.method == 'POST':
        formbldg = BuildingForm(request.POST, instance = building)
        formsys = BuildingSystemsForm(request.POST, instance = building.buildingsystems)
        formwall = WallAssemblyForm(request.POST, instance = building.wallassembly)
        formroof = RoofAssemblyForm(request.POST, instance = building.roofassembly)
        formfloor = FloorAssemblyForm(request.POST, instance = building.floorassembly)
        formwindow = WindowAssemblyForm(request.POST, instance = building.windowassembly)
        formstructural = StructuralAssemblyForm(request.POST, instance = building.structuralassembly)
        if formbldg.is_valid() and formsys.is_valid() and formwall.is_valid() and formroof.is_valid() and formfloor.is_valid() and formwindow.is_valid() and formstructural.is_valid():
            formsys.save()         

            form_wall = formwall.save(commit = False)
            form_wall.wallec = calcWallEc(formwall.cleaned_data.get('wassembly'), formwall.cleaned_data.get('walltile'), formwall.cleaned_data.get('wallarea'))
            form_wall.save() 

            form_roof = formroof.save(commit = False)
            form_roof.roofec = calcRoofEc(formroof.cleaned_data.get('rassembly'), formroof.cleaned_data.get('rooftile'), formroof.cleaned_data.get('roofarea'))
            form_roof.save()        

            form_floor = formfloor.save(commit = False)        
            form_floor.floorec = calcFloorEc(formfloor.cleaned_data.get('fassembly'), formfloor.cleaned_data.get('floorarea'))
            form_floor.save()            

            form_window = formwindow.save(commit = False)
            form_window.windowec = calcGlassEc(formwindow.cleaned_data.get('glass'), formwindow.cleaned_data.get('frame'), formwindow.cleaned_data.get('windowarea'))
            form_window.save()

            form_structural = formstructural.save(commit = False)
            form_structural.structuralec = calcStructuralEc(formstructural.cleaned_data.get('sassembly'), formstructural.cleaned_data.get('structuralarea'))
            form_structural.save()

            formbldg.save()
            return redirect('buildingprofile', pk = pk)
    
    context = {'formbldg':formbldg, 'formsys':formsys, 'formwall':formwall, 'formroof':formroof, 'formfloor':formfloor, 'formwindow':formwindow, 'formstructural':formstructural}

    return render(request, 'portal/datalogger.html', context)

@login_required(login_url = 'login')
def yourBuildings(request):
    buildings = Building.objects.filter(user = request.user)

    context = {'buildings':buildings}
    return render(request, 'portal/yourbuildings.html', context)

@login_required(login_url = 'login')
def buildingprofile(request, pk):
    building = Building.objects.get(id = pk)

    lastyrunits = building.lastyr_units.split(", ")
    twoyrbfrunits = building.twoyrbfr_units.split(", ")
    threeyrbfrunits = building.threeyrbfr_units.split(", ")

    if 'Other' in building.buildingsystems.appls:
        appliances = str(building.buildingsystems.appls).replace(', Other', '') + ', ' + str(building.buildingsystems.otherappls)

    buildingEPI = round((building.units / building.area), 3)
    buildingPOC = round((building.units / building.occupants), 3)

    wallecperunit = building.wallassembly.wallec / building.wallassembly.wallarea
    roofecperunit = building.roofassembly.roofec / building.roofassembly.roofarea
    floorecperunit = building.floorassembly.floorec / building.floorassembly.floorarea
    windowecperunit = building.windowassembly.windowec / building.windowassembly.windowarea
    structuralecperunit = building.structuralassembly.structuralec / building.structuralassembly.structuralarea

    allbuildingsincat = Building.objects.filter(category = building.category)
    
    allunits = list(i.units for i in allbuildingsincat)
    allareas = list(i.area for i in allbuildingsincat)
    alloccupants = list(i.occupants for i in allbuildingsincat)

    meanEPI = round((sum([allunits[i] / allareas[i] for i in range(allbuildingsincat.count())]) / allbuildingsincat.count()), 3)
    percEPI = round((((meanEPI - buildingEPI) * 100) / buildingEPI), 2)

    meanPOC = round((sum([allunits[i] / alloccupants[i] for i in range(allbuildingsincat.count())]) / allbuildingsincat.count()), 3)
    percPOC = round((((meanPOC - buildingPOC) * 100) / buildingPOC), 2)
    
    context = {'building':building, 'appliances':appliances, 'lastyrunits':lastyrunits, 'twoyrbfrunits':twoyrbfrunits, 'threeyrbfrunits':threeyrbfrunits, 'wallecperunit':wallecperunit, 'roofecperunit':roofecperunit, 'floorecperunit':floorecperunit, 'windowecperunit':windowecperunit, 'structuralecperunit':structuralecperunit, 'buildingEPI': buildingEPI, 'buildingPOC':buildingPOC, 'percEPI': percEPI, 'percPOC': percPOC}
    return render(request, 'portal/buildingprofile.html', context)

@login_required(login_url = 'login')
def buildingPDF(request, pk):
    building = Building.objects.get(id = pk)

    lastyrunits = building.lastyr_units.split(", ")
    twoyrbfrunits = building.twoyrbfr_units.split(", ")
    threeyrbfrunits = building.threeyrbfr_units.split(", ")

    if 'Other' in building.buildingsystems.appls:
        appliances = str(building.buildingsystems.appls).replace(', Other', '') + ', ' + str(building.buildingsystems.otherappls)

    buildingEPI = round((building.units / building.area), 3)
    buildingPOC = round((building.units / building.occupants), 3)

    wallecperunit = building.wallassembly.wallec / building.wallassembly.wallarea
    roofecperunit = building.roofassembly.roofec / building.roofassembly.roofarea
    floorecperunit = building.floorassembly.floorec / building.floorassembly.floorarea
    windowecperunit = building.windowassembly.windowec / building.windowassembly.windowarea
    structuralecperunit = building.structuralassembly.structuralec / building.structuralassembly.structuralarea
    
    allbuildingsincat = Building.objects.filter(category = building.category)
    
    allunits = list(i.units for i in allbuildingsincat)
    allareas = list(i.area for i in allbuildingsincat)
    alloccupants = list(i.occupants for i in allbuildingsincat)

    meanEPI = round((sum([allunits[i] / allareas[i] for i in range(allbuildingsincat.count())]) / allbuildingsincat.count()), 3)
    percEPI = round((((meanEPI - buildingEPI) * 100) / buildingEPI), 2)

    meanPOC = round((sum([allunits[i] / alloccupants[i] for i in range(allbuildingsincat.count())]) / allbuildingsincat.count()), 3)
    percPOC = round((((meanPOC - buildingPOC) * 100) / buildingPOC), 2)
    
    context = {'building':building, 'appliances':appliances, 'lastyrunits':lastyrunits, 'twoyrbfrunits':twoyrbfrunits, 'threeyrbfrunits':threeyrbfrunits, 'wallecperunit':wallecperunit, 'roofecperunit':roofecperunit, 'floorecperunit':floorecperunit, 'windowecperunit':windowecperunit, 'structuralecperunit':structuralecperunit, 'buildingEPI': buildingEPI, 'buildingPOC':buildingPOC, 'percEPI': percEPI, 'percPOC': percPOC}
    return render(request, 'portal/buildingpdf.html', context)

@login_required(login_url = 'login')
def generatePDF(request, pk):
    building = Building.objects.only('name').get(id = pk)

    filename = str("Building LCA Report - " + building.name + ".pdf")

    with sync_playwright() as p:
        browser = p.chromium.launch()

        page = browser.new_page()

        page.goto(request.build_absolute_uri(reverse('buildingpdf', args = [pk])))

        pdf = page.pdf(print_background = True)
        
        browser.close()  

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = "inline; filename = {}".format(filename)
    return response

@login_required(login_url = 'login')
def iot(request):
    return render(request, 'portal/iot.html')