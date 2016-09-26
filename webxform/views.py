from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hola a todos")

class FeriadoViewSet(viewsets.ModelViewSet):
    """
    ## En este objeto se aprueban los feriados
    Los feriados aprobados son antes sugeridos por el API REST de FERIADOS que entrega tentativamente todos los feriados del año
    """
    queryset = Feriado.objects.all()
    serializer_class = FeriadoSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('descripcion', '=fecha',)
    ordering_fields = '__all__'
