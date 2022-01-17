from qiskit import *
from qiskit.tools.monitor import job_monitor
import serial

IBMQ.save_account('your token here')

arduino = serial.Serial(port='COM19', baudrate=115200, timeout=.1)

qr=QuantumRegister(1)
cr=ClassicalRegister(1)

circuit=QuantumCircuit(qr,cr)
circuit.h(qr[0])
circuit.measure(qr,cr)

#simulator = Aer.get_backend('qasm_simulator')
#result = execute(circuit,backend=simulator, shots=1, memory=True).result()


#b=result.get_memory()[0]
#a=result.get_counts(circuit)

#arduino.write(bytes(b, 'utf-8'))

#print(a)
#print(b)


IBMQ.load_account()

provider = IBMQ.get_provider('ibm-q')

qcomp = provider.get_backend('ibmq_belem')

job = execute(circuit,backend=qcomp,shots=1, memory=True)
job_monitor(job)

result=job.result()

qa=result.get_counts(circuit)
qb=result.get_memory()[0]

arduino.write(bytes(qb, 'utf-8'))

print(qa)
print(qb)