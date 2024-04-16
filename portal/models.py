from django.db import models
from multiselectfield import MultiSelectField
from django.conf import settings

# Create your models here.

class BuildingSystems(models.Model):
    HVACSYSTEMS = (
        ('Fan', 'Fan'),
        ('Split AC', 'Split AC'),
        ('Window AC', 'Window AC'),
        ('Split + Window AC', 'Split + Window AC'),
        ('Mixed Mode/Hybrid', 'Mixed Mode/Hybrid'),        
        ('Evaporative Cooler', 'Evaporative Cooler'),
        ('VRF', 'VRF'),      
    )

    STARRATINGS = (
        ('1 Star', '1 Star'),
        ('2 Star', '2 Star'),
        ('3 Star', '3 Star'),
        ('4 Star', '4 Star'),
        ('5 Star', '5 Star'),            
    )

    APPLIANCES = (
        ('Air Conditioner', 'Air Conditioner'),
        ('Computer', 'Computer'),
        ('LED', 'LED'),
        ('CFL', 'CFL'),
        ('Microwave', 'Microwave'),
        ('Washing Machine', 'Washing Machine'),
        ('Ceiling Fan', 'Ceiling Fan'),
        ('Refrigerator', 'Refrigerator'),
        ('Air Fryer', 'Air Fryer'),
        ('Chimney', 'Chimney'),
        ('Geyser', 'Geyser'),
        ('OTG', 'OTG'),
        ('Oven', 'Oven'),
        ('Electric Stove', 'Electric Stove'),
        ('BEV Charger', 'BEV Charger'),
        ('Television', 'Television'),
        ('Room Heater', 'Room Heater'),
        ('Electric Kettle', 'Electric Kettle'),
        ('Other', 'Other'),
    )

    hvacsystem = models.TextField(max_length = 200, choices = HVACSYSTEMS, default = 'Choose Primary HVAC System...', null = True)
    starrating = models.TextField(max_length = 200, choices = STARRATINGS, default = 'Choose Star Rating...', null = True)
    setpoint = models.IntegerField(default = 0, null = True)
    totaltr = models.IntegerField(default = 0, null = True)
    appls = MultiSelectField(choices = APPLIANCES, max_choices = 19, max_length = 200, null = True)
    otherappls = models.CharField(max_length = 500, null = True, blank = True)

class WallAssembly(models.Model):
    WALLASSEMBLIES = (
        ('Red Brick Construction', 'Red Brick Construction'),
        ('Reinforced Cement Concrete (RCC)', 'Reinforced Cement Concrete (RCC)'),
        ('Fly Ash Bricks', 'Fly Ash Bricks'),
        ('Autoclaved Aerated Concrete (AAC)', 'Autoclaved Aerated Concrete (AAC)'),
        ('Custom', 'Custom'),        
    )

    INSULATIONS = (
        ('None', 'None'), 
        ('NCM - Stone Wool', 'NCM - Stone Wool'),
        ('NCM - Glass Wool', 'NCM - Glass Wool'),
        ('Expanded Polystyrene (XPS/EPS)', 'Expanded Polystyrene (XPS/EPS)'),
    )
    
    TILES = (
        ('None', 'None'), 
        ('Ceramic Tile', 'Ceramic Tile'),
    )

    wallarea = models.FloatField(default = 0, null = True)
    wassembly = models.TextField(max_length = 200, choices = WALLASSEMBLIES, default = 'Choose Assembly...', null = True)
    wallinsulation = models.TextField(max_length = 200, choices = INSULATIONS, default = 'Choose Insulation...', null = True)
    walltile = models.TextField(max_length = 200, choices = TILES, default = 'Choose Tiles...', null = True)
    wallec = models.FloatField(default = 0, null = True)

class RoofAssembly(models.Model):
    ROOFASSEMBLIES = (
        ('Reinforced Brick Concrete (RBC)', 'Reinforced Brick Concrete (RBC)'),
        ('Reinforced Cement Concrete (RCC)', 'Reinforced Cement Concrete (RCC)'),
        ('Fly Ash Bricks', 'Fly Ash Bricks'),
        ('Autoclaved Aerated Concrete (AAC)', 'Autoclaved Aerated Concrete (AAC)'),
        ('Custom', 'Custom'),        
    )

    INSULATIONS = (
        ('None', 'None'), 
        ('NCM - Stone Wool', 'NCM - Stone Wool'),
        ('NCM - Glass Wool', 'NCM - Glass Wool'),
        ('Expanded Polystyrene (XPS/EPS)', 'Expanded Polystyrene (XPS/EPS)'),
    )

    TILES = (
        ('None', 'None'), 
        ('Clay Roof Tile', 'Clay Roof Tile'),
        ('Cool Roof TIle', 'Cool Roof TIle'),
    )

    roofarea = models.FloatField(default = 0, null = True)
    rassembly = models.TextField(max_length = 200, choices = ROOFASSEMBLIES, default = 'Choose Assembly...', null = True)
    roofinsulation = models.TextField(max_length = 200, choices = INSULATIONS, default = 'Choose Insulation...', null = True)
    rooftile = models.TextField(max_length = 200, choices = TILES, default = 'Choose Tiles...', null = True)
    roofec = models.FloatField(default = 0, null = True)

class FloorAssembly(models.Model):
    FLOORASSEMBLIES = (
        ('Granite', 'Granite'),
        ('Marble', 'Marble'),
        ('Wood', 'Wood'),
        ('Custom', 'Custom'),        
    )

    floorarea = models.FloatField(default = 0, null = True)
    fassembly = models.TextField(max_length = 200, choices = FLOORASSEMBLIES, default = 'Choose Assembly...', null = True)
    floorec = models.FloatField(default = 0, null = True)

class WindowAssembly(models.Model):
    GLASSES = (
        ('Single Glazed Unit (SGU)', 'Single Glazed Unit (SGU)'),
        ('Double Glazed Unit (DGU)', 'Double Glazed Unit (DGU)'),       
    )

    FRAMES = (
        ('Aluminium', 'Aluminium'),
        ('Wood', 'Wood'),       
    )

    windowarea = models.FloatField(default = 0, null = True)
    glass = models.TextField(max_length = 200, choices = GLASSES, default = 'Choose Glass...', null = True)
    frame = models.TextField(max_length = 200, choices = FRAMES, default = 'Choose Frame...', null = True)
    windowec = models.FloatField(default = 0, null = True)

class StructuralAssembly(models.Model):
    STRUCTURALASSEMBLIES = (
        ('Reinforced Cement Concrete (RCC)', 'Reinforced Cement Concrete (RCC)'),    
    )

    structuralarea = models.FloatField(default = 0, null = True)
    sassembly = models.TextField(max_length = 200, choices = STRUCTURALASSEMBLIES, default = 'Choose Assembly...', null = True)
    structuralec = models.FloatField(default = 0, null = True)

class Material(models.Model):
    CATEGORIES = (
        ('Wall', 'Wall'),
        ('Roof', 'Roof'),
        ('Floor', 'Floor'),
        ('Fenestration', 'Fenestration'),
        ('Structural', 'Structural'),
    )

    UNITS = (
        ('kg (Kilogram)', 'kg (Kilogram)'),
        ('l (Litre)', 'l (Litre)'),
        ('cu.m (Cubic Metre)', 'cu.m (Cubic Metre)'),
        ('kWh (KiloWatt-Hours)', 'kWh (KiloWatt-Hours)'),
    )
    
    category = MultiSelectField(choices = CATEGORIES, max_choices = 5, default = 'Wall', max_length = 200, null = True)
    name = models.CharField(max_length = 200, null = True)
    unit = models.TextField(max_length = 200, choices = UNITS, default = 'Choose Unit...', null = True)
    gwp = models.FloatField(default = 0, null = True)    

    def __str__(self):
        return self.name
    
class Building(models.Model):
    TYPES = (
        ('Flat (Standalone)', 'Flat (Standalone)'),
        ('Flat (Complex)', 'Flat (Complex)'),
        ('Rented', 'Rented'),
        ('House', 'House'),          
    )
    
    CATEGORIES = (
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('2.5BHK', '2.5BHK'),
        ('3BHK', '3BHK'),
        ('4BHK+', '4BHK+'),
    )

    CLIMATEZONES = (
        ('Hot & Dry', 'Hot & Dry'),
        ('Composite', 'Composite'),
        ('Warm & Humid', 'Warm & Humid'),
        ('Temperate', 'Temperate'),
        ('Cold', 'Cold'),
    )

    ORIENTATIONS = (
        ('North', 'North'),
        ('South', 'South'),
        ('East', 'East'),
        ('West', 'West'),
        ('North-East', 'North-East'),
        ('North-West', 'North-West'),
        ('South-East', 'South-East'),
        ('South-West', 'South-West'),         
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 200, null = True)
    acctype = models.TextField(max_length = 200, choices = TYPES, default = 'Choose Type...', null = True)
    address = models.CharField(max_length = 500, null = True)
    floorcount = models.IntegerField(default = 1, null = True)
    yourfloor = models.IntegerField(default = 0, null = True, blank = True)
    occupants = models.IntegerField(default = 1, null = True)
    area = models.IntegerField(default = 0, null = True)
    category = models.TextField(max_length = 200, choices = CATEGORIES, default = 'Choose BHK...', null = True)
    climatezone = models.TextField(max_length = 200, choices = CLIMATEZONES, default = 'Choose Climate Zone...', null = True)
    face = models.TextField(max_length = 200, choices = ORIENTATIONS, default = 'Choose Face Direction...', null = True)
    units = models.IntegerField(default = 0, null = True)
    billamt = models.IntegerField(default = 0, null = True)
    lastyr_units = models.CharField(max_length = 500, null = True)
    twoyrbfr_units = models.CharField(max_length = 500, null = True, blank = True)
    threeyrbfr_units = models.CharField(max_length = 500, null = True, blank = True)
    buildingsystems = models.ForeignKey(BuildingSystems, on_delete = models.CASCADE, null = True)
    wallassembly = models.ForeignKey(WallAssembly, on_delete = models.CASCADE, null = True)
    roofassembly = models.ForeignKey(RoofAssembly, on_delete = models.CASCADE, null = True)
    floorassembly = models.ForeignKey(FloorAssembly, on_delete = models.CASCADE, null = True)
    windowassembly = models.ForeignKey(WindowAssembly, on_delete = models.CASCADE, null = True)
    structuralassembly = models.ForeignKey(StructuralAssembly, on_delete = models.CASCADE, null = True)
    date_added = models.DateTimeField(auto_now_add = True)   

    def __str__(self):
        return self.name