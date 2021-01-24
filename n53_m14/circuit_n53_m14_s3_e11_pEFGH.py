import cirq
import numpy as np

QUBIT_ORDER = [
    cirq.GridQubit(0, 5),
    cirq.GridQubit(0, 6),
    cirq.GridQubit(1, 4),
    cirq.GridQubit(1, 5),
    cirq.GridQubit(1, 6),
    cirq.GridQubit(1, 7),
    cirq.GridQubit(2, 4),
    cirq.GridQubit(2, 5),
    cirq.GridQubit(2, 6),
    cirq.GridQubit(2, 7),
    cirq.GridQubit(2, 8),
    cirq.GridQubit(3, 2),
    cirq.GridQubit(3, 3),
    cirq.GridQubit(3, 4),
    cirq.GridQubit(3, 5),
    cirq.GridQubit(3, 6),
    cirq.GridQubit(3, 7),
    cirq.GridQubit(3, 8),
    cirq.GridQubit(3, 9),
    cirq.GridQubit(4, 1),
    cirq.GridQubit(4, 2),
    cirq.GridQubit(4, 3),
    cirq.GridQubit(4, 4),
    cirq.GridQubit(4, 5),
    cirq.GridQubit(4, 6),
    cirq.GridQubit(4, 7),
    cirq.GridQubit(4, 8),
    cirq.GridQubit(4, 9),
    cirq.GridQubit(5, 0),
    cirq.GridQubit(5, 1),
    cirq.GridQubit(5, 2),
    cirq.GridQubit(5, 3),
    cirq.GridQubit(5, 4),
    cirq.GridQubit(5, 5),
    cirq.GridQubit(5, 6),
    cirq.GridQubit(5, 7),
    cirq.GridQubit(5, 8),
    cirq.GridQubit(6, 1),
    cirq.GridQubit(6, 2),
    cirq.GridQubit(6, 3),
    cirq.GridQubit(6, 4),
    cirq.GridQubit(6, 5),
    cirq.GridQubit(6, 6),
    cirq.GridQubit(6, 7),
    cirq.GridQubit(7, 2),
    cirq.GridQubit(7, 3),
    cirq.GridQubit(7, 4),
    cirq.GridQubit(7, 5),
    cirq.GridQubit(7, 6),
    cirq.GridQubit(8, 3),
    cirq.GridQubit(8, 4),
    cirq.GridQubit(8, 5),
    cirq.GridQubit(9, 4),
]

CIRCUIT = cirq.Circuit(
    [
        cirq.Moment(
            operations=[
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 9)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 0)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 1)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(9, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 0.41931766688684124).on(cirq.GridQubit(1, 4)),
                cirq.rz(np.pi * -0.5244847063764291).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * 0.4023568071295625).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * 0.08365382632516613).on(cirq.GridQubit(1, 7)),
                cirq.rz(np.pi * -0.8200390213852617).on(cirq.GridQubit(2, 4)),
                cirq.rz(np.pi * 0.7684522607989545).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * 0.5631104928155226).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * -0.12013053520058192).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * -0.3219578980700819).on(cirq.GridQubit(3, 2)),
                cirq.rz(np.pi * 0.36226390752439264).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * -0.25081354785192633).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * 0.3447540847806523).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -0.10811808740177511).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 0.01414321107307475).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * -0.7049805427558093).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * 0.688746173527078).on(cirq.GridQubit(3, 9)),
                cirq.rz(np.pi * -0.9095610143846702).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * 0.8741280226227549).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * 0.03160349210299197).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * 0.3800384580192153).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * -0.5773867869996285).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * -0.9281866430802291).on(cirq.GridQubit(4, 9)),
                cirq.rz(np.pi * 0.7692996538435087).on(cirq.GridQubit(5, 0)),
                cirq.rz(np.pi * -0.7267964853111832).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * -0.23067767363250857).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * 0.2917665024875207).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -0.34084434700742594).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 0.41413766339092745).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * 0.3044942712490584).on(cirq.GridQubit(5, 6)),
                cirq.rz(np.pi * -0.1478481894878204).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * -0.7096067302991369).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * 0.5635969811667613).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * -0.5426941816874842).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * 0.5901647453099161).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * -0.9450968665474545).on(cirq.GridQubit(7, 2)),
                cirq.rz(np.pi * -0.9756183416395792).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * 0.9608569646339465).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * -0.9215396770596501).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * -0.19068624799437317).on(cirq.GridQubit(8, 4)),
                cirq.rz(np.pi * 0.20478021276969885).on(cirq.GridQubit(8, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5553516266448077, phi=0.47754343999179444).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5513695622863453, phi=0.5525497751179018).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(1, 7)
                ),
                cirq.FSimGate(theta=1.5920107910314218, phi=0.495277170657118).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.4850359189030258, phi=0.5432026764541129).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.5586373808029026, phi=0.46099332137061977).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(3, 3)
                ),
                cirq.FSimGate(theta=1.5468483989685475, phi=0.5246739758652749).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5358532152984938, phi=0.5376855016240104).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.4939596076472883, phi=0.6686288484482796).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(3, 9)
                ),
                cirq.FSimGate(theta=1.548255653119813, phi=0.48307337635991665).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.5314832643812344, phi=0.47518174639867017).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.5608608535579012, phi=0.6668893914368428).on(
                    cirq.GridQubit(4, 8), cirq.GridQubit(4, 9)
                ),
                cirq.FSimGate(theta=1.5676963775554011, phi=0.48299203630424015).on(
                    cirq.GridQubit(5, 0), cirq.GridQubit(5, 1)
                ),
                cirq.FSimGate(theta=1.4807002448035869, phi=0.48033134534938904).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5479898631344362, phi=0.5021140664341368).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.5508083238882544, phi=0.5088503466820911).on(
                    cirq.GridQubit(5, 6), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.507155881326315, phi=0.4773896323482684).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.5602578123868405, phi=0.5276499696880497).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.5485996563720543, phi=0.4873901665634375).on(
                    cirq.GridQubit(7, 2), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.5468701891071555, phi=0.47909090411139443).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(7, 5)
                ),
                cirq.FSimGate(theta=1.5253448615592025, phi=0.5174324533286649).on(
                    cirq.GridQubit(8, 4), cirq.GridQubit(8, 5)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 0.051908779557838985).on(cirq.GridQubit(1, 4)),
                cirq.rz(np.pi * -0.1570758190474269).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * 0.8610097418325555).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * -0.37499910837782696).on(cirq.GridQubit(1, 7)),
                cirq.rz(np.pi * -0.8295068032091273).on(cirq.GridQubit(2, 4)),
                cirq.rz(np.pi * 0.77792004262282).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * 0.9326150960969569).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * -0.48963513848201595).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * 0.6849084620084369).on(cirq.GridQubit(3, 2)),
                cirq.rz(np.pi * -0.6446024525541262).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * 0.8093654507593696).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * -0.7154249138306435).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 0.790256963081442).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * -0.8842318394101424).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * 0.3820822126781918).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * -0.398316581906923).on(cirq.GridQubit(3, 9)),
                cirq.rz(np.pi * -0.9863895660146618).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * 0.9509565742527464).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * 0.7018374885946309).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -0.2901955384724235).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * 0.9965022064919533).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * -0.5020756365718106).on(cirq.GridQubit(4, 9)),
                cirq.rz(np.pi * -0.15161750310625308).on(cirq.GridQubit(5, 0)),
                cirq.rz(np.pi * 0.19412067163857846).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * 0.7793034013947722).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * -0.7182145725397602).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * 0.06067384617490545).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 0.01261947020859607).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * 0.737067039527071).on(cirq.GridQubit(5, 6)),
                cirq.rz(np.pi * -0.5804209577658329).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * 0.6562755406709511).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * -0.8022852898033268).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * -0.0930980442694234).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * 0.14056860789185535).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * -0.2585088528831879).on(cirq.GridQubit(7, 2)),
                cirq.rz(np.pi * 0.3377936446961546).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * -0.135474414104308).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * 0.17479170167860442).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * -0.026568259843865707).on(cirq.GridQubit(8, 4)),
                cirq.rz(np.pi * 0.04066222461919139).on(cirq.GridQubit(8, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 9)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 1)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 8)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 9)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 0)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 0.11375007762837216).on(cirq.GridQubit(0, 5)),
                cirq.rz(np.pi * -0.06313845739191101).on(cirq.GridQubit(0, 6)),
                cirq.rz(np.pi * 0.34183655081171865).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * -0.253806831541243).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * -0.5009252575625629).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * 0.48343550296163795).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * 0.07007131389953448).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * -0.527645581267553).on(cirq.GridQubit(2, 8)),
                cirq.rz(np.pi * -0.3315914405750577).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 0.33544142367836044).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * -0.9454637962195104).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * 0.9178863697105869).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * -0.7352522062843072).on(cirq.GridQubit(4, 1)),
                cirq.rz(np.pi * 0.7778096859239129).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * 0.13519405943588042).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -0.19288538126402574).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * 0.9150386196915928).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -0.7316500525675395).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -0.47076213796483773).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * 0.4357745053405362).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * -0.9141091333756286).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * 0.9287042443481173).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * 0.7114770549258108).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -0.6063307370031102).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * -0.7619241029024945).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * 0.7877856802045439).on(cirq.GridQubit(5, 8)),
                cirq.rz(np.pi * 0.9439252177364551).on(cirq.GridQubit(6, 1)),
                cirq.rz(np.pi * -0.7145507812033878).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * 0.6867977635374927).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * -0.7097303210783701).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * -0.7838571021425398).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * 0.7873240565722553).on(cirq.GridQubit(6, 6)),
                cirq.rz(np.pi * 0.6997105520527618).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * 0.8737022142720108).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * -0.7573337290786126).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * 0.320755520391696).on(cirq.GridQubit(7, 6)),
                cirq.rz(np.pi * 0.9539871150754136).on(cirq.GridQubit(8, 3)),
                cirq.rz(np.pi * -0.9834209135111338).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5390237928795745, phi=0.5165270526693762).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(0, 6)
                ),
                cirq.FSimGate(theta=1.6504170890091214, phi=0.5364505757789483).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.568670761625143, phi=0.5437849784272266).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.5465254433686004, phi=-5.727450888059412).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(2, 8)
                ),
                cirq.FSimGate(theta=1.5381480272852108, phi=0.6090669301824796).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.5830570458423034, phi=0.5523056687078169).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.546350568481482, phi=0.4879631369282715).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.5326394193330342, phi=0.4395048201320801).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5745817206538912, phi=0.5078468553250708).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5287959808590572, phi=0.5477757594186843).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.4855370661448744, phi=0.5162805489497694).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.527373036078513, phi=0.5115160136560014).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.4000192936015627, phi=0.45553928758281914).on(
                    cirq.GridQubit(5, 7), cirq.GridQubit(5, 8)
                ),
                cirq.FSimGate(theta=1.5800842999687046, phi=0.45282693980374283).on(
                    cirq.GridQubit(6, 1), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.518789513006022, phi=0.48179520284759936).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.529911511830527, phi=0.5594440380846348).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(6, 6)
                ),
                cirq.FSimGate(theta=1.4246757982684226, phi=0.4944809315999467).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.5296678467857068, phi=0.5740197418485297).on(
                    cirq.GridQubit(7, 5), cirq.GridQubit(7, 6)
                ),
                cirq.FSimGate(theta=1.4984631547270855, phi=0.49206955088399174).on(
                    cirq.GridQubit(8, 3), cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -0.24713448069352695).on(cirq.GridQubit(0, 5)),
                cirq.rz(np.pi * 0.2977461009299881).on(cirq.GridQubit(0, 6)),
                cirq.rz(np.pi * 0.11546621397053439).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * -0.027436494700057646).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * -0.09607671310061273).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * 0.07858695849968671).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * -0.6083890652764492).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * 0.1508147979084304).on(cirq.GridQubit(2, 8)),
                cirq.rz(np.pi * -0.8130558727798829).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 0.8169058558831868).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * -0.9627146107981173).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * 0.9351371842891939).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * 0.24762069711205567).on(cirq.GridQubit(4, 1)),
                cirq.rz(np.pi * -0.20506321747245002).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * -0.6312954156926376).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * 0.5736040938644923).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * 0.14131606422859974).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * 0.04207250289545421).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -0.7651203501001616).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * 0.7301327174758601).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * -0.06877898083829766).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * 0.08337409181078692).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * 0.37496245184383764).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -0.2698161339211372).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * -0.3053580048006373).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * 0.3312195821026862).on(cirq.GridQubit(5, 8)),
                cirq.rz(np.pi * 0.2745466572666991).on(cirq.GridQubit(6, 1)),
                cirq.rz(np.pi * -0.045172220733631814).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * 0.8781886531345134).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * -0.901121210675391).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * -0.43802432836821265).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * 0.4414912827979294).on(cirq.GridQubit(6, 6)),
                cirq.rz(np.pi * 0.12077871036671557).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * -0.547365944041943).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * 0.5633683710057419).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * -0.9999465796926585).on(cirq.GridQubit(7, 6)),
                cirq.rz(np.pi * 0.0757106337473065).on(cirq.GridQubit(8, 3)),
                cirq.rz(np.pi * -0.10514443218302676).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 1)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 2)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 9)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 0)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 1)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 0.8847189116150218).on(cirq.GridQubit(0, 5)),
                cirq.rz(np.pi * -0.9451632561930864).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * 0.41133373211619956).on(cirq.GridQubit(0, 6)),
                cirq.rz(np.pi * -0.5342194922140218).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * -0.20986571907665558).on(cirq.GridQubit(2, 4)),
                cirq.rz(np.pi * 0.24219101652310202).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * -0.007550715881230289).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * 0.012271609652291906).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 0.4093563861263822).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * -0.564998817327963).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * -0.21076950038099565).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * -0.20953797807355298).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * -0.863752107592455).on(cirq.GridQubit(2, 8)),
                cirq.rz(np.pi * 0.8735815153495756).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * -0.7012318802461477).on(cirq.GridQubit(4, 1)),
                cirq.rz(np.pi * 0.6907736014655701).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * 0.6428024164125671).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * -0.6526026044480875).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * 0.7357092441723263).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -0.6663598372207183).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * 0.5627609731422828).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -0.5459326631464406).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 0.1196352690665477).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * 0.33034016823315965).on(cirq.GridQubit(5, 6)),
                cirq.rz(np.pi * -0.8684844557185236).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * 0.8394083000297652).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * 0.0544976586180204).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * -0.017824531864314853).on(cirq.GridQubit(5, 8)),
                cirq.rz(np.pi * 0.6446295141685076).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * -0.6303772327002933).on(cirq.GridQubit(7, 2)),
                cirq.rz(np.pi * 0.4206396024198002).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * -0.5196833746285892).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * 0.6127113773811597).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * 0.9187972148732992).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * -0.17899797923472524).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * 0.09385166828012863).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * -0.9112153327744746).on(cirq.GridQubit(6, 6)),
                cirq.rz(np.pi * 0.8090547106077676).on(cirq.GridQubit(7, 6)),
                cirq.rz(np.pi * 0.8768876214209625).on(cirq.GridQubit(8, 4)),
                cirq.rz(np.pi * -0.821121705997487).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.4660264742068387, phi=0.4703035018096913).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5595675891930325, phi=0.5029212805853078).on(
                    cirq.GridQubit(0, 6), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.5057896135518938, phi=0.5276098280644357).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.544885207693353, phi=0.5728958894277337).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.521825393645828, phi=0.5386243364775084).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.568786150985278, phi=0.5431362030835812).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.6068421332516425, phi=0.49425168255721214).on(
                    cirq.GridQubit(2, 8), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.5926635714606605, phi=0.49518543009178106).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(5, 1)
                ),
                cirq.FSimGate(theta=1.4823586616735414, phi=0.52880608763343).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.5878491175464968, phi=0.4879472611318097).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5390712580125911, phi=0.5384288567835004).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.5700853308915463, phi=0.46400287842866444).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(5, 6)
                ),
                cirq.FSimGate(theta=1.5356042072853593, phi=0.5206952948829173).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.6447139280388123, phi=0.46839573172584353).on(
                    cirq.GridQubit(4, 8), cirq.GridQubit(5, 8)
                ),
                cirq.FSimGate(theta=1.5383311289896362, phi=0.5127577213621436).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(7, 2)
                ),
                cirq.FSimGate(theta=1.5052207980661314, phi=0.5125556567248526).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.3373234810096835, phi=-5.709279866705804).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.5012621338159504, phi=0.5119166112294746).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(7, 5)
                ),
                cirq.FSimGate(theta=1.3909778451077717, phi=0.4282244069641004).on(
                    cirq.GridQubit(6, 6), cirq.GridQubit(7, 6)
                ),
                cirq.FSimGate(theta=1.5178422515660452, phi=0.47308231008168455).on(
                    cirq.GridQubit(8, 4), cirq.GridQubit(9, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 0.3139098946818507).on(cirq.GridQubit(0, 5)),
                cirq.rz(np.pi * -0.3743542392599153).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * -0.41016910712852483).on(cirq.GridQubit(0, 6)),
                cirq.rz(np.pi * 0.28728334703070263).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * 0.8953407528264041).on(cirq.GridQubit(2, 4)),
                cirq.rz(np.pi * -0.8630154553799576).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * 0.6889606163529288).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * -0.6842397225818673).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -0.06535370176280349).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * -0.0902887294387773).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * -0.8598246599495762).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * 0.4395171814950276).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * -0.4674352284028531).on(cirq.GridQubit(2, 8)),
                cirq.rz(np.pi * 0.4772646361599737).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * 0.9559895825475485).on(cirq.GridQubit(4, 1)),
                cirq.rz(np.pi * -0.9664478613281261).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * 0.7822757858947289).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * -0.7920759739302504).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * 0.9451129448425614).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -0.8757635378909534).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * 0.3873158498511822).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -0.37048753985533894).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 0.736785785759294).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -0.28681034845958553).on(cirq.GridQubit(5, 6)),
                cirq.rz(np.pi * 0.9681726412910321).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * -0.9972487969797906).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * 0.9049875554472292).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * -0.868314428693523).on(cirq.GridQubit(5, 8)),
                cirq.rz(np.pi * 0.007323934140581554).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * 0.006928347327632615).on(cirq.GridQubit(7, 2)),
                cirq.rz(np.pi * -0.8523217213031842).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * 0.7532779490943952).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * 0.4994915177950534).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * -0.967982925540594).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * 0.7666266991271272).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * -0.8517730100817239).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * -0.8079753683223797).on(cirq.GridQubit(6, 6)),
                cirq.rz(np.pi * 0.7058147461556727).on(cirq.GridQubit(7, 6)),
                cirq.rz(np.pi * -0.609869920469322).on(cirq.GridQubit(8, 4)),
                cirq.rz(np.pi * 0.6656358358927976).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 9)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 1)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 9)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 0)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 1)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -0.2856444790781417).on(cirq.GridQubit(1, 4)),
                cirq.rz(np.pi * 0.32590032116655776).on(cirq.GridQubit(2, 4)),
                cirq.rz(np.pi * -0.7582760403822875).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * 0.7689587550081207).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * 0.3797766360230081).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * -0.27496385627578723).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * -0.956000988901924).on(cirq.GridQubit(1, 7)),
                cirq.rz(np.pi * 0.4930108935498376).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * 0.7722636962137414).on(cirq.GridQubit(3, 2)),
                cirq.rz(np.pi * -0.7326132648717611).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * 0.7131893041762983).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * -0.7956039791600531).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -0.0038864613618523843).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 0.06732167016995634).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -0.8320649037817693).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 0.821619576547285).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -0.9570510890995485).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * 0.9306347023529243).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * 0.12904916136140993).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * -0.12186525524919878).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * -0.6632736012309495).on(cirq.GridQubit(3, 9)),
                cirq.rz(np.pi * 0.9564298380051538).on(cirq.GridQubit(4, 9)),
                cirq.rz(np.pi * -0.3770162533552355).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * 0.11220317629980596).on(cirq.GridQubit(6, 1)),
                cirq.rz(np.pi * -0.6579118949759303).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * 0.6516276228841108).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * -0.8616623066511218).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * 0.8736862717036904).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * -0.13852585564118036).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 0.07090336842917003).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * -0.06785878232924142).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * 0.1039270616968357).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * -0.5227269853764346).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * 0.7198788467722416).on(cirq.GridQubit(6, 7)),
                cirq.rz(np.pi * 0.3618609198281597).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * -0.36011133542346546).on(cirq.GridQubit(8, 3)),
                cirq.rz(np.pi * 0.6681117975800143).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * -0.5188730640654514).on(cirq.GridQubit(8, 4)),
                cirq.rz(np.pi * -0.4540007131210775).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * 0.45895465189993395).on(cirq.GridQubit(8, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5496057658133178, phi=0.5393238727561925).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(2, 4)
                ),
                cirq.FSimGate(theta=1.5258573993033773, phi=0.5301963978982887).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.5999105816064956, phi=0.47191843749859924).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.4104416482963105, phi=-5.734064803424554).on(
                    cirq.GridQubit(1, 7), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.5319225163456216, phi=0.49105711881659464).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.465404631262162, phi=0.4878297652759932).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.5467222527282019, phi=0.5068034228124387).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.5496604814896044, phi=0.5531983372087332).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5524939155045483, phi=0.5566693071275687).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.363213412756342, phi=0.7994150767548583).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.5284460090316794, phi=0.5432682295494672).on(
                    cirq.GridQubit(3, 9), cirq.GridQubit(4, 9)
                ),
                cirq.FSimGate(theta=1.3166607142943418, phi=0.40127686655135986).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(6, 1)
                ),
                cirq.FSimGate(theta=1.5594498457697554, phi=0.5290555375763617).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.5125120660103082, phi=0.5195553885293336).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.54223977200166, phi=0.47914474770071624).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.6074361272506783, phi=0.4906717148713765).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.533964395594986, phi=0.47457535225216274).on(
                    cirq.GridQubit(5, 7), cirq.GridQubit(6, 7)
                ),
                cirq.FSimGate(theta=1.5001433000839564, phi=0.6605028795204214).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(8, 3)
                ),
                cirq.FSimGate(theta=1.640026880988053, phi=0.4976366432039147).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(8, 4)
                ),
                cirq.FSimGate(theta=1.5423122824843978, phi=0.7792646973911541).on(
                    cirq.GridQubit(7, 5), cirq.GridQubit(8, 5)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 0.44673783899379227).on(cirq.GridQubit(1, 4)),
                cirq.rz(np.pi * -0.40648199690537623).on(cirq.GridQubit(2, 4)),
                cirq.rz(np.pi * 0.2576636694289519).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * -0.24698095480311924).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * -0.47619936366296567).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * 0.5810121434101866).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * 0.16975416096994816).on(cirq.GridQubit(1, 7)),
                cirq.rz(np.pi * -0.6327442563220345).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * -0.014958604688800763).on(cirq.GridQubit(3, 2)),
                cirq.rz(np.pi * 0.05460903603078322).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * -0.46983934661684096).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * 0.3874246716330862).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -0.5963938707109903).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 0.6598290795190942).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * 0.5509757560926581).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * -0.5614210833271425).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * 0.25909495164296076).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * -0.28551133838958487).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * -0.02084373831637758).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * 0.028027644428588735).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * -0.04796595713070231).on(cirq.GridQubit(3, 9)),
                cirq.rz(np.pi * 0.3411221939049066).on(cirq.GridQubit(4, 9)),
                cirq.rz(np.pi * -0.4133801672196382).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * 0.14856709016420866).on(cirq.GridQubit(6, 1)),
                cirq.rz(np.pi * -0.29619709050093573).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * 0.28991281840911626).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * -0.14199585061799003).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * 0.15401981567055759).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * 0.8372241024842001).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * -0.9048465896962105).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * 0.8556109031121308).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * -0.8195426237445366).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * 0.7816115848182801).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * -0.5844597234224731).on(cirq.GridQubit(6, 7)),
                cirq.rz(np.pi * -0.9589657882666015).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * 0.9607153726712957).on(cirq.GridQubit(8, 3)),
                cirq.rz(np.pi * 0.3025501604047683).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * -0.15331142689020552).on(cirq.GridQubit(8, 4)),
                cirq.rz(np.pi * -0.6177061809814685).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * 0.6226601197603249).on(cirq.GridQubit(8, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 8)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 2)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 9)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 0)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 1)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 1)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 2)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 0.5713176668868711).on(cirq.GridQubit(1, 4)),
                cirq.rz(np.pi * -0.6764847063764583).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * -0.12164319287044913).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * 0.6076538263251786).on(cirq.GridQubit(1, 7)),
                cirq.rz(np.pi * -0.6760390213851921).on(cirq.GridQubit(2, 4)),
                cirq.rz(np.pi * 0.6244522607988843).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * -0.024889507184432575).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * 0.46786946479937275).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * -0.38995789807013737).on(cirq.GridQubit(3, 2)),
                cirq.rz(np.pi * 0.4302639075244475).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * 0.6331864521479956).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * -0.5392459152192696).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 0.41188191259812523).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * -0.5058567889268256).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * 0.8550194572441533).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * -0.8712538264728841).on(cirq.GridQubit(3, 9)),
                cirq.rz(np.pi * -0.7575610143846411).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * 0.7221280226227255).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -0.2683965078969558).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * 0.6800384580191632).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * 0.4786132130003544).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * 0.015813356919784544).on(cirq.GridQubit(4, 9)),
                cirq.rz(np.pi * 0.32129965384351167).on(cirq.GridQubit(5, 0)),
                cirq.rz(np.pi * -0.2787964853111868).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * 0.8813223263674578).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * -0.8202334975124456).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * 0.40315565299267003).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * -0.32986233660916897).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * -0.06750572875092396).on(cirq.GridQubit(5, 6)),
                cirq.rz(np.pi * 0.22415181051216204).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * -0.9256067302991097).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * 0.7795969811667348).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * -0.5412908918380754).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * 0.5887614554605067).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * 0.9869031334524914).on(cirq.GridQubit(7, 2)),
                cirq.rz(np.pi * -0.9076183416395242).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * -0.515143035366042).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * 0.5544603229403375).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * -0.9426862479944299).on(cirq.GridQubit(8, 4)),
                cirq.rz(np.pi * 0.9567802127697567).on(cirq.GridQubit(8, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5553516266448077, phi=0.47754343999179444).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5513695622863453, phi=0.5525497751179018).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(1, 7)
                ),
                cirq.FSimGate(theta=1.5920107910314218, phi=0.495277170657118).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.4850359189030258, phi=0.5432026764541129).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.5586373808029026, phi=0.46099332137061977).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(3, 3)
                ),
                cirq.FSimGate(theta=1.5468483989685475, phi=0.5246739758652749).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5358532152984938, phi=0.5376855016240104).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.4939596076472883, phi=0.6686288484482796).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(3, 9)
                ),
                cirq.FSimGate(theta=1.548255653119813, phi=0.48307337635991665).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.5314832643812344, phi=0.47518174639867017).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.5608608535579012, phi=0.6668893914368428).on(
                    cirq.GridQubit(4, 8), cirq.GridQubit(4, 9)
                ),
                cirq.FSimGate(theta=1.5676963775554011, phi=0.48299203630424015).on(
                    cirq.GridQubit(5, 0), cirq.GridQubit(5, 1)
                ),
                cirq.FSimGate(theta=1.4807002448035869, phi=0.48033134534938904).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5479898631344362, phi=0.5021140664341368).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.5508083238882544, phi=0.5088503466820911).on(
                    cirq.GridQubit(5, 6), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.507155881326315, phi=0.4773896323482684).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.5602578123868405, phi=0.5276499696880497).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.5485996563720543, phi=0.4873901665634375).on(
                    cirq.GridQubit(7, 2), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.5468701891071555, phi=0.47909090411139443).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(7, 5)
                ),
                cirq.FSimGate(theta=1.5253448615592025, phi=0.5174324533286649).on(
                    cirq.GridQubit(8, 4), cirq.GridQubit(8, 5)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -0.10009122044219096).on(cirq.GridQubit(1, 4)),
                cirq.rz(np.pi * -0.00507581904739744).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * -0.6149902581674315).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * -0.898999108377839).on(cirq.GridQubit(1, 7)),
                cirq.rz(np.pi * -0.9735068032091966).on(cirq.GridQubit(2, 4)),
                cirq.rz(np.pi * 0.9219200426228898).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * -0.47938490390308813).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * 0.9223648615180289).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * 0.7529084620084919).on(cirq.GridQubit(3, 2)),
                cirq.rz(np.pi * -0.7126024525541818).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * -0.07463454924055278).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * 0.16857508616927774).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 0.2702569630815419).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * -0.3642318394102423).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * 0.8220822126782295).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * -0.8383165819069602).on(cirq.GridQubit(3, 9)),
                cirq.rz(np.pi * 0.8616104339853083).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * -0.8970434257472238).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -0.9981625114054211).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -0.590195538472372).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * -0.059497793508031915).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * 0.5539243634281709).on(cirq.GridQubit(4, 9)),
                cirq.rz(np.pi * 0.2963824968937429).on(cirq.GridQubit(5, 0)),
                cirq.rz(np.pi * -0.253879328361418).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * -0.332696598605194).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * 0.3937854274602063).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -0.6833261538251911).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 0.7566194702086922).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * -0.8909329604729468).on(cirq.GridQubit(5, 6)),
                cirq.rz(np.pi * -0.9524209577658151).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * 0.8722755406709255).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * 0.9817147101966996).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * -0.09450133411883332).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * 0.1419718977412647).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * -0.19050885288313363).on(cirq.GridQubit(7, 2)),
                cirq.rz(np.pi * 0.26979364469610084).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * -0.6594744141043198).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * 0.6987917016786154).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * 0.7254317401561927).on(cirq.GridQubit(8, 4)),
                cirq.rz(np.pi * -0.7113377753808658).on(cirq.GridQubit(8, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 8)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 9)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 9)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 0)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(9, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 0.2657500776284017).on(cirq.GridQubit(0, 5)),
                cirq.rz(np.pi * -0.21513845739194115).on(cirq.GridQubit(0, 6)),
                cirq.rz(np.pi * -0.7581634491883068).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * 0.8461931684587847).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * -0.9329252575626394).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * 0.9154355029617134).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * 0.2860713138995072).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * -0.7436455812675269).on(cirq.GridQubit(2, 8)),
                cirq.rz(np.pi * 0.8644085594250173).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -0.8605585763217156).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 0.30653620378054636).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * -0.3341136302894698).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * -0.3552522062842347).on(cirq.GridQubit(4, 1)),
                cirq.rz(np.pi * 0.3978096859238381).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * -0.9808059405641975).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * 0.9231146187360522).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -0.9249613803084177).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -0.8916500525675272).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -0.3307621379648787).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * 0.29577450534057825).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * 0.20189086662444905).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * -0.18729575565196036).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * 0.9314770549257639).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -0.8263307370030635).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 0.638075897097479).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * -0.6122143197954307).on(cirq.GridQubit(5, 8)),
                cirq.rz(np.pi * 0.1999252177363589).on(cirq.GridQubit(6, 1)),
                cirq.rz(np.pi * 0.029449218796708948).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * -0.4266055263118835).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * 0.403672968771006).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * 0.6361428978574669).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * -0.6326759434277502).on(cirq.GridQubit(6, 6)),
                cirq.rz(np.pi * -0.5642894479472337).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * 0.13770221427200624).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * -0.7373337290785731).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * 0.30075552039165654).on(cirq.GridQubit(7, 6)),
                cirq.rz(np.pi * 0.6539871150754653).on(cirq.GridQubit(8, 3)),
                cirq.rz(np.pi * -0.6834209135111855).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5390237928795745, phi=0.5165270526693762).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(0, 6)
                ),
                cirq.FSimGate(theta=1.6504170890091214, phi=0.5364505757789483).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.568670761625143, phi=0.5437849784272266).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.5465254433686004, phi=-5.727450888059412).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(2, 8)
                ),
                cirq.FSimGate(theta=1.5381480272852108, phi=0.6090669301824796).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.5830570458423034, phi=0.5523056687078169).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.546350568481482, phi=0.4879631369282715).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.5326394193330342, phi=0.4395048201320801).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5745817206538912, phi=0.5078468553250708).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5287959808590572, phi=0.5477757594186843).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.4855370661448744, phi=0.5162805489497694).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.527373036078513, phi=0.5115160136560014).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.4000192936015627, phi=0.45553928758281914).on(
                    cirq.GridQubit(5, 7), cirq.GridQubit(5, 8)
                ),
                cirq.FSimGate(theta=1.5800842999687046, phi=0.45282693980374283).on(
                    cirq.GridQubit(6, 1), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.518789513006022, phi=0.48179520284759936).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.529911511830527, phi=0.5594440380846348).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(6, 6)
                ),
                cirq.FSimGate(theta=1.4246757982684226, phi=0.4944809315999467).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.5296678467857068, phi=0.5740197418485297).on(
                    cirq.GridQubit(7, 5), cirq.GridQubit(7, 6)
                ),
                cirq.FSimGate(theta=1.4984631547270855, phi=0.49206955088399174).on(
                    cirq.GridQubit(8, 3), cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -0.3991344806935565).on(cirq.GridQubit(0, 5)),
                cirq.rz(np.pi * 0.4497461009300171).on(cirq.GridQubit(0, 6)),
                cirq.rz(np.pi * -0.7845337860294374).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * 0.8725635052999152).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * 0.3359232868994633).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * -0.3534130415003893).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * -0.8243890652764222).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * 0.36681479790840255).on(cirq.GridQubit(2, 8)),
                cirq.rz(np.pi * -0.0090558727799589).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 0.012905855883260531).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * -0.2147146107981729).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * 0.18713718428924947).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * -0.13237930288801908).on(cirq.GridQubit(4, 1)),
                cirq.rz(np.pi * 0.17493678252762246).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * 0.48470458430744).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -0.5423959061355853).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -0.018683935771388622).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * 0.20207250289544368).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -0.9051203501001184).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * 0.870132717475818).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * 0.8152210191616256).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * -0.8006259081891369).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * 0.15496245184388494).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -0.04981613392118451).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 0.29464199519938955).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * -0.26878041789734125).on(cirq.GridQubit(5, 8)),
                cirq.rz(np.pi * -0.9814533427332047).on(cirq.GridQubit(6, 1)),
                cirq.rz(np.pi * -0.7891722207337275).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * -0.008408057016110429).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * -0.014524500524767057).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * 0.14197567163178065).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * -0.13850871720206398).on(cirq.GridQubit(6, 6)),
                cirq.rz(np.pi * -0.6152212896332884).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * 0.18863405595806093).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * 0.5433683710057002).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * -0.9799465796926191).on(cirq.GridQubit(7, 6)),
                cirq.rz(np.pi * 0.3757106337472548).on(cirq.GridQubit(8, 3)),
                cirq.rz(np.pi * -0.405144432182975).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 8)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 9)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 0)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 0.06471891161504284).on(cirq.GridQubit(0, 5)),
                cirq.rz(np.pi * -0.1251632561931063).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * 0.339333732116165).on(cirq.GridQubit(0, 6)),
                cirq.rz(np.pi * -0.4622194922139878).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * -0.5698657190765698).on(cirq.GridQubit(2, 4)),
                cirq.rz(np.pi * 0.602191016523014).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * 0.37244928411870987).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * -0.36772839034764826).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 0.41735638612647213).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * -0.5729988173280529).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 0.9052304996189513).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * 0.6744620219265012).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * -0.7117521075924255).on(cirq.GridQubit(2, 8)),
                cirq.rz(np.pi * 0.7215815153495461).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * 0.7187681197538567).on(cirq.GridQubit(4, 1)),
                cirq.rz(np.pi * -0.7292263985344366).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * 0.7988024164125767).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * -0.8086026044480971).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * -0.14829075582772674).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * 0.21764016277933576).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -0.9852390268577397).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -0.9979326631464183).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * -0.6314402962162012).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * 0.7781598757285099).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * 0.7796352690665389).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -0.3296598317668304).on(cirq.GridQubit(5, 6)),
                cirq.rz(np.pi * -0.2804844557185687).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * 0.2514083000298091).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * -0.09750234138200944).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * 0.13417546813571443).on(cirq.GridQubit(5, 8)),
                cirq.rz(np.pi * 0.7086295141685804).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * -0.6943772327003662).on(cirq.GridQubit(7, 2)),
                cirq.rz(np.pi * 0.6326396024197916).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * -0.7316833746285805).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * 0.6741146672305345).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * 0.8573939250239233).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * 0.4050020207652509).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * -0.4901483317198475).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * 0.2727846672255264).on(cirq.GridQubit(6, 6)),
                cirq.rz(np.pi * -0.37494528939223337).on(cirq.GridQubit(7, 6)),
                cirq.rz(np.pi * -0.6831123785789998).on(cirq.GridQubit(8, 4)),
                cirq.rz(np.pi * 0.7388782940024765).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.4660264742068387, phi=0.4703035018096913).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5595675891930325, phi=0.5029212805853078).on(
                    cirq.GridQubit(0, 6), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.5057896135518938, phi=0.5276098280644357).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.544885207693353, phi=0.5728958894277337).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.521825393645828, phi=0.5386243364775084).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.568786150985278, phi=0.5431362030835812).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.6068421332516425, phi=0.49425168255721214).on(
                    cirq.GridQubit(2, 8), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.5926635714606605, phi=0.49518543009178106).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(5, 1)
                ),
                cirq.FSimGate(theta=1.4823586616735414, phi=0.52880608763343).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.5878491175464968, phi=0.4879472611318097).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5390712580125911, phi=0.5384288567835004).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.5319407509110305, phi=0.5000474088191262).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.5700853308915463, phi=0.46400287842866444).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(5, 6)
                ),
                cirq.FSimGate(theta=1.5356042072853593, phi=0.5206952948829173).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.6447139280388123, phi=0.46839573172584353).on(
                    cirq.GridQubit(4, 8), cirq.GridQubit(5, 8)
                ),
                cirq.FSimGate(theta=1.5383311289896362, phi=0.5127577213621436).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(7, 2)
                ),
                cirq.FSimGate(theta=1.5052207980661314, phi=0.5125556567248526).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.3373234810096835, phi=-5.709279866705804).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.5012621338159504, phi=0.5119166112294746).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(7, 5)
                ),
                cirq.FSimGate(theta=1.3909778451077717, phi=0.4282244069641004).on(
                    cirq.GridQubit(6, 6), cirq.GridQubit(7, 6)
                ),
                cirq.FSimGate(theta=1.5178422515660452, phi=0.47308231008168455).on(
                    cirq.GridQubit(8, 4), cirq.GridQubit(9, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -0.8660901053181692).on(cirq.GridQubit(0, 5)),
                cirq.rz(np.pi * 0.8056457607401057).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * -0.33816910712849085).on(cirq.GridQubit(0, 6)),
                cirq.rz(np.pi * 0.2152833470306681).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * -0.7446592471736861).on(cirq.GridQubit(2, 4)),
                cirq.rz(np.pi * 0.7769845446201303).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * 0.30896061635298644).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * -0.30423972258192483).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -0.07335370176289571).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * -0.08228872943868508).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 0.024175340050477914).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * -0.4444828185050254).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * -0.6194352284028827).on(cirq.GridQubit(2, 8)),
                cirq.rz(np.pi * 0.6292646361600033).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * -0.4640104174524582).on(cirq.GridQubit(4, 1)),
                cirq.rz(np.pi * 0.4535521386718783).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * 0.6262757858947182).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * -0.6360759739302386).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * -0.17088705515738453).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * 0.24023646210899355).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -0.06468415014879703).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * 0.08151246014463917).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * -0.31106112679597503).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * 0.45778070630828366).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * 0.07678578575930568).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * 0.3731896515404028).on(cirq.GridQubit(5, 6)),
                cirq.rz(np.pi * 0.38017264129107714).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * -0.4092487969798368).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * -0.9430124445527418).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * 0.9796855713064467).on(cirq.GridQubit(5, 8)),
                cirq.rz(np.pi * -0.056676065859491365).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * 0.07092834732770553).on(cirq.GridQubit(7, 2)),
                cirq.rz(np.pi * 0.9356782786968267).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * 0.9652779490943842).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * 0.4380882279456786).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * -0.9065796356912208).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * 0.18262669912715115).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * -0.26777301008174775).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * 0.008024631677619333).on(cirq.GridQubit(6, 6)),
                cirq.rz(np.pi * -0.11018525384432631).on(cirq.GridQubit(7, 6)),
                cirq.rz(np.pi * 0.9501300795306425).on(cirq.GridQubit(8, 4)),
                cirq.rz(np.pi * -0.8943641641071659).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 9)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 9)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 0)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 1)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 2)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(9, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -0.4976444790781308).on(cirq.GridQubit(1, 4)),
                cirq.rz(np.pi * 0.5379003211665513).on(cirq.GridQubit(2, 4)),
                cirq.rz(np.pi * -0.9782760403822399).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * 0.9889587550080732).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * 0.827776636023004).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * -0.7229638562757831).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * -0.5720009889018596).on(cirq.GridQubit(1, 7)),
                cirq.rz(np.pi * 0.10901089354978011).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * -0.12773630378623654).on(cirq.GridQubit(3, 2)),
                cirq.rz(np.pi * 0.16738673512821675).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * 0.033189304176399426).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * -0.11560397916015874).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -0.6435335473951701).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * 0.7208917442612333).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * 0.36011353863817136).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -0.29667832983006515).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * 0.4959350962181673).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * -0.5063804234526539).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -0.44905108909945907).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * 0.4226347023528327).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * -0.4749508386385932).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * 0.48213474475080664).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * 0.2287263987690629).on(cirq.GridQubit(3, 9)),
                cirq.rz(np.pi * 0.06442983800514027).on(cirq.GridQubit(4, 9)),
                cirq.rz(np.pi * 0.286983746644866).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * -0.5517968237002955).on(cirq.GridQubit(6, 1)),
                cirq.rz(np.pi * 0.14608810502399938).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * -0.15237237711581883).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * 0.6143376933488645).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -0.602313728296298).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * 0.004070854509478497).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * -0.07169334172148659).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * -0.6678587823292685).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * 0.7039270616968651).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * 0.6437953384273074).on(cirq.GridQubit(5, 6)),
                cirq.rz(np.pi * -0.3871368179084222).on(cirq.GridQubit(6, 6)),
                cirq.rz(np.pi * 0.44527301462359453).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * -0.24812115322778755).on(cirq.GridQubit(6, 7)),
                cirq.rz(np.pi * 0.0738609198281516).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * -0.07211133542345739).on(cirq.GridQubit(8, 3)),
                cirq.rz(np.pi * -0.6558882024199431).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * 0.8051269359345058).on(cirq.GridQubit(8, 4)),
                cirq.rz(np.pi * 0.9459992868788965).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * -0.94104534810004).on(cirq.GridQubit(8, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5496057658133178, phi=0.5393238727561925).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(2, 4)
                ),
                cirq.FSimGate(theta=1.5258573993033773, phi=0.5301963978982887).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.5999105816064956, phi=0.47191843749859924).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.4104416482963105, phi=-5.734064803424554).on(
                    cirq.GridQubit(1, 7), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.5319225163456216, phi=0.49105711881659464).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.465404631262162, phi=0.4878297652759932).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.4707183263040744, phi=0.5651156081809627).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5467222527282019, phi=0.5068034228124387).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.5496604814896044, phi=0.5531983372087332).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5524939155045483, phi=0.5566693071275687).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.363213412756342, phi=0.7994150767548583).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.5284460090316794, phi=0.5432682295494672).on(
                    cirq.GridQubit(3, 9), cirq.GridQubit(4, 9)
                ),
                cirq.FSimGate(theta=1.3166607142943418, phi=0.40127686655135986).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(6, 1)
                ),
                cirq.FSimGate(theta=1.5594498457697554, phi=0.5290555375763617).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.5125120660103082, phi=0.5195553885293336).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.54223977200166, phi=0.47914474770071624).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.6074361272506783, phi=0.4906717148713765).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.4382571284509336, phi=0.5684944786275166).on(
                    cirq.GridQubit(5, 6), cirq.GridQubit(6, 6)
                ),
                cirq.FSimGate(theta=1.533964395594986, phi=0.47457535225216274).on(
                    cirq.GridQubit(5, 7), cirq.GridQubit(6, 7)
                ),
                cirq.FSimGate(theta=1.5001433000839564, phi=0.6605028795204214).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(8, 3)
                ),
                cirq.FSimGate(theta=1.640026880988053, phi=0.4976366432039147).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(8, 4)
                ),
                cirq.FSimGate(theta=1.5423122824843978, phi=0.7792646973911541).on(
                    cirq.GridQubit(7, 5), cirq.GridQubit(8, 5)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 0.6587378389937858).on(cirq.GridQubit(1, 4)),
                cirq.rz(np.pi * -0.6184819969053699).on(cirq.GridQubit(2, 4)),
                cirq.rz(np.pi * 0.4776636694289055).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * -0.4669809548030722).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * -0.9241993636629616).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * -0.9709878565898176).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * -0.21424583903010938).on(cirq.GridQubit(1, 7)),
                cirq.rz(np.pi * -0.2487442563219724).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * 0.8850413953111727).on(cirq.GridQubit(3, 2)),
                cirq.rz(np.pi * -0.8453909639691924).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * 0.21016065338305343).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * -0.2925753283668127).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -0.4561234297210863).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * 0.5334816265871495).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -0.9603938707110118).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -0.976170920480882).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -0.777024243907283).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 0.7665789166727964).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -0.24890504835713093).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * 0.22248866161050454).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * 0.5831562616836323).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * -0.5759723555714189).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * -0.939965957130717).on(cirq.GridQubit(3, 9)),
                cirq.rz(np.pi * -0.7668778060950799).on(cirq.GridQubit(4, 9)),
                cirq.rz(np.pi * 0.9226198327802603).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * 0.8125670901643102).on(cirq.GridQubit(6, 1)),
                cirq.rz(np.pi * 0.8998029094991369).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * -0.9060871815909564).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * 0.3820041493820226).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -0.3699801843294539).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * 0.6946273923335435).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * -0.7622498795455516).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * -0.5443890968878398).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * 0.5804573762554363).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * -0.9848537819493798).on(cirq.GridQubit(5, 6)),
                cirq.rz(np.pi * -0.758487697531735).on(cirq.GridQubit(6, 6)),
                cirq.rz(np.pi * -0.18638841518174792).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * 0.3835402765775549).on(cirq.GridQubit(6, 7)),
                cirq.rz(np.pi * -0.6709657882665934).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * 0.6727153726712877).on(cirq.GridQubit(8, 3)),
                cirq.rz(np.pi * -0.3734498395952722).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * 0.522688573109835).on(cirq.GridQubit(8, 4)),
                cirq.rz(np.pi * -0.017706180981440167).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * 0.02266011976029662).on(cirq.GridQubit(8, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 9)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 1)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 8)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 9)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 0)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 0.7233176668869).on(cirq.GridQubit(1, 4)),
                cirq.rz(np.pi * -0.8284847063764873).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * -0.6456431928704595).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * -0.8683461736748109).on(cirq.GridQubit(1, 7)),
                cirq.rz(np.pi * -0.5320390213851242).on(cirq.GridQubit(2, 4)),
                cirq.rz(np.pi * 0.4804522607988163).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * -0.6128895071843858).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * -0.9441305352006717).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * -0.45795789807019194).on(cirq.GridQubit(3, 2)),
                cirq.rz(np.pi * 0.49826390752450206).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * -0.4828135478520814).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * 0.5767540847808064).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 0.9318819125980257).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 0.974143211073274).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * 0.4150194572441162).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * -0.431253826472847).on(cirq.GridQubit(3, 9)),
                cirq.rz(np.pi * -0.6055610143846115).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * 0.5701280226226959).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * 0.9425320436532129).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -0.6809556968178213).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -0.5683965078969038).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * 0.98003845801911).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * -0.4653867869996434).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * 0.9598133569197824).on(cirq.GridQubit(4, 9)),
                cirq.rz(np.pi * -0.1267003461564842).on(cirq.GridQubit(5, 0)),
                cirq.rz(np.pi * 0.16920351468881023).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * -0.006677673632575996).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * 0.06776650248758825).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -0.8528443470072338).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 0.926137663390736).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * -0.4395057287509062).on(cirq.GridQubit(5, 6)),
                cirq.rz(np.pi * 0.5961518105121437).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * 0.8583932697009197).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * 0.9955969811667055).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * -0.5398876019886651).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * 0.5873581656110965).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * -0.38232940488452255).on(cirq.GridQubit(6, 6)),
                cirq.rz(np.pi * -0.02938770910860789).on(cirq.GridQubit(6, 7)),
                cirq.rz(np.pi * 0.9189031334524357).on(cirq.GridQubit(7, 2)),
                cirq.rz(np.pi * -0.8396183416394707).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * 0.00885696463397066).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * 0.03046032294032485).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * 0.30531375200551514).on(cirq.GridQubit(8, 4)),
                cirq.rz(np.pi * -0.2912197872301928).on(cirq.GridQubit(8, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5553516266448077, phi=0.47754343999179444).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5513695622863453, phi=0.5525497751179018).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(1, 7)
                ),
                cirq.FSimGate(theta=1.5920107910314218, phi=0.495277170657118).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.4850359189030258, phi=0.5432026764541129).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.5586373808029026, phi=0.46099332137061977).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(3, 3)
                ),
                cirq.FSimGate(theta=1.5468483989685475, phi=0.5246739758652749).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5358532152984938, phi=0.5376855016240104).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.4939596076472883, phi=0.6686288484482796).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(3, 9)
                ),
                cirq.FSimGate(theta=1.548255653119813, phi=0.48307337635991665).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.6000940826263392, phi=0.5132890545539279).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.5314832643812344, phi=0.47518174639867017).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.5608608535579012, phi=0.6668893914368428).on(
                    cirq.GridQubit(4, 8), cirq.GridQubit(4, 9)
                ),
                cirq.FSimGate(theta=1.5676963775554011, phi=0.48299203630424015).on(
                    cirq.GridQubit(5, 0), cirq.GridQubit(5, 1)
                ),
                cirq.FSimGate(theta=1.4807002448035869, phi=0.48033134534938904).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5479898631344362, phi=0.5021140664341368).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.5508083238882544, phi=0.5088503466820911).on(
                    cirq.GridQubit(5, 6), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.507155881326315, phi=0.4773896323482684).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.5602578123868405, phi=0.5276499696880497).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.3390062722902263, phi=0.4491086448159195).on(
                    cirq.GridQubit(6, 6), cirq.GridQubit(6, 7)
                ),
                cirq.FSimGate(theta=1.5485996563720543, phi=0.4873901665634375).on(
                    cirq.GridQubit(7, 2), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.5468701891071555, phi=0.47909090411139443).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(7, 5)
                ),
                cirq.FSimGate(theta=1.5253448615592025, phi=0.5174324533286649).on(
                    cirq.GridQubit(8, 4), cirq.GridQubit(8, 5)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -0.2520912204422194).on(cirq.GridQubit(1, 4)),
                cirq.rz(np.pi * 0.14692418095263213).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * -0.09099025816742104).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * 0.5770008916221506).on(cirq.GridQubit(1, 7)),
                cirq.rz(np.pi * 0.8824931967907349).on(cirq.GridQubit(2, 4)),
                cirq.rz(np.pi * -0.9340799573770427).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * 0.10861509609686511).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * 0.33436486151807504).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * 0.8209084620085465).on(cirq.GridQubit(3, 2)),
                cirq.rz(np.pi * -0.7806024525542363).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * -0.9586345492404763).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * -0.9474249138307987).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -0.24974303691835847).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 0.15576816058965812).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * -0.7379177873217329).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * 0.7216834180930021).on(cirq.GridQubit(3, 9)),
                cirq.rz(np.pi * 0.7096104339852799).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * -0.7450434257471955).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -0.2394228518816571).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * 0.5009991987170492).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -0.698162511405473).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -0.8901955384723206).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * 0.8845022064919659).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * -0.390075636571827).on(cirq.GridQubit(4, 9)),
                cirq.rz(np.pi * 0.7443824968937399).on(cirq.GridQubit(5, 0)),
                cirq.rz(np.pi * -0.7018793283614139).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * 0.5553034013948395).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * -0.49421457253982753).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * 0.5726738461747138).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * -0.49938052979121156).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * -0.5189329604729642).on(cirq.GridQubit(5, 6)),
                cirq.rz(np.pi * 0.6755790422342021).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * -0.9117244593291037).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * 0.7657147101967289).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * -0.09590462396824127).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * 0.14337518759067266).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * -0.20606500921845686).on(cirq.GridQubit(6, 6)),
                cirq.rz(np.pi * -0.20565210477467358).on(cirq.GridQubit(6, 7)),
                cirq.rz(np.pi * -0.12250885288308018).on(cirq.GridQubit(7, 2)),
                cirq.rz(np.pi * 0.20179364469604513).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * 0.8165255858956675).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * -0.7772082983213721).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * -0.5225682598437545).on(cirq.GridQubit(8, 4)),
                cirq.rz(np.pi * 0.5366622246190769).on(cirq.GridQubit(8, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 9)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 9)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 0)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 0.4177500776284307).on(cirq.GridQubit(0, 5)),
                cirq.rz(np.pi * -0.36713845739197015).on(cirq.GridQubit(0, 6)),
                cirq.rz(np.pi * 0.14183655081167112).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * -0.05380683154119779).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * 0.6350747424372947).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * -0.6525644970382162).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * 0.5020713138994825).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * -0.9596455812674999).on(cirq.GridQubit(2, 8)),
                cirq.rz(np.pi * 0.6068974930362895).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * -0.5437670222098251).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * 0.060408559425096625).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -0.056558576321790476).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * -0.4414637962193981).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * 0.41388636971047466).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * 0.0247477937158412).on(cirq.GridQubit(4, 1)),
                cirq.rz(np.pi * 0.01780968592376219).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * -0.09680594056427506).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * 0.039114618736129744).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -0.7649613803084276).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * 0.9483499474324782).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -0.1907621379649213).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * 0.15577450534062087).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * -0.6821091333754711).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * 0.6967042443479621).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * -0.8485229450742843).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * 0.9536692629969846).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * -0.818134870244339).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * 0.5021979908700074).on(cirq.GridQubit(5, 6)),
                cirq.rz(np.pi * 0.03807589709745298).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * -0.012214319795404669).on(cirq.GridQubit(5, 8)),
                cirq.rz(np.pi * -0.5440747822637373).on(cirq.GridQubit(6, 1)),
                cirq.rz(np.pi * 0.7734492187968052).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * 0.45999118383874044).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * -0.4829237413796179).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * 0.056142897857480334).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * -0.05267594342776817).on(cirq.GridQubit(6, 6)),
                cirq.rz(np.pi * 0.17171055205277141).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * -0.5982977857280012).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * -0.7173337290785088).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * 0.28075552039160123).on(cirq.GridQubit(7, 6)),
                cirq.rz(np.pi * 0.35398711507551783).on(cirq.GridQubit(8, 3)),
                cirq.rz(np.pi * -0.3834209135112381).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5390237928795745, phi=0.5165270526693762).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(0, 6)
                ),
                cirq.FSimGate(theta=1.6504170890091214, phi=0.5364505757789483).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.568670761625143, phi=0.5437849784272266).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.5465254433686004, phi=-5.727450888059412).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(2, 8)
                ),
                cirq.FSimGate(theta=1.2913067233725621, phi=0.47167387649514164).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.5381480272852108, phi=0.6090669301824796).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.5830570458423034, phi=0.5523056687078169).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.546350568481482, phi=0.4879631369282715).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.5326394193330342, phi=0.4395048201320801).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5745817206538912, phi=0.5078468553250708).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5287959808590572, phi=0.5477757594186843).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.4855370661448744, phi=0.5162805489497694).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.527373036078513, phi=0.5115160136560014).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.4411810311735318, phi=0.4660991447993951).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(5, 6)
                ),
                cirq.FSimGate(theta=1.4000192936015627, phi=0.45553928758281914).on(
                    cirq.GridQubit(5, 7), cirq.GridQubit(5, 8)
                ),
                cirq.FSimGate(theta=1.5800842999687046, phi=0.45282693980374283).on(
                    cirq.GridQubit(6, 1), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.518789513006022, phi=0.48179520284759936).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.529911511830527, phi=0.5594440380846348).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(6, 6)
                ),
                cirq.FSimGate(theta=1.4246757982684226, phi=0.4944809315999467).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.5296678467857068, phi=0.5740197418485297).on(
                    cirq.GridQubit(7, 5), cirq.GridQubit(7, 6)
                ),
                cirq.FSimGate(theta=1.4984631547270855, phi=0.49206955088399174).on(
                    cirq.GridQubit(8, 3), cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -0.5511344806935855).on(cirq.GridQubit(0, 5)),
                cirq.rz(np.pi * 0.6017461009300461).on(cirq.GridQubit(0, 6)),
                cirq.rz(np.pi * 0.31546621397058244).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * -0.2274364947001091).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * 0.7679232868995314).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * -0.7854130415004529).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * 0.9596109347236025).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * 0.5828147979083801).on(cirq.GridQubit(2, 8)),
                cirq.rz(np.pi * -0.40892873034490373).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * 0.47205920117136807).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * 0.794944127219964).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -0.7910941441166578).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 0.5332853892017715).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * -0.560862815710695).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * -0.512379302888095).on(cirq.GridQubit(4, 1)),
                cirq.rz(np.pi * 0.5549367825276983).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * -0.3992954156924824).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * 0.34160409386433704).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -0.17868393577138544).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * 0.362072502895436).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * 0.9548796498999242).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * -0.9898672825242247).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * -0.3007789808384543).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * 0.3153740918109452).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * -0.06503754815606688).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * 0.17018386607876732).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 0.5050026546430052).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * -0.8209395340173369).on(cirq.GridQubit(5, 6)),
                cirq.rz(np.pi * 0.8946419951994167).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * -0.8687804178973684).on(cirq.GridQubit(5, 8)),
                cirq.rz(np.pi * -0.23745334273310847).on(cirq.GridQubit(6, 1)),
                cirq.rz(np.pi * 0.4668277792661763).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * -0.8950047671667344).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * 0.8720722096258569).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * 0.7219756716317649).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * -0.7185087172020528).on(cirq.GridQubit(6, 6)),
                cirq.rz(np.pi * 0.6487787103667042).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * 0.924634055958066).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * 0.5233683710056539).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * -0.9599465796925638).on(cirq.GridQubit(7, 6)),
                cirq.rz(np.pi * 0.6757106337472022).on(cirq.GridQubit(8, 3)),
                cirq.rz(np.pi * -0.7051444321829224).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 9)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 9)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 0)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 8)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -0.7552810883849356).on(cirq.GridQubit(0, 5)),
                cirq.rz(np.pi * 0.6948367438068721).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * 0.26733373211613104).on(cirq.GridQubit(0, 6)),
                cirq.rz(np.pi * -0.3902194922139527).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * -0.9298657190764705).on(cirq.GridQubit(2, 4)),
                cirq.rz(np.pi * 0.9621910165229147).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * 0.7524492841186501).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * -0.7477283903475884).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 0.4253563861265644).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * -0.5809988173281497).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 0.02123049961889777).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * -0.44153797807344525).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * -0.5597521075923941).on(cirq.GridQubit(2, 8)),
                cirq.rz(np.pi * 0.5695815153495171).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * 0.13876811975387698).on(cirq.GridQubit(4, 1)),
                cirq.rz(np.pi * -0.14922639853445682).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * 0.9548024164125918).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * -0.9646026044481122).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * 0.9677092441722208).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -0.8983598372206117).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -0.5332390268577587).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * 0.5500673368536054).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 0.488559703783858).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -0.34184012427154936).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * -0.5603647309334705).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -0.989659831766821).on(cirq.GridQubit(5, 6)),
                cirq.rz(np.pi * 0.30751554428138683).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * -0.33659169997014643).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * -0.24950234138203956).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * 0.28617546813574457).on(cirq.GridQubit(5, 8)),
                cirq.rz(np.pi * 0.7726295141686511).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * -0.7583772327004369).on(cirq.GridQubit(7, 2)),
                cirq.rz(np.pi * 0.8446396024197783).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * -0.9436833746285673).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * 0.7355179570799013).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * 0.7959906351745564).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * 0.9890020207652236).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * 0.9258516682801798).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * -0.5432153327744723).on(cirq.GridQubit(6, 6)),
                cirq.rz(np.pi * 0.44105471060776535).on(cirq.GridQubit(7, 6)),
                cirq.rz(np.pi * -0.2431123785789638).on(cirq.GridQubit(8, 4)),
                cirq.rz(np.pi * 0.29887829400244054).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.4660264742068387, phi=0.4703035018096913).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5595675891930325, phi=0.5029212805853078).on(
                    cirq.GridQubit(0, 6), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.5057896135518938, phi=0.5276098280644357).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.544885207693353, phi=0.5728958894277337).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.521825393645828, phi=0.5386243364775084).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.568786150985278, phi=0.5431362030835812).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.6068421332516425, phi=0.49425168255721214).on(
                    cirq.GridQubit(2, 8), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.5926635714606605, phi=0.49518543009178106).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(5, 1)
                ),
                cirq.FSimGate(theta=1.4823586616735414, phi=0.52880608763343).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.5878491175464968, phi=0.4879472611318097).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5390712580125911, phi=0.5384288567835004).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.5319407509110305, phi=0.5000474088191262).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.5700853308915463, phi=0.46400287842866444).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(5, 6)
                ),
                cirq.FSimGate(theta=1.5356042072853593, phi=0.5206952948829173).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.6447139280388123, phi=0.46839573172584353).on(
                    cirq.GridQubit(4, 8), cirq.GridQubit(5, 8)
                ),
                cirq.FSimGate(theta=1.5383311289896362, phi=0.5127577213621436).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(7, 2)
                ),
                cirq.FSimGate(theta=1.5052207980661314, phi=0.5125556567248526).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.3373234810096835, phi=-5.709279866705804).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.5012621338159504, phi=0.5119166112294746).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(7, 5)
                ),
                cirq.FSimGate(theta=1.3909778451077717, phi=0.4282244069641004).on(
                    cirq.GridQubit(6, 6), cirq.GridQubit(7, 6)
                ),
                cirq.FSimGate(theta=1.5178422515660452, phi=0.47308231008168455).on(
                    cirq.GridQubit(8, 4), cirq.GridQubit(9, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -0.04609010531819078).on(cirq.GridQubit(0, 5)),
                cirq.rz(np.pi * -0.014354239259872668).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * -0.26616910712845576).on(cirq.GridQubit(0, 6)),
                cirq.rz(np.pi * 0.1432833470306341).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * -0.38465924717378547).on(cirq.GridQubit(2, 4)),
                cirq.rz(np.pi * 0.41698454462022966).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * -0.07103938364695375).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * 0.07576027741801536).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -0.08135370176299248).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * -0.07428872943859284).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 0.9081753400505315).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * 0.671517181494921).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * -0.7714352284029128).on(cirq.GridQubit(2, 8)),
                cirq.rz(np.pi * 0.7812646361600334).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * 0.11598958254752155).on(cirq.GridQubit(4, 1)),
                cirq.rz(np.pi * -0.1264478613281014).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * 0.4702757858947076).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * -0.480075973930228).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * 0.713112944842668).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -0.6437635378910589).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -0.5166841501487734).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * 0.5335124601446156).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 0.568938873203959).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -0.4222192936916503).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * -0.583214214240685).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -0.9668103484596066).on(cirq.GridQubit(5, 6)),
                cirq.rz(np.pi * -0.2078273587088784).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * 0.17875120302011874).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * -0.7910124445527128).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * 0.8276855713064177).on(cirq.GridQubit(5, 8)),
                cirq.rz(np.pi * -0.12067606585956428).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * 0.13492834732777845).on(cirq.GridQubit(7, 2)),
                cirq.rz(np.pi * 0.72367827869684).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * -0.8227220509056289).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * 0.37668493809630715).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * -0.8451763458418494).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * -0.4013733008728216).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * 0.31622698991822273).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * 0.8240246316776181).on(cirq.GridQubit(6, 6)),
                cirq.rz(np.pi * -0.926185253844325).on(cirq.GridQubit(7, 6)),
                cirq.rz(np.pi * 0.5101300795306044).on(cirq.GridQubit(8, 4)),
                cirq.rz(np.pi * -0.45436416410712765).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 8)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 9)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 9)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 0)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 1)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 2)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(9, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -0.7096444790781153).on(cirq.GridQubit(1, 4)),
                cirq.rz(np.pi * 0.7499003211665359).on(cirq.GridQubit(2, 4)),
                cirq.rz(np.pi * 0.8017239596178061).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * -0.7910412449919739).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * -0.7242233639769967).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * 0.8290361437242199).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * -0.18800098890179529).on(cirq.GridQubit(1, 7)),
                cirq.rz(np.pi * -0.27498910645028646).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * 0.9722636962137764).on(cirq.GridQubit(3, 2)),
                cirq.rz(np.pi * -0.9326132648717963).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * -0.6468106958234995).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * 0.5643960208397402).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * 0.5284664526047389).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * -0.45110825573867575).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * 0.7241135386381939).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -0.6606783298300877).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -0.17606490378189493).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 0.16561957654740833).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * 0.05894891090062921).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * -0.08536529764725105).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * 0.9210491613613878).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * -0.9138652552491744).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * -0.8792736012309236).on(cirq.GridQubit(3, 9)),
                cirq.rz(np.pi * -0.8275701619948732).on(cirq.GridQubit(4, 9)),
                cirq.rz(np.pi * 0.9509837466449654).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * 0.784203176299605).on(cirq.GridQubit(6, 1)),
                cirq.rz(np.pi * 0.950088105023911).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * -0.9563723771157304).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * 0.09033769334885182).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -0.0783137282962854).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * 0.14666756466013284).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * -0.21429005187214545).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * 0.7321412176707054).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * -0.6960729383031089).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * -0.23620466157263784).on(cirq.GridQubit(5, 6)),
                cirq.rz(np.pi * 0.49286318209152535).on(cirq.GridQubit(6, 6)),
                cirq.rz(np.pi * -0.5867269853763775).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * 0.7838788467721844).on(cirq.GridQubit(6, 7)),
                cirq.rz(np.pi * -0.2141390801718531).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * 0.21588866457655184).on(cirq.GridQubit(8, 3)),
                cirq.rz(np.pi * 0.020111797580098636).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * 0.12912693593446414).on(cirq.GridQubit(8, 4)),
                cirq.rz(np.pi * 0.34599928687886594).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * -0.3410453481000095).on(cirq.GridQubit(8, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5496057658133178, phi=0.5393238727561925).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(2, 4)
                ),
                cirq.FSimGate(theta=1.5258573993033773, phi=0.5301963978982887).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.5999105816064956, phi=0.47191843749859924).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.4104416482963105, phi=-5.734064803424554).on(
                    cirq.GridQubit(1, 7), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.5319225163456216, phi=0.49105711881659464).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.465404631262162, phi=0.4878297652759932).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.4707183263040744, phi=0.5651156081809627).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5467222527282019, phi=0.5068034228124387).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.5496604814896044, phi=0.5531983372087332).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5524939155045483, phi=0.5566693071275687).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.363213412756342, phi=0.7994150767548583).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.5284460090316794, phi=0.5432682295494672).on(
                    cirq.GridQubit(3, 9), cirq.GridQubit(4, 9)
                ),
                cirq.FSimGate(theta=1.3166607142943418, phi=0.40127686655135986).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(6, 1)
                ),
                cirq.FSimGate(theta=1.5594498457697554, phi=0.5290555375763617).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.5125120660103082, phi=0.5195553885293336).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.54223977200166, phi=0.47914474770071624).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.6074361272506783, phi=0.4906717148713765).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.4382571284509336, phi=0.5684944786275166).on(
                    cirq.GridQubit(5, 6), cirq.GridQubit(6, 6)
                ),
                cirq.FSimGate(theta=1.533964395594986, phi=0.47457535225216274).on(
                    cirq.GridQubit(5, 7), cirq.GridQubit(6, 7)
                ),
                cirq.FSimGate(theta=1.5001433000839564, phi=0.6605028795204214).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(8, 3)
                ),
                cirq.FSimGate(theta=1.640026880988053, phi=0.4976366432039147).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(8, 4)
                ),
                cirq.FSimGate(theta=1.5423122824843978, phi=0.7792646973911541).on(
                    cirq.GridQubit(7, 5), cirq.GridQubit(8, 5)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 0.8707378389937772).on(cirq.GridQubit(1, 4)),
                cirq.rz(np.pi * -0.8304819969053566).on(cirq.GridQubit(2, 4)),
                cirq.rz(np.pi * 0.6976636694288573).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * -0.6869809548030251).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * 0.6278006363370414).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * -0.5229878565898183).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * -0.5982458390301759).on(cirq.GridQubit(1, 7)),
                cirq.rz(np.pi * 0.1352557436780942).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * -0.21495860468884262).on(cirq.GridQubit(3, 2)),
                cirq.rz(np.pi * 0.2546090360308228).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * 0.8901606533829524).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * -0.9725753283667117).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * 0.3718765702790024).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * -0.29451837341293924).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * 0.6756061292889657).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -0.6121709204808594).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -0.10502424390722076).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 0.09457891667273416).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -0.756905048357217).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * 0.7304886616105951).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * -0.8128437383163487).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * 0.8200276444285621).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * 0.16803404286926957).on(cirq.GridQubit(3, 9)),
                cirq.rz(np.pi * 0.1251221939049336).on(cirq.GridQubit(4, 9)),
                cirq.rz(np.pi * 0.2586198327801597).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * -0.5234329098355892).on(cirq.GridQubit(6, 1)),
                cirq.rz(np.pi * 0.09580290949922535).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * -0.10208718159104481).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * 0.9060041493820341).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -0.8939801843294677).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * 0.5520306821828892).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * -0.6196531693949018).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * 0.05561090311218627).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * -0.019542623744589722).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * -0.10485378194943454).on(cirq.GridQubit(5, 6)),
                cirq.rz(np.pi * 0.36151230246832433).on(cirq.GridQubit(6, 6)),
                cirq.rz(np.pi * 0.8456115848182241).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * -0.6484597234224171).on(cirq.GridQubit(6, 7)),
                cirq.rz(np.pi * -0.3829657882665887).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * 0.3847153726712874).on(cirq.GridQubit(8, 3)),
                cirq.rz(np.pi * 0.9505501604046817).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * -0.8013114268901188).on(cirq.GridQubit(8, 4)),
                cirq.rz(np.pi * 0.5822938190185858).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * -0.5773398802397294).on(cirq.GridQubit(8, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 8)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 8)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 9)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 0)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 0.8753176668869279).on(cirq.GridQubit(1, 4)),
                cirq.rz(np.pi * -0.9804847063765152).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * 0.8303568071295301).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * -0.3443461736748006).on(cirq.GridQubit(1, 7)),
                cirq.rz(np.pi * -0.388039021385054).on(cirq.GridQubit(2, 4)),
                cirq.rz(np.pi * 0.3364522607987461).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * 0.7991104928156598).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * -0.35613053520071736).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * -0.5259578980702443).on(cirq.GridQubit(3, 2)),
                cirq.rz(np.pi * 0.5662639075245589).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * 0.401186452147841).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * -0.30724591521911604).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -0.5481180874020746).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 0.4541432110733742).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * -0.024980542755920872).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * 0.008746173527187847).on(cirq.GridQubit(3, 9)),
                cirq.rz(np.pi * -0.4535610143845825).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * 0.4181280226226692).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -0.9814679563467732).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -0.7569556968178358).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -0.8683965078968512).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -0.7199615419809425).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * 0.590613213000361).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * -0.096186643080213).on(cirq.GridQubit(4, 9)),
                cirq.rz(np.pi * -0.5747003461564824).on(cirq.GridQubit(5, 0)),
                cirq.rz(np.pi * 0.6172035146888061).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * -0.8946776736326099).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * 0.9557665024876215).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -0.10884434700713866).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 0.18213766339064089).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * -0.8115057287508876).on(cirq.GridQubit(5, 6)),
                cirq.rz(np.pi * 0.9681518105121262).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * 0.6423932697009466).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * -0.7884030188333215).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * -0.5384843121392539).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * 0.5859548757616853).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * -0.906329404884533).on(cirq.GridQubit(6, 6)),
                cirq.rz(np.pi * 0.4946122908914025).on(cirq.GridQubit(6, 7)),
                cirq.rz(np.pi * 0.8509031334523833).on(cirq.GridQubit(7, 2)),
                cirq.rz(np.pi * -0.7716183416394184).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * 0.532856964633981).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * -0.49353967705968554).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * -0.4466862479945557).on(cirq.GridQubit(8, 4)),
                cirq.rz(np.pi * 0.460780212769878).on(cirq.GridQubit(8, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5553516266448077, phi=0.47754343999179444).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5513695622863453, phi=0.5525497751179018).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(1, 7)
                ),
                cirq.FSimGate(theta=1.5920107910314218, phi=0.495277170657118).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.4850359189030258, phi=0.5432026764541129).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.5586373808029026, phi=0.46099332137061977).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(3, 3)
                ),
                cirq.FSimGate(theta=1.5468483989685475, phi=0.5246739758652749).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5358532152984938, phi=0.5376855016240104).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.4939596076472883, phi=0.6686288484482796).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(3, 9)
                ),
                cirq.FSimGate(theta=1.548255653119813, phi=0.48307337635991665).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.6000940826263392, phi=0.5132890545539279).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.5314832643812344, phi=0.47518174639867017).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.5608608535579012, phi=0.6668893914368428).on(
                    cirq.GridQubit(4, 8), cirq.GridQubit(4, 9)
                ),
                cirq.FSimGate(theta=1.5676963775554011, phi=0.48299203630424015).on(
                    cirq.GridQubit(5, 0), cirq.GridQubit(5, 1)
                ),
                cirq.FSimGate(theta=1.4807002448035869, phi=0.48033134534938904).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5479898631344362, phi=0.5021140664341368).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.5508083238882544, phi=0.5088503466820911).on(
                    cirq.GridQubit(5, 6), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.507155881326315, phi=0.4773896323482684).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.5602578123868405, phi=0.5276499696880497).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.3390062722902263, phi=0.4491086448159195).on(
                    cirq.GridQubit(6, 6), cirq.GridQubit(6, 7)
                ),
                cirq.FSimGate(theta=1.5485996563720543, phi=0.4873901665634375).on(
                    cirq.GridQubit(7, 2), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.5468701891071555, phi=0.47909090411139443).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(7, 5)
                ),
                cirq.FSimGate(theta=1.5253448615592025, phi=0.5174324533286649).on(
                    cirq.GridQubit(8, 4), cirq.GridQubit(8, 5)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -0.40409122044224727).on(cirq.GridQubit(1, 4)),
                cirq.rz(np.pi * 0.29892418095266).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * 0.43300974183258933).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * 0.05300089162214019).on(cirq.GridQubit(1, 7)),
                cirq.rz(np.pi * 0.7384931967906647).on(cirq.GridQubit(2, 4)),
                cirq.rz(np.pi * -0.7900799573769726).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * 0.6966150960968195).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * -0.2536351384818771).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * 0.8889084620085989).on(cirq.GridQubit(3, 2)),
                cirq.rz(np.pi * -0.8486024525542887).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * 0.1573654507596013).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * -0.06342491383087631).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -0.7697430369182577).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 0.6757681605895585).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * -0.2979177873217003).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * 0.28168341809296726).on(cirq.GridQubit(3, 9)),
                cirq.rz(np.pi * 0.5576104339852531).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * -0.5930434257471665).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -0.3154228518816733).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * 0.5769991987170643).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -0.39816251140552567).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * 0.809804461527732).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * -0.17149779350802946).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * 0.6659243634281775).on(cirq.GridQubit(4, 9)),
                cirq.rz(np.pi * -0.8076175031062619).on(cirq.GridQubit(5, 0)),
                cirq.rz(np.pi * 0.8501206716385857).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * -0.556696598605127).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * 0.6177854274601386).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -0.17132615382538127).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 0.2446194702088835).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * -0.14693296047298202).on(cirq.GridQubit(5, 6)),
                cirq.rz(np.pi * 0.30357904223422066).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * -0.6957244593291307).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * 0.5497147101967559).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * -0.09730791381765261).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * 0.14477847744008399).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * 0.3179349907815535).on(cirq.GridQubit(6, 6)),
                cirq.rz(np.pi * -0.729652104774684).on(cirq.GridQubit(6, 7)),
                cirq.rz(np.pi * -0.05450885288302786).on(cirq.GridQubit(7, 2)),
                cirq.rz(np.pi * 0.1337936446959928).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * 0.29252558589565714).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * -0.25320829832136166).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * 0.229431740156314).on(cirq.GridQubit(8, 4)),
                cirq.rz(np.pi * -0.21533777538099172).on(cirq.GridQubit(8, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 9)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 1)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 9)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 0)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 1)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 8)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 2)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 0.569750077628462).on(cirq.GridQubit(0, 5)),
                cirq.rz(np.pi * -0.5191384573920014).on(cirq.GridQubit(0, 6)),
                cirq.rz(np.pi * -0.9581634491883464).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * -0.9538068315411803).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * 0.2030747424372311).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * -0.2205644970381616).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * 0.7180713138994554).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * 0.8243544187325271).on(cirq.GridQubit(2, 8)),
                cirq.rz(np.pi * -0.3611025069636074).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * 0.4242329777900717).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * -0.7435914405748172).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 0.7474414236781234).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 0.8105362037806529).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * -0.8381136302895764).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * 0.40474779371592384).on(cirq.GridQubit(4, 1)),
                cirq.rz(np.pi * -0.36219031407632046).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * 0.7871940594356474).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -0.8448853812637926).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -0.6049613803084195).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * 0.7883499474324701).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -0.05076213796496846).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * 0.015774505340668026).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * 0.4338908666246065).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * -0.4192957556521156).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * -0.6285229450743307).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * 0.7336692629970312).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 0.8818651297555824).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * 0.8021979908700883).on(cirq.GridQubit(5, 6)),
                cirq.rz(np.pi * -0.5619241029025708).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * 0.5877856802046236).on(cirq.GridQubit(5, 8)),
                cirq.rz(np.pi * 0.7119252177361687).on(cirq.GridQubit(6, 1)),
                cirq.rz(np.pi * -0.4825507812031009).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * -0.6534121060106312).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * 0.6304795484697536).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * -0.5238571021424926).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * 0.5273240565722138).on(cirq.GridQubit(6, 6)),
                cirq.rz(np.pi * 0.9077105520527754).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * 0.6657022142719949).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * -0.6973337290784535).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * 0.2607555203915459).on(cirq.GridQubit(7, 6)),
                cirq.rz(np.pi * 0.05398711507557042).on(cirq.GridQubit(8, 3)),
                cirq.rz(np.pi * -0.08342091351128843).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5390237928795745, phi=0.5165270526693762).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(0, 6)
                ),
                cirq.FSimGate(theta=1.6504170890091214, phi=0.5364505757789483).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.568670761625143, phi=0.5437849784272266).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.5465254433686004, phi=-5.727450888059412).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(2, 8)
                ),
                cirq.FSimGate(theta=1.2913067233725621, phi=0.47167387649514164).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.5381480272852108, phi=0.6090669301824796).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.5830570458423034, phi=0.5523056687078169).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.546350568481482, phi=0.4879631369282715).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.5326394193330342, phi=0.4395048201320801).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5745817206538912, phi=0.5078468553250708).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5287959808590572, phi=0.5477757594186843).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.4855370661448744, phi=0.5162805489497694).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.527373036078513, phi=0.5115160136560014).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.4411810311735318, phi=0.4660991447993951).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(5, 6)
                ),
                cirq.FSimGate(theta=1.4000192936015627, phi=0.45553928758281914).on(
                    cirq.GridQubit(5, 7), cirq.GridQubit(5, 8)
                ),
                cirq.FSimGate(theta=1.5800842999687046, phi=0.45282693980374283).on(
                    cirq.GridQubit(6, 1), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.518789513006022, phi=0.48179520284759936).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.529911511830527, phi=0.5594440380846348).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(6, 6)
                ),
                cirq.FSimGate(theta=1.4246757982684226, phi=0.4944809315999467).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.5296678467857068, phi=0.5740197418485297).on(
                    cirq.GridQubit(7, 5), cirq.GridQubit(7, 6)
                ),
                cirq.FSimGate(theta=1.4984631547270855, phi=0.49206955088399174).on(
                    cirq.GridQubit(8, 3), cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -0.7031344806936167).on(cirq.GridQubit(0, 5)),
                cirq.rz(np.pi * 0.7537461009300773).on(cirq.GridQubit(0, 6)),
                cirq.rz(np.pi * -0.5845337860294).on(cirq.GridQubit(1, 5)),
                cirq.rz(np.pi * 0.6725635052998734).on(cirq.GridQubit(1, 6)),
                cirq.rz(np.pi * -0.800076713100405).on(cirq.GridQubit(2, 5)),
                cirq.rz(np.pi * 0.7825869584994745).on(cirq.GridQubit(2, 6)),
                cirq.rz(np.pi * 0.743610934723634).on(cirq.GridQubit(2, 7)),
                cirq.rz(np.pi * 0.7988147979083485).on(cirq.GridQubit(2, 8)),
                cirq.rz(np.pi * 0.5590712696549931).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * -0.49594079882852876).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * -0.40105587278012).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 0.40490585588342615).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * -0.7187146107982795).on(cirq.GridQubit(3, 7)),
                cirq.rz(np.pi * 0.6911371842893561).on(cirq.GridQubit(3, 8)),
                cirq.rz(np.pi * -0.8923793028881776).on(cirq.GridQubit(4, 1)),
                cirq.rz(np.pi * 0.934936782527781).on(cirq.GridQubit(4, 2)),
                cirq.rz(np.pi * 0.7167045843075952).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -0.7743959061357405).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -0.3386839357713936).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * 0.5220725028954442).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * 0.8148796498999669).on(cirq.GridQubit(4, 7)),
                cirq.rz(np.pi * -0.8498672825242674).on(cirq.GridQubit(4, 8)),
                cirq.rz(np.pi * 0.5832210191614682).on(cirq.GridQubit(5, 1)),
                cirq.rz(np.pi * -0.5686259081889772).on(cirq.GridQubit(5, 2)),
                cirq.rz(np.pi * -0.2850375481560204).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * 0.39018386607872085).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 0.8050026546430838).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * 0.8790604659825868).on(cirq.GridQubit(5, 6)),
                cirq.rz(np.pi * -0.5053580048005596).on(cirq.GridQubit(5, 7)),
                cirq.rz(np.pi * 0.5312195821026124).on(cirq.GridQubit(5, 8)),
                cirq.rz(np.pi * 0.5065466572669878).on(cirq.GridQubit(6, 1)),
                cirq.rz(np.pi * -0.2771722207339199).on(cirq.GridQubit(6, 2)),
                cirq.rz(np.pi * 0.21839852268263724).on(cirq.GridQubit(6, 3)),
                cirq.rz(np.pi * -0.24133108022351474).on(cirq.GridQubit(6, 4)),
                cirq.rz(np.pi * -0.6980243283682508).on(cirq.GridQubit(6, 5)),
                cirq.rz(np.pi * 0.701491282797972).on(cirq.GridQubit(6, 6)),
                cirq.rz(np.pi * -0.08722128963329977).on(cirq.GridQubit(7, 3)),
                cirq.rz(np.pi * -0.33936594404193).on(cirq.GridQubit(7, 4)),
                cirq.rz(np.pi * 0.5033683710055986).on(cirq.GridQubit(7, 5)),
                cirq.rz(np.pi * -0.9399465796925085).on(cirq.GridQubit(7, 6)),
                cirq.rz(np.pi * 0.9757106337471518).on(cirq.GridQubit(8, 3)),
                cirq.rz(np.pi * 0.9948555678171301).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 1)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 9)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 0)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(9, 4)
                ),
            ]
        ),
    ]
)

