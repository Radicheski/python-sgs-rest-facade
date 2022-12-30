from zeep import Client


class SOAPService:
    def __init__(self):
        self.__client__ = Client('https://www3.bcb.gov.br/sgspub/JSP/sgsgeral/FachadaWSSGS.wsdl')
        self.__service__ = self.__client__.service
        self.__factory__ = self.__client__.type_factory('http://DefaultNamespace')

    def getUltimosValoresSerieVO(self, in0, in1):
        return WSSerieVO(self.__service__.getUltimosValoresSerieVO(in0, in1))

    def getUltimoValorVO(self, in0):
        return WSSerieVO(self.__service__.getUltimoValorVO(in0))

    def getUltimoValorXML(self, in0):
        return self.__service__.getUltimoValorXML(in0)._value_1

    def getValor(self, in0, in1):
        return str(self.__service__.getValor(in0, in1)._value_1)

    def getValorEspecial(self, in0, in1, in2):
        return self.__service__.getValorEspecial(in0, in1, in2)

    def getValoresSeriesVO(self, in0, in1, in2):
        return [WSSerieVO(data).__dict__() for data in self.__service__.getValoresSeriesVO(in0, in1, in2)]

    def getValoresSeriesXML(self, in0, in1, in2):
        return self.__service__.getValoresSeriesXML(in0, in1, in2)._value_1

    def array_of_long(self, list):
        return self.__factory__.ArrayOfflong([int(valor) for valor in list.split(',')])


class WSSerieVO:
    def __init__(self, data):
        self.anoFim = data.anoFim
        self.anoInicio = data.anoInicio
        self.aviso = data.aviso._value_1
        self.diaFim = data.diaFim
        self.diaInicio = data.diaInicio
        self.especial = data.especial
        self.fonte = data.fonte._value_1
        self.fullName = data.fullName._value_1
        self.gestorProprietario = data.gestorProprietario._value_1
        self.mesFim = data.mesFim
        self.mesInicio = data.mesInicio
        self.nomeAbreviado = data.nomeAbreviado._value_1
        self.nomeCompleto = data.nomeCompleto._value_1
        self.oid = data.oid
        self.periodicidade = data.periodicidade._value_1
        self.periodicidadeSigla = data.periodicidadeSigla._value_1
        self.possuiBloqueios = data.possuiBloqueios
        self.publica = data.publica
        self.shortName = data.shortName._value_1
        self.ultimoValor = WSValorSerieVO(data.ultimoValor)
        self.unidadePadrao = data.unidadePadrao._value_1
        self.unidadePadraoIngles = data.unidadePadraoIngles._value_1
        self.valorDiaNaoUtil = data.valorDiaNaoUtil
        self.valores = [WSValorSerieVO(valor) for valor in data.valores]

    def __dict__(self):
        return {
            'anoFim': self.anoFim,
            'anoInicio': self.anoInicio,
            'aviso': self.aviso,
            'diaFim': self.diaFim,
            'diaInicio': self.diaInicio,
            'especial': self.especial,
            'fonte': self.fonte,
            'fullName': self.fullName,
            'gestorProprietario': self.gestorProprietario,
            'mesFim': self.mesFim,
            'mesInicio': self.mesInicio,
            'nomeAbreviado': self.nomeAbreviado,
            'nomeCompleto': self.nomeCompleto,
            'oid': self.oid,
            'periodicidade': self.periodicidade,
            'periodicidadeSigla': self.periodicidadeSigla,
            'possuiBloqueios': self.possuiBloqueios,
            'publica': self.publica,
            'shortName': self.shortName,
            'ultimoValor': self.ultimoValor.__dict__(),
            'unidadePadrao': self.unidadePadrao,
            'unidadePadraoIngles': self.unidadePadraoIngles,
            'valorDiaNaoUtil': self.valorDiaNaoUtil,
            'valores': [valor.__dict__() for valor in self.valores]
        }


class WSValorSerieVO:
    def __init__(self, data):
        self.ano = data.ano
        self.anoFim = data.anoFim
        self.bloqueado = data.bloqueado
        self.bloqueioLiberado = data.bloqueioLiberado
        self.dia = data.dia
        self.diaFim = data.diaFim
        self.mes = data.mes
        self.mesFim = data.mesFim
        self.oid = data.oid
        self.oidSerie = data.oidSerie
        self.svalor = data.svalor._value_1 if data.svalor is not None else None
        self.valor = data.valor._value_1 if data.valor is not None else None

    def __dict__(self):
        return {
            'ano': self.ano,
            'anoFim': self.anoFim,
            'bloqueado': self.bloqueado,
            'bloqueioLiberado': self.bloqueioLiberado,
            'dia': self.dia,
            'diaFim': self.diaFim,
            'mes': self.mes,
            'mesFim': self.mesFim,
            'oid': self.oid,
            'oidSerie': self.oidSerie,
            'svalor': self.svalor,
            'valor': self.valor
        }
