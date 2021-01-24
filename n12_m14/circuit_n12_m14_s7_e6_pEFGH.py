import cirq
import numpy as np

QUBIT_ORDER = [
    cirq.GridQubit(3, 3),
    cirq.GridQubit(3, 4),
    cirq.GridQubit(3, 5),
    cirq.GridQubit(3, 6),
    cirq.GridQubit(4, 3),
    cirq.GridQubit(4, 4),
    cirq.GridQubit(4, 5),
    cirq.GridQubit(4, 6),
    cirq.GridQubit(5, 3),
    cirq.GridQubit(5, 4),
    cirq.GridQubit(5, 5),
    cirq.GridQubit(5, 6),
]

CIRCUIT = cirq.Circuit(
    [
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 0.2767373377033284).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * -0.18492941569567625).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -0.33113463396189063).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 0.40440704518468423).on(cirq.GridQubit(5, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5862983338115253, phi=0.5200148508319427).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5346175385256955, phi=0.5131039467233695).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(5, 5)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -0.6722145774944012).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * 0.7640224995020534).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 0.049341949396894985).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 0.02393046182589869).on(cirq.GridQubit(5, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -4.480708067260001).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 4.525888267898699).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 2.135954522972214).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -2.1822665205802965).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -3.7780476633662574).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * 3.817335880513747).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * 0.7811374803446167).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -0.6780279413275597).on(cirq.GridQubit(5, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.541977006124425, phi=0.6073798124875975).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.5138652502397498, phi=0.47710618607286504).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5849169442855044, phi=0.54346233613361).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5398075246432927, phi=0.5174515645943538).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(5, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 5.048199817882042).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -5.0030196172433445).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * -2.6543362735839113).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * 2.6080242759758283).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * 3.9045088495271663).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -3.8652206323796765).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -1.5516585295358842).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * 1.6547680685529413).on(cirq.GridQubit(5, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -3.2786928385561493).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * 3.339006443218924).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -5.390755870544794).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * 5.4172568990486605).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 4.367652291347506).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -3.9105776028384707).on(cirq.GridQubit(5, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.589821065740506, phi=0.5045391214115686).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5472406430590444, phi=0.5216932173558055).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.5707871303628709, phi=0.5176678491729374).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(5, 6)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 2.9425087256630427).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -2.882195121000268).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * 4.466531408750767).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -4.440030380246901).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * -4.89701654221443).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * 5.354091230723465).on(cirq.GridQubit(5, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 12.703597923836748).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * -12.7869629079138).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * 3.782562501914174).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -3.873596611893716).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * 4.772639843256901).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * -4.771314675186062).on(cirq.GridQubit(4, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.4668587973263782, phi=0.4976074601121169).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.603651215218248, phi=0.46649538437100246).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.6160334279232749, phi=0.4353897326147861).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(4, 6)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -12.477250219528523).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * 12.39388523545147).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -5.4898636407973544).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 5.398829530817813).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -5.863871460773714).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 5.8651966288445525).on(cirq.GridQubit(4, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 5.16073733770325).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * -5.068929415695599).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -3.587134633961795).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 3.6604070451845887).on(cirq.GridQubit(5, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5862983338115253, phi=0.5200148508319427).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5346175385256955, phi=0.5131039467233695).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(5, 5)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -5.556214577494324).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * 5.648022499501975).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 3.305341949396799).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * -3.232069538174005).on(cirq.GridQubit(5, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 7.565359127187911).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * -7.506809626368408).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * -15.28470806725993).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 15.329888267898626).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 7.019954522972137).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -7.066266520580219).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -13.842047663366333).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * 13.881335880513822).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * 3.001137480344569).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -2.8980279413275123).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 5.563573798571002).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * -5.8504123921354285).on(cirq.GridQubit(5, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.2947043217999283, phi=0.4859467238431821).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.541977006124425, phi=0.6073798124875975).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.5138652502397498, phi=0.47710618607286504).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5849169442855044, phi=0.54346233613361).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5398075246432927, phi=0.5174515645943538).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.4593314109380113, phi=0.5230636172671492).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(5, 6)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -7.378072351850649).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * 7.436621852670151).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * 15.852199817881967).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -15.80701961724327).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * -7.538336273583833).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * 7.492024275975751).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * 13.968508849527241).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -13.929220632379753).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -3.771658529535837).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * 3.874768068552894).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * -5.593307215154117).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * 5.30646862158969).on(cirq.GridQubit(5, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -8.162692838556204).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * 8.223006443218978).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -12.938755870544817).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * 12.965256899048683).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * -12.724144773112773).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * 12.73446915351482).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * 11.027652291347495).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -10.570577602838458).on(cirq.GridQubit(5, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.589821065740506, phi=0.5045391214115686).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5472406430590444, phi=0.5216932173558055).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.5124128267683938, phi=0.5133142626030278).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.5707871303628709, phi=0.5176678491729374).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(5, 6)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 7.826508725663096).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -7.7661951210003215).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * 12.014531408750791).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -11.988030380246926).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 11.590471496440383).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -11.580147116038336).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * -11.55701654221442).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * 12.014091230723457).on(cirq.GridQubit(5, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 26.023597923836856).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * -26.106962907913907).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * 25.356253063938887).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * -25.2805848307585).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * 8.370562501914259).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -8.461596611893802).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * 10.100639843256841).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * -10.099314675186001).on(cirq.GridQubit(4, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.4668587973263782, phi=0.4976074601121169).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.47511091993527, phi=0.538612093835262).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.603651215218248, phi=0.46649538437100246).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.6160334279232749, phi=0.4353897326147861).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(4, 6)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -25.79725021952863).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * 25.713885235451578).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -24.48288974563276).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * 24.55855797881315).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -10.07786364079744).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 9.986829530817898).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -11.191871460773655).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 11.193196628844492).on(cirq.GridQubit(4, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 10.044737337703173).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * -9.952929415695523).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -8.401251133882973).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * 8.52245467467511).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -6.843134633961698).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 6.916407045184491).on(cirq.GridQubit(5, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5862983338115253, phi=0.5200148508319427).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5289739216684795, phi=0.5055240639761313).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.5346175385256955, phi=0.5131039467233695).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(5, 5)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -10.440214577494247).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * 10.5320224995019).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 8.199075778124648).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -8.07787223733251).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * 6.561341949396702).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * -6.48806953817391).on(cirq.GridQubit(5, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 12.597359127188014).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * -12.538809626368511).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * -26.08870806725985).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 26.13388826789855).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 11.90395452297206).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -11.950266520580142).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -23.906047663366408).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * 23.945335880513902).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * 5.221137480344522).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -5.118027941327464).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 9.263573798570924).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * -9.55041239213535).on(cirq.GridQubit(5, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.2947043217999283, phi=0.4859467238431821).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.541977006124425, phi=0.6073798124875975).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.5138652502397498, phi=0.47710618607286504).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5849169442855044, phi=0.54346233613361).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5398075246432927, phi=0.5174515645943538).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.4593314109380113, phi=0.5230636172671492).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(5, 6)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -12.410072351850753).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * 12.468621852670255).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * 26.656199817881895).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -26.611019617243198).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * -12.422336273583753).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * 12.376024275975672).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * 24.032508849527318).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -23.993220632379824).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -5.991658529535789).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * 6.094768068552847).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * -9.293307215154037).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * 9.006468621589612).on(cirq.GridQubit(5, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -13.046692838556257).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * 13.107006443219033).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -20.486755870544844).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * 20.51325689904871).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * -19.82814477311278).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * 19.838469153514826).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * 17.687652291347487).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -17.230577602838448).on(cirq.GridQubit(5, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.589821065740506, phi=0.5045391214115686).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5472406430590444, phi=0.5216932173558055).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.5124128267683938, phi=0.5133142626030278).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.5707871303628709, phi=0.5176678491729374).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(5, 6)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 12.71050872566315).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -12.650195121000372).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * 19.562531408750814).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -19.53603038024695).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 18.69447149644039).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -18.684147116038343).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * -18.21701654221441).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * 18.674091230723448).on(cirq.GridQubit(5, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 39.34359792383697).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * -39.42696290791402).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * 38.52825306393881).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * -38.452584830758425).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * 12.958562501914345).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -13.049596611893888).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * 15.428639843256777).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * -15.42731467518594).on(cirq.GridQubit(4, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.4668587973263782, phi=0.4976074601121169).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.47511091993527, phi=0.538612093835262).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.603651215218248, phi=0.46649538437100246).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.6160334279232749, phi=0.4353897326147861).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(4, 6)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -39.11725021952874).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * 39.03388523545169).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -37.65488974563269).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * 37.730557978813074).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -14.665863640797525).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 14.574829530817984).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -16.519871460773594).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 16.52119662884443).on(cirq.GridQubit(4, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 14.928737337703097).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * -14.836929415695444).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -12.10125113388289).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * 12.22245467467503).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -10.099134633961603).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 10.172407045184396).on(cirq.GridQubit(5, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5862983338115253, phi=0.5200148508319427).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5289739216684795, phi=0.5055240639761313).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.5346175385256955, phi=0.5131039467233695).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(5, 5)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -15.32421457749417).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * 15.416022499501823).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 11.899075778124569).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -11.777872237332431).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * 9.817341949396608).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * -9.744069538173814).on(cirq.GridQubit(5, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * 17.629359127188117).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * -17.570809626368614).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * -36.89270806725978).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * 36.93788826789848).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * 16.787954522971983).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * -16.834266520580062).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * -33.970047663366486).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * 34.00933588051398).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * 7.441137480344476).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * -7.338027941327417).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * 12.963573798570843).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * -13.250412392135269).on(cirq.GridQubit(5, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.2947043217999283, phi=0.4859467238431821).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.541977006124425, phi=0.6073798124875975).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.5138652502397498, phi=0.47710618607286504).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5849169442855044, phi=0.54346233613361).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5398075246432927, phi=0.5174515645943538).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.4593314109380113, phi=0.5230636172671492).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(5, 6)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.rz(np.pi * -17.442072351850854).on(cirq.GridQubit(3, 3)),
                cirq.rz(np.pi * 17.500621852670356).on(cirq.GridQubit(3, 4)),
                cirq.rz(np.pi * 37.46019981788182).on(cirq.GridQubit(3, 5)),
                cirq.rz(np.pi * -37.415019617243125).on(cirq.GridQubit(3, 6)),
                cirq.rz(np.pi * -17.306336273583675).on(cirq.GridQubit(4, 3)),
                cirq.rz(np.pi * 17.260024275975592).on(cirq.GridQubit(4, 4)),
                cirq.rz(np.pi * 34.09650884952739).on(cirq.GridQubit(4, 5)),
                cirq.rz(np.pi * -34.057220632379895).on(cirq.GridQubit(4, 6)),
                cirq.rz(np.pi * -8.211658529535743).on(cirq.GridQubit(5, 3)),
                cirq.rz(np.pi * 8.3147680685528).on(cirq.GridQubit(5, 4)),
                cirq.rz(np.pi * -12.993307215153958).on(cirq.GridQubit(5, 5)),
                cirq.rz(np.pi * 12.706468621589535).on(cirq.GridQubit(5, 6)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
            ]
        ),
    ]
)

