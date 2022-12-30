from flask import Flask, request, abort

from SOAPService import SOAPService


def create_application():

    application = Flask(__name__)
    service = SOAPService()

    @application.route('/getUltimosValoresSerieVO')
    def getUltimosValoresSerieVO():
        in0, in1 = get_args('in0,in1')
        return service.getUltimosValoresSerieVO(in0, in1).__dict__()

    @application.route('/getUltimoValorVO')
    def getUltimoValorVO():
        in0 = get_args('in0')
        return service.getUltimoValorVO(in0).__dict__()

    @application.route('/getUltimoValorXML')
    def getUltimoValorXML():
        in0 = get_args('in0')
        return service.getUltimoValorXML(in0), {'Content-Type': 'application/xml'}

    @application.route('/getValor')
    def getValor():
        in0, in1 = get_args('in0,in1')
        return service.getValor(in0, in1), {'Content-Type': 'text/plain'}

    @application.route('/getValorEspecial')
    def getValorEspecial():
        abort(405)

    @application.route('/getValoresSeriesVO')
    def getValoresSeriesVO():
        in0, in1, in2 = get_args('in0,in1,in2')
        in0 = service.array_of_long(in0)
        return service.getValoresSeriesVO(in0, in1, in2)

    @application.route('/getValoresSeriesXML')
    def getValoresSeriesXML():
        in0, in1, in2 = get_args('in0,in1,in2')
        in0 = service.array_of_long(in0)
        return service.getValoresSeriesXML(in0, in1, in2), {'Content-Type': 'application/xml'}

    def get_args(data):
        args = request.args.get
        new_data = data.split(',')
        if len(new_data) == 1:
            return args(new_data[0])
        else:
            return [args(arg) for arg in new_data]

    return application
