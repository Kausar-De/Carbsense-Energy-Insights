from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password1', 'password2']
        labels = {
            'username': _('Account Username'),
            'email': _('Email Address'),
            'first_name': _('Building Name'),
        }

class LoginForm(forms.Form):
    username = forms.CharField(label = 'Username', max_length = 100)
    password = forms.CharField(label = 'Password', max_length = 100, widget = forms.PasswordInput())

class BuildingForm(ModelForm):
    class Meta:
        model = Building
        exclude = ['user', 'buildingsystems', 'wallassembly', 'roofassembly', 'floorassembly', 'windowassembly', 'structuralassembly', 'date_added']
        labels = {
            'name': _('Flat Name'),
            'acctype': _('Type of Accommodation'),
            'address': _('Full Address with Pin Code'),
            'floorcount': _('Number of Floors'),
            'yourfloor': _('Your Floor (Keep 0 for House)'),
            'occupants': _('No. of Occupants'),
            'area': _('Area (Sq. m.)'),
            'category': _('Category (BHK)'),            
            'climatezone': _('Climate Zone'),
            'face': _('Which Direction does your Building Face?'),
            'units': _('Total Billed Units Last Year'),
            'billamt': _('Total Electricity Bill Last Year'),
            'lastyr_units': _('Monthwise Billed Units Last Year'),
            'twoyrbfr_units': _('(Optional) Monthwise Billed Units 2 Years Ago'),
            'threeyrbfr_units': _('(Optional) Monthwise Billed Units 3 Years Ago'),
        }

class BuildingSystemsForm(ModelForm):
    class Meta:
        model = BuildingSystems
        fields = ['hvacsystem', 'starrating', 'setpoint', 'totaltr', 'appls', 'otherappls']
        labels = {
            'hvacsystem': _('Primary HVAC System'),
            'starrating': _('HVAC Star Rating (Average in Case of Variance)'),
            'setpoint': _('Thermal Comfort Set Point (Celsius)'),
            'totaltr': _('Total Tonnage Rating (TR)'),
            'appls': _('Appliances Used'),
            'otherappls': _('Other Appliances (Please write one after another, comma-separated)'),
        }

class WallAssemblyForm(ModelForm):
    class Meta:
        model = WallAssembly
        fields = ['wallarea', 'wassembly', 'wallinsulation', 'walltile']
        labels = {
            'wallarea': _('Wall Area (Sq. m)'),
            'wassembly': _('Wall Assembly'),
            'wallinsulation': _('Insulation'),
            'walltile': _('Tiles'),
        }

class RoofAssemblyForm(ModelForm):
    class Meta:
        model = RoofAssembly
        fields = ['roofarea', 'rassembly', 'roofinsulation', 'rooftile']
        labels = {
            'roofarea': _('Roof Area (Sq. m)'),
            'rassembly': _('Roof Assembly'),
            'roofinsulation': _('Insulation'),
            'rooftile': _('Tiles'),
        }

class FloorAssemblyForm(ModelForm):
    class Meta:
        model = FloorAssembly
        fields = ['floorarea', 'fassembly']
        labels = {
            'floorarea': _('Floor Area (Sq. m)'),
            'fassembly': _('Floor Assembly'),
        }

class WindowAssemblyForm(ModelForm):
    class Meta:
        model = WindowAssembly
        fields = ['windowarea', 'glass', 'frame']
        labels = {
            'windowarea': _('Window Area (Sq. m)'),
            'glass': _('Window Glass Type'),
            'frame': _('Window Frame Type'),
        }

class StructuralAssemblyForm(ModelForm):
    class Meta:
        model = StructuralAssembly
        fields = ['structuralarea', 'sassembly']
        labels = {
            'structuralarea': _('Structural Area (Sq. m)'),
            'sassembly': _('Structural Assembly'),
        }