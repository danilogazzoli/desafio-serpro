from .models import Paciente
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PacienteSerializer
from pickle import load
from sklearn.neural_network import MLPClassifier
from sklearn import preprocessing
import numpy as np
import pandas as pd

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all().order_by('id')
    serializer_class = PacienteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Paciente.objects.all().order_by('diagnostico')
        pk = self.request.parser_context.get('kwargs') 
        if len(pk):
            mlpmodel = self.load_model()
            queryset = queryset.filter(id = int(pk.get('pk')))
            hospital = list(queryset.values('hospital')[0].get('hospital'))[0]
            hospital = self.trata_hospital(hospital)
            idade = queryset.values('idade')[0].get('idade')
            sexo = queryset.values('sexo')[0].get('sexo')
            sexo = self.trata_sexo(sexo)
            tdp = queryset.values('TDP')[0].get('TDP')  
            tdp = 0 if tdp == None else tdp
            par = queryset.values('PAR')[0].get('PAR')
            par = 0 if par == None else par
            cs = queryset.values('CS')[0].get('CS') 
            cs = 0 if cs == None else cs
            asj = queryset.values('ASJ')[0].get('ASJ')
            asj = 0 if asj == None else asj
            ecg = queryset.values('ECG')[0].get('ECG') 
            ecg = 0 if ecg == None else ecg
            fcm = queryset.values('FCM')[0].get('FCM') 
            fcm = 0 if fcm == None else fcm
            aie = queryset.values('AIE')[0].get('AIE') 
            aie = 0 if aie == None else aie
            #dst = queryset.values('DST')[0].get('DST') 
            ist = queryset.values('IST')[0].get('IST') 
            ist = 0 if ist == None else ist
            nvp = queryset.values('NVP')[0].get('NVP')
            nvp = 0 if nvp == None else nvp
            talassemia = queryset.values('talassemia')[0].get('talassemia')
            talassemia = 0 if talassemia == None else talassemia
            
            '''
            'Idade', 'TDP', 'par_dummy', 'cs_dummy', 'asj_dummy', 'ecg_dummy',
            'fcm_dummy', 'aie_dummy', 'ist_dummy', 'nvp_dummy', 'talassemia_dummy',
            'sexo_dummy', 'hospital_dummy'
            '''

            dados = [idade, tdp, par, cs, asj, ecg, fcm, aie, ist, nvp, talassemia, sexo, hospital] 
            df = pd.DataFrame(dados)                               
            X = self.normaliza_dados(df).tolist()
            y_pred = mlpmodel.predict(np.array(X).T.tolist())

            queryset.update(diagnostico = y_pred[0])  
        return queryset       

    def load_model(self):
        return load(open('./model/mlpclassifier.pkl', 'rb'))    

    def trata_sexo(self, sexo):    
        return 1 if sexo == 'M' else 2

    def trata_hospital(self, hospital):
        value = 4
        if hospital == 'C':
            return 1
        elif hospital == 'H':
            return 2
        elif hospital == 'S':
            return 3    
        return value

    def normaliza_dados(self, dados):
        return preprocessing.MinMaxScaler().fit_transform(dados)



